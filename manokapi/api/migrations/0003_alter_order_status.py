# Generated by Django 4.2.16 on 2024-11-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSED', 'Processed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10),
        ),
    ]