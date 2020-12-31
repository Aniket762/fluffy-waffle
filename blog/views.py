from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
#list view gives the youTube wala feel

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostViewList(ListView):
    model = Post
    template_name = 'blog/home.html'
    # by default it expects <app>/<model>_<viewtype>.html
    # template passing is basically the page it needs to show when func called
    context_object_name = 'posts' # object to loop over
    ordering = ['-date_posted'] 
    #ordering the post on basis of time, bringing the latest post top


# taki har ek post k lia ek page ban jai, url mei khelna hai 
class PostDetailView(DetailView):
    model = Post
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
