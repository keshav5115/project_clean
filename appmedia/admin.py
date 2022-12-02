from django.contrib import admin

from .models import Blog
# Register your models here.

class blogadmin(admin.ModelAdmin):
    list_display =['title','author','textarea','photo']


admin.site.register(Blog,blogadmin)
