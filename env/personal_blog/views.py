from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from .forms import PostForm, EditForm
# ListView, DetailView takes query and return data
# ListView returns multiple data, DetailView return one block of data


# instead of retireving request, we use ListView



# Create your views here.

# request has the value passed from clients
# as specified in the seetings of main, the function will render pages from the templates
# can return some value {"name": "value to return"}

class home_view(ListView):
    model = Post
    template_name = 'home.html'

    # ordering = ['-id'] -- this will reverse order 
    # this will be used for recent update
    ordering = ['-date']

    # this will be updated for context processor
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(home_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def category_view(request, cats):

    category_posts = Post.objects.filter(category=cats.replace('-'," "))


    return render(request, 'categories.html', {'cats':cats.replace('-'," ").title() ,'category_posts':category_posts})

class article_view(DetailView):
    model = Post

    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(article_view, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class add_post_view(CreateView):

    model = Post
    
    # this specifies which fields we want
    form_class = PostForm
    template_name = 'add_post.html'

    #fields = '__all__'
    #fields = ('title','author','body')

class add_category_view(CreateView):

    model = Category
    
    template_name = 'add_category.html'

    fields = '__all__'
    #fields = ('title','author','body')

class update_post_view(UpdateView):

    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','body']

class delete_post_view(DeleteView):
    model = Post

    template_name = 'delete_post.html'

    # because deleteview doesnt redirect from the models, we have to specify it here
    success_url = reverse_lazy('home')