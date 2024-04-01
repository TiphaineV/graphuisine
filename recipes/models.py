from django.db import models
from django.utils.text import slugify, get_valid_filename
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime
import subprocess

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    recipe_file = models.FileField(upload_to="source_files")
    tag_list = models.ManyToManyField("Tag")
    img = models.FileField(upload_to="static/assets/img/", blank=True)
    pub_date = models.DateTimeField("date published", default=datetime.now, blank=True) 

    def __str__(self):
        return str(self.title)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

# needs to be transformed into a post-save hook?
@receiver(pre_save, sender=Recipe)
def gen_svg(sender, instance, *args, **kwargs):
    print("Generating SVG file...")
    process = subprocess.Popen(["./node_modules/.bin/mmdc", "-i", f"./{instance.recipe_file}", "-o", f"./static/recipes/svg/{slugify(instance.title)}.svg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout, stderr)
    print(instance.title)
