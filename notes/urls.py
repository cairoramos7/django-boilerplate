from django.urls import path

from notes.interfaces.api.views.note_detail import NoteDetailView
from notes.interfaces.api.views.note_list import NoteListView

app_name = "notes"

urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("<int:note_id>/", NoteDetailView.as_view(), name="note-detail"),
]
