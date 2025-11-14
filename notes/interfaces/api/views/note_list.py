from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.application.use_cases import NoteUseCases
from notes.infrastructure.repositories import NoteRepository
from notes.interfaces.api.views.mixins import NoteEntityMixin


class NoteListView(APIView, NoteEntityMixin):
    def get(self, request, format=None):
        """
        GET /api/notes/
        Returns a list of all notes.
        """
        use_case = NoteUseCases(note_repository=NoteRepository())
        notes = use_case.all()
        data = [self._entity_to_dict(note) for note in notes]
        return Response(data)
