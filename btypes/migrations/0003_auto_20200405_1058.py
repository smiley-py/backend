# Generated by Django 2.2.10 on 2020-04-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btypes', '0002_auto_20200404_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btype',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='btype',
            name='title',
        ),
        migrations.AddField(
            model_name='btype',
            name='color',
            field=models.CharField(default='#000000', max_length=10),
        ),
        migrations.AddField(
            model_name='btype',
            name='is_deleted',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='btype',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]