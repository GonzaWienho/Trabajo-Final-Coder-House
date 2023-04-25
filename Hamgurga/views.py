from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView,
from Hamgurga.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "Hamgurga/index.html")

class PostList(ListView):
    model = Post
    context_object_name = "post_list.html"

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy("Post-List")
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("Post-list")
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("Post-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('Post-list')

