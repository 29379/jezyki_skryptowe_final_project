import json, sys, os

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import Data
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from pathlib import Path
from django.shortcuts import render
from django.db.models import F


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
imdb_file = os.path.join(PROJECT_DIR, 'webscraping/imdb.json')


class MovieCreateView(CreateView):
    model = Data
    template_name = 'data_create.html'
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')
    context_object_name = 'movie'
    with open(imdb_file) as f:
        contents = json.load(f)
        for elem in contents:
            elem['release_year'] = elem['release_year'].strip('()')
            Data.objects.create(**elem)


class MovieListView(ListView):
    model = Data
    template_name = 'data_list.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search_area') or ''
        if search_input != '':
            context['movies'] = context['movies'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input
        return context


"""class MovieDetailView(DetailView):
    model = Data
    template_name = 'data_detail.html'
    context_object_name = 'movie'"""
def movie_detail_view(request, pk):
    movie = Data.objects.get(pk=pk)
    if movie is not None:
        return render(request, 'data_detail.html', {'movie': movie})
    else:
        return Http404("Image not found")


class MovieUpdateView(UpdateView):
    model = Data
    template_name = 'data_update.html'
    fields = ['title', 'release_year', 'directors_and_actors',
              'user_rating', 'poster']
    success_url = reverse_lazy('movies')
    context_object_name = 'movie'


class MovieDeleteView(DeleteView):
    model = Data
    template_name = 'data_delete.html'
    context_object_name = 'movies'
    success_url = reverse_lazy('movies')


def test(request):
    return HttpResponse('It works!')


movie_list_view = MovieListView.as_view()
#   movie_detail_view = MovieDetailView.as_view()
movie_create_view = MovieCreateView.as_view()
movie_update_view = MovieUpdateView.as_view()
movie_delete_view = MovieDeleteView.as_view()
