# my_app/views.py

from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Place, Architect
from .forms import HoursForm

class PlaceCreate(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['name', 'location', 'style', 'year']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaceUpdate(LoginRequiredMixin, UpdateView):
    model = Place
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['location', 'style', 'year']

class PlaceDelete(LoginRequiredMixin, DeleteView):
    model = Place
    success_url = '/places/'

class ArchitectCreate(LoginRequiredMixin, CreateView):
    model = Architect
    fields = '__all__'

class ArchitectList(LoginRequiredMixin, ListView):
    model = Architect

class ArchitectDetail(LoginRequiredMixin, DetailView):
    model = Architect

class ArchitectUpdate(LoginRequiredMixin, UpdateView):
    model = Architect
    fields = ['bio']

class ArchitectDelete(LoginRequiredMixin, DeleteView):
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
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def place_index(request):
    # 'places' is the variable name (place) in places/index.html
    places = Place.objects.filter(user=request.user)
    return render(request, 'places/index.html', {'places': places})

@login_required
def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    architects = Architect.objects.exclude(id__in=place.architects.all().values_list('id'))
    hours_form = HoursForm()
    return render(request, 'places/detail.html', {'place': place, 'hours_form': hours_form, 'architects': architects})

@login_required
def add_hours(request, place_id):
    form = HoursForm(request.POST)
    if form.is_valid():
        hour = form.save(commit=False)
        hour.place_id = place_id
        hour.save()
    return redirect('place-detail', place_id=place_id)

@login_required
def associate_architect(request, place_id, architect_id):
    Place.objects.get(id=place_id).architects.add(architect_id)
    return redirect('place-detail', place_id=place_id)

@login_required
def remove_architect(request, place_id, architect_id):
    Place.objects.get(id=place_id).architects.remove(architect_id)
    return redirect('place-detail', place_id=place_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('place-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
