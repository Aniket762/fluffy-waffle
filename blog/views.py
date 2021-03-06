from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView , CreateView, DeleteView
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


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields= ['title','content']
    #fields that you want to change

    # setting the author of the post as the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # only wirter of the post can edit it
    # else 403 error
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# delete krne k lia post
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
