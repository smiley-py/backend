# Generated by Django 2.2.10 on 2020-04-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_auto_20200404_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='state',
            name='title',
        ),
        migrations.AddField(
            model_name='state',
            name='color',
            field=models.CharField(default='#000000', max_length=10),
        ),
        migrations.AddField(
            model_name='state',
            name='is_deleted',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]