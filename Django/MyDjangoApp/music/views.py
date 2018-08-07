from django.views import generic
from .models import Album 
from django.views.generic.edit import CreateView , UpdateView , DeleteView


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    # slug_field = "detail"
