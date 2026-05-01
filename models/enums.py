"""Stub enums module - placeholders for undefined enums used in test_models.py."""

from enum import Enum


class MemoryScope(str, Enum):
    """Memory scope enum."""
    USER = "user"
    SESSION = "session"
    GLOBAL = "global"
    WORKSPACE = "workspace"


class ExecutionLanguage(str, Enum):
    """Execution language enum."""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    BASH = "bash"
    GO = "go"
    RUST = "rust"


class PatternType(str, Enum):
    """Pattern type enum."""
    REGEX = "regex"
    GLOB = "glob"
    CODE_STYLE = "code_style"
    ERROR_RESOLUTION = "error_resolution"
    TOOL_USAGE = "tool_usage"
    WORKFLOW = "workflow"
    PREFERENCE = "preference"
    CONTEXT = "context"
    CUSTOM = "custom"


class ErrorCode(str, Enum):
    """Error code enum."""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    RATE_LIMITED = "RATE_LIMITED"
    EXECUTION_FAILED = "EXECUTION_FAILED"
    EXECUTION_TIMEOUT = "EXECUTION_TIMEOUT"
    MEMORY_LIMIT_EXCEEDED = "MEMORY_LIMIT_EXCEEDED"
    STORAGE_ERROR = "STORAGE_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    AUTHENTICATION_REQUIRED = "AUTHENTICATION_REQUIRED"
    INVALID_TOKEN = "INVALID_TOKEN"
