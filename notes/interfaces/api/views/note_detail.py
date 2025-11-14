from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from notes.application.use_cases import NoteUseCases
from notes.infrastructure.repositories import NoteRepository
from notes.interfaces.api.views.mixins import NoteEntityMixin


class NoteDetailView(APIView, NoteEntityMixin):
    def get(self, request, note_id, format=None):
        """
        GET /api/notes/{note_id}/
        Returns a note by its ID.
        """
        use_case = NoteUseCases(note_repository=NoteRepository())
        note = use_case.get(note_id)
        data = self._entity_to_dict(note)
        return Response(data)

    def put(self, request, note_id, format=None):
        """
        PUT /api/notes/{note_id}/
        Updates a note by its ID.
        """
        use_case = NoteUseCases(note_repository=NoteRepository())

        # Extrai title e content de request.data
        title = request.data.get("title")
        content = request.data.get("content")

        # Verifica se title e content foram fornecidos
        if not title or not content:
            return Response(
                {"error": "Title and content are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        note = use_case.update(note_id, title, content)

        if note is None:
            return Response(
                {"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND
            )

        data = self._entity_to_dict(note)
        return Response(data)

    def delete(self, request, note_id, format=None):
        """
        DELETE /api/notes/{note_id}/
        Deletes a note by its ID.
        """
        use_case = NoteUseCases(note_repository=NoteRepository())
        use_case.delete(note_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
