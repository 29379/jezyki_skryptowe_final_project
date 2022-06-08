from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Data
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import F


class MovieListView(ListView):
    model = Data
    template_name = 'data_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Data
    template_name = 'data_get.html'
    context_object_name = 'movies'


class MovieCreateView(CreateView):
    model = Data
    template_name = 'data_create.html'
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')
    context_object_name = 'movies'


class MovieUpdateView(UpdateView):
    model = Data
    template_name = 'data_update.html'
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')
    context_object_name = 'movies'


class MovieDeleteView(DeleteView):
    model = Data
    template_name = 'data_delete.html'
    context_object_name = 'movies'
    success_url = reverse_lazy('movies')


def test(request):
    return HttpResponse('It works!')


movie_list_view = MovieListView.as_view()
movie_detail_view = MovieDetailView.as_view()
movie_create_view = MovieCreateView.as_view()
movie_update_view = MovieUpdateView.as_view()
movie_delete_view = MovieDeleteView.as_view()
