"""Tests for models/enums.py."""

import pytest
from models.enums import (
    MemoryScope,
    ExecutionLanguage,
    PatternType,
    ErrorCode,
)


class TestMemoryScope:
    """Tests for MemoryScope enum."""

    def test_memory_scope_values(self):
        """Test all MemoryScope enum values exist."""
        assert MemoryScope.USER.value == "user"
        assert MemoryScope.SESSION.value == "session"
        assert MemoryScope.GLOBAL.value == "global"
        assert MemoryScope.WORKSPACE.value == "workspace"

    def test_memory_scope_is_string_enum(self):
        """Test MemoryScope inherits from str."""
        assert isinstance(MemoryScope.USER, str)

    def test_memory_scope_from_string(self):
        """Test creating MemoryScope from string value."""
        assert MemoryScope("user") == MemoryScope.USER
        assert MemoryScope("session") == MemoryScope.SESSION

    def test_memory_scope_invalid_value(self):
        """Test invalid MemoryScope value raises error."""
        with pytest.raises(ValueError):
            MemoryScope("invalid")


class TestExecutionLanguage:
    """Tests for ExecutionLanguage enum."""

    def test_execution_language_values(self):
        """Test all ExecutionLanguage enum values exist."""
        assert ExecutionLanguage.PYTHON.value == "python"
        assert ExecutionLanguage.JAVASCRIPT.value == "javascript"
        assert ExecutionLanguage.TYPESCRIPT.value == "typescript"
        assert ExecutionLanguage.BASH.value == "bash"
        assert ExecutionLanguage.GO.value == "go"
        assert ExecutionLanguage.RUST.value == "rust"

    def test_execution_language_is_string_enum(self):
        """Test ExecutionLanguage inherits from str."""
        assert isinstance(ExecutionLanguage.PYTHON, str)

    def test_execution_language_from_string(self):
        """Test creating ExecutionLanguage from string value."""
        assert ExecutionLanguage("python") == ExecutionLanguage.PYTHON
        assert ExecutionLanguage("bash") == ExecutionLanguage.BASH

    def test_execution_language_invalid_value(self):
        """Test invalid ExecutionLanguage value raises error."""
        with pytest.raises(ValueError):
            ExecutionLanguage("cobol")


class TestPatternType:
    """Tests for PatternType enum."""

    def test_pattern_type_values(self):
        """Test all PatternType enum values exist."""
        assert PatternType.REGEX.value == "regex"
        assert PatternType.GLOB.value == "glob"
        assert PatternType.CODE_STYLE.value == "code_style"
        assert PatternType.ERROR_RESOLUTION.value == "error_resolution"
        assert PatternType.TOOL_USAGE.value == "tool_usage"
        assert PatternType.WORKFLOW.value == "workflow"
        assert PatternType.PREFERENCE.value == "preference"
        assert PatternType.CONTEXT.value == "context"
        assert PatternType.CUSTOM.value == "custom"

    def test_pattern_type_is_string_enum(self):
        """Test PatternType inherits from str."""
        assert isinstance(PatternType.REGEX, str)

    def test_pattern_type_from_string(self):
        """Test creating PatternType from string value."""
        assert PatternType("regex") == PatternType.REGEX
        assert PatternType("custom") == PatternType.CUSTOM

    def test_pattern_type_invalid_value(self):
        """Test invalid PatternType value raises error."""
        with pytest.raises(ValueError):
            PatternType("invalid")


class TestErrorCode:
    """Tests for ErrorCode enum."""

    def test_error_code_values(self):
        """Test all ErrorCode enum values exist."""
        assert ErrorCode.VALIDATION_ERROR.value == "VALIDATION_ERROR"
        assert ErrorCode.NOT_FOUND.value == "NOT_FOUND"
        assert ErrorCode.PERMISSION_DENIED.value == "PERMISSION_DENIED"
        assert ErrorCode.RATE_LIMITED.value == "RATE_LIMITED"
        assert ErrorCode.EXECUTION_FAILED.value == "EXECUTION_FAILED"
        assert ErrorCode.EXECUTION_TIMEOUT.value == "EXECUTION_TIMEOUT"
        assert ErrorCode.MEMORY_LIMIT_EXCEEDED.value == "MEMORY_LIMIT_EXCEEDED"
        assert ErrorCode.STORAGE_ERROR.value == "STORAGE_ERROR"
        assert ErrorCode.INTERNAL_ERROR.value == "INTERNAL_ERROR"
        assert ErrorCode.AUTHENTICATION_REQUIRED.value == "AUTHENTICATION_REQUIRED"
        assert ErrorCode.INVALID_TOKEN.value == "INVALID_TOKEN"

    def test_error_code_is_string_enum(self):
        """Test ErrorCode inherits from str."""
        assert isinstance(ErrorCode.INTERNAL_ERROR, str)

    def test_error_code_from_string(self):
        """Test creating ErrorCode from string value."""
        assert ErrorCode("NOT_FOUND") == ErrorCode.NOT_FOUND
        assert ErrorCode("INTERNAL_ERROR") == ErrorCode.INTERNAL_ERROR

    def test_error_code_invalid_value(self):
        """Test invalid ErrorCode value raises error."""
        with pytest.raises(ValueError):
            ErrorCode("INVALID_ERROR_CODE")
