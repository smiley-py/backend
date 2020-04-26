# Generated by Django 2.1.15 on 2020-04-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
                ('is_deleted', models.CharField(default='0', max_length=1)),
            ],
        ),
    ]
