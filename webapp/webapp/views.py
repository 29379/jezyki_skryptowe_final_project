import json, os

from django.views.generic import UpdateView, ListView
from matplotlib.pyplot import title
from .models import Data
from django.http import Http404
from pathlib import Path
from django.shortcuts import render


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
imdb_file = os.path.join(PROJECT_DIR, 'webscraping/imdb.json')
filmweb_file = os.path.join(PROJECT_DIR, 'webscraping/filmweb.json')


def movie_create_view(request):
    try:
        f = open(filmweb_file)
        contents = json.load(f)
        for elem in contents:
            elem['release_year'] = elem['release_year'].strip('()')
            elem['title'] = elem['title'].rstrip()
            Data.objects.create(**elem)
    except FileNotFoundError:
        pass
    except IOError:
        pass

    try:
        f = open(imdb_file)
        contents = json.load(f)
        for elem in contents:
            elem['release_year'] = elem['release_year'].strip('()')
            Data.objects.create(**elem)
    except FileNotFoundError:
        pass
    except IOError:
        pass

    for row in Data.objects.all():
            if Data.objects.filter(title=row.title).count() > 1:
                row.delete()
        
    return render(request, "data_create.html")



class MovieListView(ListView):
    model = Data
    template_name = 'data_list.html'
    context_object_name = 'movies'
    database_size = Data.objects.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search_area') or ''
        if search_input != '':
            context['movies'] = context['movies'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input
        context['count'] = self.get_queryset().count()
        return context


def movie_detail_view(request, pk):
    movie = Data.objects.get(pk=pk)
    if movie is not None:
        return render(request, 'data_detail.html', {'movie': movie})
    else:
        return Http404("Image not found")


def movie_delete_view(request):
    Data.objects.all().delete()
    return render(request, "data_delete.html")


def scrape_imdb_view(request):
    os.system(f'python /home/Kuba//Desktop/tmp/jezyki_skryptowe_final_project/imdb_scraping_script.py')
    return render(request, "scraping_done_site.html")


def scrape_filmweb_view(request):
    os.system(f'python /home/Kuba//Desktop/tmp/jezyki_skryptowe_final_project/filmweb_scraping_script.py')
    return render(request, "scraping_done_site.html")


movie_list_view = MovieListView.as_view()