# from django.urls import path
# from notes.views import list, detail

# urlpatterns = [path("notes", list, name="list"), path(f'notes/<int:pk>', detail, name="detail"),]

from django.urls import path
from notes.views import NotesListView, NotesDetail, PopularNotesListView

urlpatterns = [path("notes", NotesListView.as_view(), name="notes.list"), 
               path('notes/<int:pk>', NotesDetail.as_view(), name="notes.detail"),
                path('notes/<int:pk>', PopularNotesListView.as_view(), name="notes.popular"),]