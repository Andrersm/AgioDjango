# Generated by Django 5.0 on 2023-12-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_remove_contact_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loan',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]