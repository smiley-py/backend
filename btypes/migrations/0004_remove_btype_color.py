# Generated by Django 2.2.10 on 2020-04-05 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btypes', '0003_auto_20200405_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btype',
            name='color',
        ),
    ]