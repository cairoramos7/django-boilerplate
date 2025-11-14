from notes.domain import NoteEntity
from notes.infrastructure.models.note_model import NoteModel


def to_entity(note_model: NoteModel) -> NoteEntity:
    return NoteEntity(
        id=note_model.id,
        title=note_model.title,
        content=note_model.content,
        created_at=note_model.created_at,
        updated_at=note_model.updated_at,
    )


def to_model(note_entity: NoteEntity) -> NoteModel:
    if note_entity.id:
        try:
            note_model = NoteModel.objects.get(id=note_entity.id)
        except NoteModel.DoesNotExist:
            note_model = NoteModel()

    else:
        note_model = NoteModel()

    note_model.title = note_entity.title
    model.title = note_entity.title
    model.content = note_entity.content

    return model
