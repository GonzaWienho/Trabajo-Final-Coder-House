from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from Hamgurga.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def index(request):
    return render(request, "Hamgurga/index.html")

class PostList(ListView):
    model = Post
    context_object_name = "post_list.html"

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy("Post-List")
    fields = '__all__'

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("Post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "Hamgurga/not_found.html")


class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("Post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Hamgurga/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("Post-List")

class Login(LoginView):
    next_page = reverse_lazy("Post-List")

class Logout(LogoutView):
    template_name = 'registration/logout.html'
