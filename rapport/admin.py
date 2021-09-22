from django.contrib import admin
from rapport.models import Rapport

# Register your models here.


class RapportAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']


admin.site.register(Rapport, RapportAdmin)