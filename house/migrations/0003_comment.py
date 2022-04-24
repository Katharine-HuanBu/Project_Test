# Generated by Django 3.1.2 on 2022-04-13 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0002_houseimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('label', models.CharField(choices=[('Postitive', 'Positive'), ('Negative', 'Negative')], default='Positive', max_length=32, verbose_name='sentiment label')),
                ('score', models.FloatField(default=1, verbose_name='sentiment score')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'house_comments',
                'verbose_name_plural': 'house_comments',
                'ordering': ('-create_at',),
            },
        ),
    ]
