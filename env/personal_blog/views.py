# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import track_of_mind, book, data_structure, data_analytic

# Create your views here.

def index(request):
# request has the value passed from clients
# as specified in the seetings of main, the function will render pages from the templates
# can return some value {"name": "value to return"}
    
    #collect_books = book.objects.all()
    #collect_minds = track_of_mind.objects.all()
    #collect_strucs = data_structure.objects.all()
    #collect_analytics = data_analytic.objects.all()
#
    #total_list = [collect_books, collect_minds, collect_strucs, collect_analytics]
#
    #all_items = {"books": collect_books, "track_of_minds": collect_minds, "data_structures": collect_strucs, "data_analytics": collect_analytics, "total_list": total_list}


    return render(request, 'home.html')

def select_track_of_mind(request):
    
    #title = request.GET.get("title_name")
#
    #collect_books = book.objects.all()
    #collect_minds = track_of_mind.objects.all()
    #collect_strucs = data_structure.objects.all()
    #collect_analytics = data_analytic.objects.all()
#
    #selected_item = track_of_mind.objects.get(title=title)
#
    #all_items = {"books": collect_books, "track_of_minds": collect_minds, "data_structures": collect_strucs, "data_analytics": collect_analytics, "item": selected_item}
    
    return render(request, 'home.html')

def select_book(request):

    #title = request.GET.get("title_name")
#
    #collect_books = book.objects.all()
    #collect_minds = track_of_mind.objects.all()
    #collect_strucs = data_structure.objects.all()
    #collect_analytics = data_analytic.objects.all()
#
    #selected_item = book.objects.get(title=title)
#
    #all_items = {"books": collect_books, "track_of_minds": collect_minds, "data_structures": collect_strucs, "data_analytics": collect_analytics, "item": selected_item}
    
    return render(request, 'home.html')



def select_data_structure(request):
   
    #title = request.GET.get("title_name")
#
    #collect_books = book.objects.all()
    #collect_minds = track_of_mind.objects.all()
    #collect_strucs = data_structure.objects.all()
    #collect_analytics = data_analytic.objects.all()
#
    #selected_item = data_structure.objects.get(title=title)
#
    #all_items = {"books": collect_books, "track_of_minds": collect_minds, "data_structures": collect_strucs, "data_analytics": collect_analytics, "item": selected_item}
    
    return render(request, 'home.html')

def select_data_analytic(request):
    
    #title = request.GET.get("title_name")
#
    #collect_books = book.objects.all()
    #collect_minds = track_of_mind.objects.all()
    #collect_strucs = data_structure.objects.all()
    #collect_analytics = data_analytic.objects.all()
#
    #selected_item = data_analytic.objects.get(title=title)
#
    #all_items = {"books": collect_books, "track_of_minds": collect_minds, "data_structures": collect_strucs, "data_analytics": collect_analytics, "item": selected_item}
    
    return render(request, 'home.html')