"""Stub core module - placeholder for undefined core types used in test_models.py."""

from typing import Any, Dict, Optional, List


class UserContext:
    """User execution context with permissions and metadata."""
    def __init__(self, user_id: str, device_id: Optional[str] = None,
                 session_id: Optional[str] = None, project_id: Optional[str] = None,
                 workspace_id: Optional[str] = None, cwd: Optional[str] = None,
                 context: Optional[Dict[str, Any]] = None,
                 permissions: Optional[List[str]] = None,
                 metadata: Optional[Dict[str, Any]] = None,
                 request_id: Optional[str] = None,
                 trace_id: Optional[str] = None, **kwargs):
        self.user_id = user_id
        self.device_id = device_id
        self.session_id = session_id
        self.project_id = project_id
        self.workspace_id = workspace_id
        self.cwd = cwd
        self.context = context or {}
        self.permissions = permissions or []
        self.metadata = metadata or {}
        self.request_id = request_id
        self.trace_id = trace_id

    def has_permission(self, perm: str) -> bool:
        """Check if user has a permission."""
        return perm in self.permissions or "*" in self.permissions

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        result = {}
        for k, v in self.__dict__.items():
            if v is not None:
                result[k] = v
        return result

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserContext":
        """Create from dictionary."""
        return cls(**data)


class SmartCPError:
    """SmartCP error response."""
    def __init__(self, error: str, error_code: str,
                 details: Optional[Dict[str, Any]] = None,
                 request_id: Optional[str] = None):
        self.success = False
        self.error = error
        self.error_code = error_code
        self.details = details
        self.request_id = request_id

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {
            k: v for k, v in self.__dict__.items()
            if v is not None
        }
