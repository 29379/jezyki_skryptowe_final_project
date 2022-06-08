from django.views.generic.detail import DetailView
from .models import Data
from django.db.models import F


class MovieDetailView(DetailView):
    model = Data
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        pass
