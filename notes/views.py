from django.shortcuts import render
from notes.models import Notes

# Create your views here.
def list(request):
    all_notes = Notes.objects.all()
    return render(request, "notes/notes_list.html", {
        'notes': all_notes,
    })