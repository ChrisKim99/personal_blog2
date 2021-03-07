from .models import Category


def category_renderer(request):
    return {
       'all_subjects': Category.objects.all(),
    }