from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Note:
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    id: Optional[int] = None

    def create(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title: str, content: str):
        self.title = title
        self.content = content
        self.updated_at = datetime.now()
