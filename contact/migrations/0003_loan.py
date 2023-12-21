# Generated by Django 5.0 on 2023-12-20 14:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_picture_contact_show_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_amount', models.DecimalField(decimal_places=2, default='total_amount', max_digits=10)),
                ('loan_date', models.DateField(default=django.utils.timezone.now)),
                ('total_installments', models.IntegerField()),
                ('actual_installments', models.IntegerField(default='total-installmensts')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contact.contact')),
            ],
        ),
    ]
