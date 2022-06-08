from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Data
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import F


class MovieListView(ListView):
    model = Data


class MovieDetailView(DetailView):
    model = Data


class MovieCreateView(CreateView):
    model = Data
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')


class MovieUpdateView(UpdateView):
    model = Data
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')


class MovieDeleteView(DeleteView):
    model = Data
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')


def test(request):
    return HttpResponse('It works!')


movie_list_view = MovieListView.as_view()
movie_detail_view = MovieDetailView.as_view()
movie_create_view = MovieCreateView.as_view()
movie_update_view = MovieUpdateView.as_view()
movie_delete_view = MovieDeleteView.as_view()
