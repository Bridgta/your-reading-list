from django.shortcuts import render

from .models import Reading

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def readings_index(request):
    return render(request, 'readings/index.html', { 'reading': reading })

class Reading:
    def __init__(self, title, author, description, pages):
        self.title = title
        self.author = author
        self.description = description
        self.pages = pages

readings = [
    Reading('Eloquent Javascript', 'Et el.', 'Explore the complexities of the language of Javascript', 880),
    Reading('Cats Cradle', 'Kurt Vonnegut', 'Find the way of Bokonon', 300),
    Reading('NY Times Aticle', 'Anon.', '2020 geopolitical outlooks and perdictions', 4)
]