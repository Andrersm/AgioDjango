# Generated by Django 5.0 on 2023-12-22 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_category_contact_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
