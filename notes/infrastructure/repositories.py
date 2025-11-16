from typing import List, Optional
from notes.domain import NoteEntity, NoteRepositoryInterface
from notes.infrastructure.models.note_model import NoteModel
from notes.infrastructure import mappers


class NoteRepository(NoteRepositoryInterface):
    def get(self, note_id: int) -> Optional[NoteEntity]:
        try:
            return mappers.to_entity(NoteModel.objects.get(id=note_id))
        except NoteModel.DoesNotExist:
            return None

    def all(self) -> List[NoteEntity]:
        return [mappers.to_entity(note_model) for note_model in NoteModel.objects.all()]

    def create(self, note: NoteEntity) -> NoteEntity:
        note_model = mappers.to_model(note)
        note_model.save()
        return mappers.to_entity(note_model)

    def update(self, note: NoteEntity) -> NoteEntity:
        note_model = mappers.to_model(note)
        note_model.save()
        return mappers.to_entity(note_model)

    def delete(self, note_id: int) -> None:
        try:
            note_model = NoteModel.objects.get(id=note_id)
            note_model.delete()
        except NoteModel.DoesNotExist:
            pass
