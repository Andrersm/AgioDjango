# Generated by Django 5.0 on 2023-12-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_parcelas_installment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
