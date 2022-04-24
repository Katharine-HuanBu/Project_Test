# Generated by Django 3.1.2 on 2022-04-13 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='house_images')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house', verbose_name='House')),
            ],
            options={
                'verbose_name': 'house_images',
                'verbose_name_plural': 'house_images',
                'ordering': ('-create_at',),
            },
        ),
    ]