from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.http import HttpResponse
from.models import post

def home(request):
	context = {
	  'posts':post.objects.all()
	}
	return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-Date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['Title','Contents']

    def form_valid(self,form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['Title','Contents']

    def form_valid(self,form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True

            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = "/"


    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True

            return False


    

def about(request):
	return render(request,'blog/about.html',{'title':'About'})
