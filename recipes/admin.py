from django.contrib import admin

from .models import Recipe
from .models import Tag

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Tag)
