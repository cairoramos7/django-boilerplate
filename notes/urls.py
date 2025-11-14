from django.urls import path

from notes.interfaces.api.views.note_detail import NoteDetailView
from notes.interfaces.api.views.note_list import NoteListView

# ;from .views import NoteListView, NoteDetailView


app_name = "notes"

urlpatterns = [
    path("notes/", NoteListView.as_view(), name="note-list"),
    path("notes/<int:note_id>/", NoteDetailView.as_view(), name="note-detail"),
]
