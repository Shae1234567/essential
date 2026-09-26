from abc import ABC, abstractmethod
import requests
from typing import Any, Dict, List, Optional

class Tool(ABC):
    """Base class for all tools in the system."""
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool with given arguments. Must be implemented by subclasses."""
        pass

class ToolRegistry:
    """Central registry for managing all tools in the system."""
    
    _tools: Dict[str, Tool] = {}
    
    @classmethod
    def register(cls, name: str, tool: Tool):
        """Register a new tool with the registry."""
        cls._tools[name] = tool
    
    @classmethod
    def get_tool(cls, name: str) -> Optional[Tool]:
        """Retrieve a tool by name."""
        return cls._tools.get(name)
    
    @classmethod
    def list_tools(cls) -> List[str]:
        """List all registered tools."""
        return list(cls._tools.keys())
