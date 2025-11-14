class NoteEntityMixin:
    def _entity_to_dict(self, entity):
        return {
            "id": entity.id,
            "title": entity.title,
            "content": entity.content,
            "created_at": entity.created_at,
            "updated_at": entity.updated_at,
        }
