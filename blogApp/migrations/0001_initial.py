# Generated by Django 3.1.4 on 2020-12-10 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='gategory')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('categories', models.ManyToManyField(related_name='posts', to='blogApp.Category', verbose_name='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='author')),
                ('body', models.TextField(verbose_name='comment body')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.post', verbose_name='post')),
            ],
        ),
    ]
