from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reading
from .forms import ReadForm


class ReadingCreate(CreateView):
    model = Reading
    fields = '__all__'

class ReadingUpdate(UpdateView):
    model = Reading
    fields = ['title', 'description', 'pages']

class ReadingDelete(DeleteView):
    model = Reading
    success_url = '/readings/'

# readings = [
#     Reading('NY Times Aticle', 'Anon.', '2020 geopolitical outlooks and perdictions', 4)
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def readings_index(request):
    readings = Reading.objects.all()
    return render(request, 'readings/index.html', { 'readings': readings })

def readings_detail(request, reading_id):
    reading = Reading.objects.get(id=reading_id)
    read_form = ReadForm()
    return render(request, 'readings/detail.html', { 'reading': reading, 'read_form': read_form })

def add_read(request, reading_id):
    form = ReadForm(request.POST)
    if form.is_valid():
        new_read = form.save(commit=False)
        new_read.reading_id = reading_id
        new_read.save()
    return redirect('detail', reading_id=reading_id)
