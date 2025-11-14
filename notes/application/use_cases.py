from typing import List, Optional
from notes.infrastructure.repositories import NoteRepository
from notes.domain import NoteEntity, NoteRepositoryInterface


class NoteUseCases:
    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository

    def create(self, title: str, content: str) -> NoteEntity:
        note = NoteEntity(title=title, content=content)
        return self.note_repository.create(note)

    def get(self, note_id: int) -> Optional[NoteEntity]:
        return self.note_repository.get(note_id)

    def all(self) -> List[NoteEntity]:
        return self.note_repository.all()

    def update(self, note_id: int, title: str, content: str) -> Optional[NoteEntity]:
        note = self.note_repository.get(note_id)
        if note is None:
            return None
        note.update(title, content)
        return self.note_repository.update(note)

    def delete(self, note_id: int) -> None:
        self.note_repository.delete(note_id)
