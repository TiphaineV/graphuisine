# Generated by Django 5.0 on 2024-01-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_tag_alter_recipe_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tag_list',
            field=models.ManyToManyField(to='recipes.tag'),
        ),
    ]