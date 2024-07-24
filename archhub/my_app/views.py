# my_app/views.py

from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from .models import Place, Architect
from .forms import HoursForm

class PlaceCreate(CreateView):
    model = Place
    fields = '__all__'

class PlaceUpdate(UpdateView):
    model = Place
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['location', 'style', 'year']

class PlaceDelete(DeleteView):
    model = Place
    success_url = '/places/'

class ArchitectCreate(CreateView):
    model = Architect
    fields = '__all__'

class ArchitectList(ListView):
    model = Architect

class ArchitectDetail(DetailView):
    model = Architect

class ArchitectUpdate(UpdateView):
    model = Architect
    fields = ['bio']

class ArchitectDelete(DeleteView):
    model = Architect
    success_url = '/architects/'
    

# class Place:
#     def __init__(self, name, location, style, year):
#         self.name = name 
#         self.location = location
#         self.style = style
#         self.year = year

# places = [
#     Place("Mushroom Beach House", "San Diego, CA", "Futuristic", 1968),
#     Place("Donut Hole", "La Puente, CA", "Novelty", 1968),
#     Place("Wayfarers Chapel", "Rancho Palos Verdes, CA", "Modern", 1951),
#     Place("Union 76 Gas Station", "Los Angeles, CA", "Googie", 1965),
#     Place("Chemosphere", "Los Angeles, CA", "Futuristic", 1960),
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def place_index(request):
    # 'places' is the variable name (place) in places/index.html
    places = Place.objects.all()
    return render(request, 'places/index.html', {'places': places})

def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    hours_form = HoursForm()
    return render(request, 'places/detail.html', {'place': place, 'hours_form': hours_form})

def add_hours(request, place_id):
    form = HoursForm(request.POST)
    if form.is_valid():
        hour = form.save(commit=False)
        hour.place_id = place_id
        hour.save()
    return redirect('place-detail', place_id=place_id)


    # place = Place.objects.get(id=place_id)
    # form = HoursForm(request.POST)
    # if form.is_valid():
    #     hour = form.save(commit=False)
    #     hour.place = place
    #     hour.save()
    # return render(request, 'places/detail.html', {'place': place})