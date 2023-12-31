# Generated by Django 5.0 on 2023-12-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='actual_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='actual_installments',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
