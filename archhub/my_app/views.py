from django.shortcuts import render
# from django.http import HttpResponse


class Place:
    def __init__(self, name, location, style, year):
        self.name = name 
        self.location = location
        self.style = style
        self.year = year

places = [
    Place("Mushroom Beach House", "San Diego, CA", "Futuristic", 1968),
    Place("Donut Hole", "La Puente, CA", "Novelty", 1968),
    Place("Wayfarers Chapel", "Rancho Palos Verdes, CA", "Modern", 1951),
    Place("Union 76 Gas Station", "Los Angeles, CA", "Googie", 1965),
    Place("Chemosphere", "Los Angeles, CA", "Futuristic", 1960),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def place_index(request):
    # 'places' is the variable name (place) in places/index.html
    return render(request, 'places/index.html', {'places': places})
