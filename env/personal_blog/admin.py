from django.contrib import admin
from .models import track_of_mind, book
from .data_struc_models import data_structure_1
from .data_analytic_models import data_analytic_1

# Register your models here.


admin.site.register(track_of_mind)

admin.site.register(book)




# ---------------- register for data related items-------------------

admin.site.register(data_structure_1)

admin.site.register(data_analytic_1)