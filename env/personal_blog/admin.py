from django.contrib import admin
from .models import track_of_mind, book, data_analytic, data_structure, post

# Register your models here.


admin.site.register(track_of_mind)

admin.site.register(book)


admin.site.register(post)

# ---------------- register for data related items-------------------

admin.site.register(data_structure)

admin.site.register(data_analytic)