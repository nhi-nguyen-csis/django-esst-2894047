from django.shortcuts import render
from notes.models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView

# Create your views here.
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, "notes/notes_list.html", {
#         'notes': all_notes,
#     })

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')

#     return render(request, 'notes/notes_detail.html', {'note': note})

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" #optional


class NotesDetail(DetailView):
    model = Notes
    context_object_name = "note" 

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" 
    queryset = Notes.objects.filter(likes__gte=1)
