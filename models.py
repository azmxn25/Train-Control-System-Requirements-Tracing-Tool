from dataclasses import dataclass
from typing import Optional

@dataclass
class Requirement:
    id: str
    description: str
    parent_id: Optional[str]
    category: str  # e.g., 'Customer', 'System', 'Subsystem'
