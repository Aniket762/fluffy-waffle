from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView , CreateView
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

# only create when logged in , and till then redirects to login page

class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields= ['title','content']
    #fields that you want to change

    # setting the author of the post as the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin , UpdateView):
    model = Post
    fields= ['title','content']
    #fields that you want to change

    # setting the author of the post as the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
