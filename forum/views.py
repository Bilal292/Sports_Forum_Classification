from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,  DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from .classifier import predict_category
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    #this is executed before the form is saved 
    def form_valid(self, form): 
        self.object = form.save(commit=False) #stops the form from being saved in database
        text = self.object.body  #we store whatever user type in 
        category = self.object.category #get category to check if it says auto or not
      
        if (category == 'AutoCategorise'):#to check if user has already classified the post or not
            predict = predict_category([text]) #gives text to the classifer to predict
            self.object.category = predict  #changes the category to the predicted label

        return super().form_valid(form)     #saves the post


class MyPostView(ListView):
    model = Post
    template_name = 'my_posts.html'
    ordering = ['-date_posted']
  
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my_posts')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form) 
    success_url = reverse_lazy('home')

class CricketView(ListView):
    model = Post
    template_name = 'cricket.html'
    ordering = ['-id']

class BaseballView(ListView):
    model = Post
    template_name = 'baseball.html'
    ordering = ['-id']

class BasketballView(ListView):
    model = Post
    template_name = 'basketball.html'
    ordering = ['-id']

class FootballView(ListView):
    model = Post
    template_name = 'football.html'
    ordering = ['-id']

class HockeyView(ListView):
    model = Post
    template_name = 'hockey.html'
    ordering = ['-id']

class RugbyView(ListView):
    model = Post
    template_name = 'rugby.html'
    ordering = ['-id']

class TabletennisView(ListView):
    model = Post
    template_name = 'tabletennis.html'
    ordering = ['-id']

class TennisView(ListView):
    model = Post
    template_name = 'tennis.html'
    ordering = ['-id']

class VolleyballView(ListView):
    model = Post
    template_name = 'volleyball.html'
    ordering = ['-id']

class BadmintonView(ListView):
    model = Post
    template_name = 'badminton.html'
    ordering = ['-id']