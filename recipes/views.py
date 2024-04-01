from django.shortcuts import render
from django.views import generic
from re import findall

from .models import Recipe

class IndexView(generic.ListView):
    template_name = "recipes/index.html"
    context_object_name = "recipe_list"

    def get_queryset(self):
        return Recipe.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_ingredients(self, file):
        contents = file.read().decode()
        ingredients = findall(r'\{\{[\S\n\t\v ]+?\}\}', contents)
        utensils = findall(r'\(\[[\S\n\t\v ]+?\]\)', contents)

        return [ x.strip("{{").strip("}}").strip("\"") for x in ingredients ], set([ x.strip("([").strip("])").strip("\"") for x in utensils ])


    def get_context_data(self, **kwargs):
        context = super(generic.DetailView, self).get_context_data()
        fname = self.object.recipe_file
        context['ingredients'], context['utensils'] = self.get_ingredients(fname)

        context['test'] = 2

        return context
