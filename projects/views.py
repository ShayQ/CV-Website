from .models import Post
from django.views import generic

# Create your views here.


class ProjectView(generic.DetailView):
    model = Post
    template_name = 'projectView.html'


class ProjectList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'projectList.html'


class ProfileView(generic.TemplateView):
    template_name = 'index.html'
