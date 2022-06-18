from django.contrib import admin
from . import models


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(models.Data, MovieAdmin) 
