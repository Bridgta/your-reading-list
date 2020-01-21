from django.shortcuts import render
from .models import Reading

# class Reading:
#     def __init__(self, title, author, description, pages):
#         self.title = title
#         self.author = author
#         self.description = description
#         self.pages = pages

readings = [
    Reading('Eloquent Javascript', 'Et el.', 'Explore the complexities of the language of Javascript', 880),
    Reading('Cats Cradle', 'Kurt Vonnegut', 'Find the way of Bokonon', 300),
    Reading('NY Times Aticle', 'Anon.', '2020 geopolitical outlooks and perdictions', 4)
]


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def readings_index(request):
    readings = Reading.objects.all()
    return render(request, 'readings/index.html', { 'readings': readings })

def readings_detail(request, reading_id):
    reading = Reading.objects.get(id=reading_id)
    return render(request, 'readings/detail.html', { 'reading': reading })