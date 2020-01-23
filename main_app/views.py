from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Reading, Note
from .forms import ReadForm


class ReadingCreate(CreateView):
    model = Reading
    fields = '__all__'
    success_url = '/readings/'

class ReadingUpdate(UpdateView):
    model = Reading
    fields = '__all__'
    success_url = '/readings/'

class ReadingDelete(DeleteView):
    model = Reading
    success_url = '/readings/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def readings_index(request):
    readings = Reading.objects.all()
    return render(request, 'readings/index.html', { 'readings': readings })

def readings_detail(request, reading_id):
    reading = Reading.objects.get(id=reading_id)
    notes_reading_doesnt_have = Reading.objects.exclude(id__in = reading.notes.all().values_list('id'))
    read_form = ReadForm()
    return render(request, 'readings/detail.html', { 'reading': reading, 'read_form': read_form, 'notes': notes_reading_doesnt_have})

def add_read(request, reading_id):
    form = ReadForm(request.POST)
    if form.is_valid():
        new_read = form.save(commit=False)
        new_read.reading_id = reading_id
        new_read.save()
    return redirect('detail', reading_id=reading_id)

def assoc_note(request, reading_id, note_id):
    Reading.objects.get(id=reading_id).notes.add(note_id)
    return redirect('detail', note_id=note_id)

class NoteList(ListView):
    model = Note

class NoteDetail(DetailView):
    model = Note

class NoteCreate(CreateView):
    model = Note
    fields = '__all__'

class NoteUpdate(UpdateView):
    model = Note
    fields = ['quote']

class NoteDelete(DeleteView):
    model = Note
    success_url = '/notes/'