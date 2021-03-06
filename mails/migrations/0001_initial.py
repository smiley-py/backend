# Generated by Django 2.1.15 on 2020-05-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('smtp', models.CharField(max_length=250)),
                ('port', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('tolist', models.CharField(blank=True, max_length=250, null=True)),
                ('cclist', models.CharField(blank=True, max_length=250, null=True)),
                ('bcclist', models.CharField(blank=True, max_length=250, null=True)),
                ('is_deleted', models.CharField(default='0', max_length=1)),
            ],
        ),
    ]
