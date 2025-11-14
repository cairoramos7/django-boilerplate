from abc import ABC
from typing import List, Optional
from notes.domain import NoteEntity


class NoteRepositoryInterface(ABC):
    def get(self, note_id: int) -> Optional[NoteEntity]:
        pass

    def all(self) -> List[NoteEntity]:
        pass

    def create(self, note: NoteEntity) -> NoteEntity:
        pass

    def update(self, note: NoteEntity) -> NoteEntity:
        pass

    def delete(self, note_id: int) -> None:
        pass
