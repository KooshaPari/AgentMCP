"""Tests for models/schemas.py."""

import pytest
from pydantic import ValidationError
from models.schemas import (
    MessageSchema,
    ContextSchema,
    ExecuteCodeRequest,
    ExecuteCodeResponse,
)
from models.enums import ExecutionLanguage


class TestMessageSchema:
    """Tests for MessageSchema."""

    def test_message_schema_creation(self):
        """Test basic MessageSchema creation."""
        msg = MessageSchema(role="user", content="Hello")
        assert msg.role == "user"
        assert msg.content == "Hello"

    def test_message_schema_missing_fields(self):
        """Test MessageSchema requires both fields."""
        with pytest.raises(ValidationError):
            MessageSchema(role="user")

        with pytest.raises(ValidationError):
            MessageSchema(content="Hello")


class TestContextSchema:
    """Tests for ContextSchema."""

    def test_context_schema_required_fields(self):
        """Test ContextSchema requires user_id."""
        ctx = ContextSchema(user_id="user123")
        assert ctx.user_id == "user123"
        assert ctx.session_id is None

    def test_context_schema_optional_session_id(self):
        """Test ContextSchema with optional session_id."""
        ctx = ContextSchema(user_id="user123", session_id="session456")
        assert ctx.user_id == "user123"
        assert ctx.session_id == "session456"


class TestExecuteCodeRequest:
    """Tests for ExecuteCodeRequest schema."""

    def test_execute_code_request_defaults(self):
        """Test ExecuteCodeRequest default values."""
        req = ExecuteCodeRequest(code="print('hello')")
        assert req.code == "print('hello')"
        assert req.language == ExecutionLanguage.PYTHON
        assert req.timeout == 30
        assert req.max_output_size == 10000
        assert req.context == {}

    def test_execute_code_request_with_language_string(self):
        """Test ExecuteCodeRequest with language as string."""
        req = ExecuteCodeRequest(code="console.log('hi')", language="javascript")
        assert req.language == ExecutionLanguage.JAVASCRIPT

    def test_execute_code_request_with_language_enum(self):
        """Test ExecuteCodeRequest with language as enum."""
        req = ExecuteCodeRequest(code="echo hello", language=ExecutionLanguage.BASH)
        assert req.language == ExecutionLanguage.BASH

    def test_execute_code_request_with_custom_timeout(self):
        """Test ExecuteCodeRequest with custom timeout."""
        req = ExecuteCodeRequest(code="sleep 5", timeout=60)
        assert req.timeout == 60

    def test_execute_code_request_timeout_minimum(self):
        """Test ExecuteCodeRequest timeout minimum validation."""
        with pytest.raises(ValidationError):
            ExecuteCodeRequest(code="print('hi')", timeout=0)

    def test_execute_code_request_timeout_maximum(self):
        """Test ExecuteCodeRequest timeout maximum validation."""
        with pytest.raises(ValidationError):
            ExecuteCodeRequest(code="print('hi')", timeout=301)

    def test_execute_code_request_invalid_language(self):
        """Test ExecuteCodeRequest invalid language raises error."""
        with pytest.raises(ValidationError):
            ExecuteCodeRequest(code="code", language="invalid_lang")

    def test_execute_code_request_with_context(self):
        """Test ExecuteCodeRequest with context dictionary."""
        req = ExecuteCodeRequest(
            code="print(x)",
            context={"x": 42},
        )
        assert req.context == {"x": 42}

    def test_execute_code_request_with_max_output_size(self):
        """Test ExecuteCodeRequest with custom max_output_size."""
        req = ExecuteCodeRequest(
            code="big_output",
            max_output_size=5000,
        )
        assert req.max_output_size == 5000


class TestExecuteCodeResponse:
    """Tests for ExecuteCodeResponse schema."""

    def test_execute_code_response_required_fields(self):
        """Test ExecuteCodeResponse requires execution_id."""
        resp = ExecuteCodeResponse(execution_id="exec-123")
        assert resp.execution_id == "exec-123"
        assert resp.status == "success"
        assert resp.result is None
        assert resp.error is None
        assert resp.output is None
        assert resp.variables == []

    def test_execute_code_response_with_result(self):
        """Test ExecuteCodeResponse with result."""
        resp = ExecuteCodeResponse(
            execution_id="exec-123",
            result={"output": "hello"},
        )
        assert resp.result == {"output": "hello"}

    def test_execute_code_response_with_error(self):
        """Test ExecuteCodeResponse with error."""
        resp = ExecuteCodeResponse(
            execution_id="exec-123",
            status="error",
            error="Something went wrong",
        )
        assert resp.status == "error"
        assert resp.error == "Something went wrong"

    def test_execute_code_response_with_output(self):
        """Test ExecuteCodeResponse with output."""
        resp = ExecuteCodeResponse(
            execution_id="exec-123",
            output="Hello World\n",
        )
        assert resp.output == "Hello World\n"

    def test_execute_code_response_with_variables(self):
        """Test ExecuteCodeResponse with variables."""
        resp = ExecuteCodeResponse(
            execution_id="exec-123",
            variables=["x", "y", "result"],
        )
        assert resp.variables == ["x", "y", "result"]

    def test_execute_code_response_with_execution_time(self):
        """Test ExecuteCodeResponse with execution_time_ms."""
        resp = ExecuteCodeResponse(
            execution_id="exec-123",
            execution_time_ms=125.5,
        )
        assert resp.execution_time_ms == 125.5

    def test_execute_code_response_full_example(self):
        """Test ExecuteCodeResponse with all fields."""
        resp = ExecuteCodeResponse(
            execution_id="exec-456",
            status="success",
            result={"return_value": 42},
            output="42\n",
            variables=["x", "y"],
            execution_time_ms=50.123,
        )
        assert resp.execution_id == "exec-456"
        assert resp.status == "success"
        assert resp.result == {"return_value": 42}
        assert resp.output == "42\n"
        assert resp.variables == ["x", "y"]
        assert resp.execution_time_ms == 50.123
