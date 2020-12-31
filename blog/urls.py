from django.urls import path
from .views import PostViewList, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostViewList.as_view(), name='blog-home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    #pk is primary key , url defining likewise
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/', views.about, name='blog-about'),
]
