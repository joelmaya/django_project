from django.urls import path
from.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )
from.import views

urlpatterns = [
    path('', PostListView.as_view(), name ="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name ="post-detail"),
    path('post/<int:pk>/Update/', PostUpdateView.as_view(), name ="post-Update"),
    path('post/<int:pk>/Delete/', PostDeleteView.as_view(), name ="post-Delete"),
    path('post/new/', PostCreateView.as_view(), name ="post-Create"),
    path('about/',views.about,name = "blog-about"),
]