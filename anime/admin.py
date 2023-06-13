from django.contrib import admin

# Register your models here.

from anime.models import animecards
# Register your models here.

class animeadmin(admin.ModelAdmin):
    list_display=("a_photo","a_title","a_descript","a_link")
admin.site.register(animecards,animeadmin)