"""Tests for models/core.py."""

import pytest
from models.core import UserContext, SmartCPError


class TestUserContext:
    """Tests for UserContext class."""

    def test_user_context_creation(self):
        """Test basic UserContext creation."""
        ctx = UserContext(user_id="user123")
        assert ctx.user_id == "user123"
        assert ctx.device_id is None
        assert ctx.session_id is None
        assert ctx.project_id is None
        assert ctx.workspace_id is None
        assert ctx.cwd is None

    def test_user_context_with_optional_params(self):
        """Test UserContext creation with optional parameters."""
        ctx = UserContext(
            user_id="user123",
            device_id="device456",
            session_id="session789",
            project_id="project001",
            workspace_id="workspace002",
            cwd="/path/to/work",
        )
        assert ctx.user_id == "user123"
        assert ctx.device_id == "device456"
        assert ctx.session_id == "session789"
        assert ctx.project_id == "project001"
        assert ctx.workspace_id == "workspace002"
        assert ctx.cwd == "/path/to/work"

    def test_user_context_with_context_dict(self):
        """Test UserContext with context dictionary."""
        ctx = UserContext(
            user_id="user123",
            context={"key": "value", "number": 42},
        )
        assert ctx.context == {"key": "value", "number": 42}

    def test_user_context_with_permissions(self):
        """Test UserContext with permissions list."""
        ctx = UserContext(
            user_id="user123",
            permissions=["read", "write", "execute"],
        )
        assert ctx.permissions == ["read", "write", "execute"]

    def test_user_context_with_metadata(self):
        """Test UserContext with metadata dictionary."""
        ctx = UserContext(
            user_id="user123",
            metadata={"role": "admin", "level": 5},
        )
        assert ctx.metadata == {"role": "admin", "level": 5}

    def test_user_context_with_request_trace_ids(self):
        """Test UserContext with request_id and trace_id."""
        ctx = UserContext(
            user_id="user123",
            request_id="req-001",
            trace_id="trace-abc",
        )
        assert ctx.request_id == "req-001"
        assert ctx.trace_id == "trace-abc"

    def test_user_context_has_permission(self):
        """Test has_permission method."""
        ctx = UserContext(
            user_id="user123",
            permissions=["read", "write"],
        )
        assert ctx.has_permission("read") is True
        assert ctx.has_permission("write") is True
        assert ctx.has_permission("delete") is False

    def test_user_context_has_permission_wildcard(self):
        """Test has_permission with wildcard permission."""
        ctx = UserContext(
            user_id="user123",
            permissions=["*"],
        )
        assert ctx.has_permission("read") is True
        assert ctx.has_permission("write") is True
        assert ctx.has_permission("anything") is True

    def test_user_context_to_dict(self):
        """Test to_dict method excludes None values."""
        ctx = UserContext(user_id="user123", device_id="device456")
        d = ctx.to_dict()
        assert "user_id" in d
        assert "device_id" in d
        assert d["user_id"] == "user123"
        assert d["device_id"] == "device456"
        # None values should be excluded
        assert "session_id" not in d

    def test_user_context_to_dict_includes_all_non_none(self):
        """Test to_dict includes all non-None values."""
        ctx = UserContext(
            user_id="user123",
            permissions=["read"],
            metadata={"key": "value"},
        )
        d = ctx.to_dict()
        assert d["user_id"] == "user123"
        assert d["permissions"] == ["read"]
        assert d["metadata"] == {"key": "value"}

    def test_user_context_from_dict(self):
        """Test from_dict class method."""
        data = {
            "user_id": "user123",
            "device_id": "device456",
            "session_id": "session789",
            "permissions": ["read"],
        }
        ctx = UserContext.from_dict(data)
        assert ctx.user_id == "user123"
        assert ctx.device_id == "device456"
        assert ctx.session_id == "session789"
        assert ctx.permissions == ["read"]

    def test_user_context_roundtrip(self):
        """Test UserContext to_dict/from_dict roundtrip."""
        original = UserContext(
            user_id="user123",
            device_id="device456",
            session_id="session789",
            permissions=["read", "write"],
            metadata={"key": "value"},
        )
        d = original.to_dict()
        restored = UserContext.from_dict(d)
        assert restored.user_id == original.user_id
        assert restored.device_id == original.device_id
        assert restored.session_id == original.session_id
        assert restored.permissions == original.permissions
        assert restored.metadata == original.metadata


class TestSmartCPError:
    """Tests for SmartCPError class."""

    def test_smartcp_error_creation(self):
        """Test basic SmartCPError creation."""
        err = SmartCPError(
            error="Something went wrong",
            error_code="INTERNAL_ERROR",
        )
        assert err.success is False
        assert err.error == "Something went wrong"
        assert err.error_code == "INTERNAL_ERROR"
        assert err.details is None
        assert err.request_id is None

    def test_smartcp_error_with_details(self):
        """Test SmartCPError with details dictionary."""
        err = SmartCPError(
            error="Validation failed",
            error_code="VALIDATION_ERROR",
            details={"field": "email", "reason": "invalid format"},
        )
        assert err.details == {"field": "email", "reason": "invalid format"}

    def test_smartcp_error_with_request_id(self):
        """Test SmartCPError with request_id."""
        err = SmartCPError(
            error="Not found",
            error_code="NOT_FOUND",
            request_id="req-123",
        )
        assert err.request_id == "req-123"

    def test_smartcp_error_to_dict(self):
        """Test to_dict method excludes None values."""
        err = SmartCPError(
            error="Error message",
            error_code="ERROR_CODE",
        )
        d = err.to_dict()
        assert "success" in d
        assert "error" in d
        assert "error_code" in d
        assert d["success"] is False
        assert d["error"] == "Error message"
        assert d["error_code"] == "ERROR_CODE"
        # None values should be excluded
        assert "details" not in d
        assert "request_id" not in d

    def test_smartcp_error_to_dict_with_optionals(self):
        """Test to_dict includes non-None optional values."""
        err = SmartCPError(
            error="Error",
            error_code="CODE",
            details={"key": "value"},
            request_id="req-001",
        )
        d = err.to_dict()
        assert d["details"] == {"key": "value"}
        assert d["request_id"] == "req-001"
