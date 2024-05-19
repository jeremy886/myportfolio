# Generated by Django 5.0.6 on 2024-05-15 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_portfolio_comment_portfolio_item'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('category', models.CharField(choices=[('Nature', 'Nature'), ('Events', 'Events'), ('Portraits', 'Portraits'), ('Landscapes', 'Landscapes')], max_length=100, verbose_name='Category')),
                ('tags', models.CharField(max_length=100, verbose_name='Tags')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('public_visible', models.BooleanField(default=True, verbose_name='Publicly Visible')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('photo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='portfolio.photoitem')),
            ],
        ),
    ]
