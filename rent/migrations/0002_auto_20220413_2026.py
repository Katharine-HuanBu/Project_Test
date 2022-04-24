# Generated by Django 3.1.2 on 2022-04-13 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.rent'),
        ),
        migrations.AddField(
            model_name='rent',
            name='rent_type',
            field=models.CharField(choices=[('First Rent', 'Frst Rent'), ('Delay', 'Delay')], default='First Rent', max_length=32, verbose_name='Rent Type'),
        ),
        migrations.CreateModel(
            name='Unsubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('status', models.CharField(choices=[('wait to approve', 'wait to approve'), ('approve', 'approve')], max_length=32, verbose_name='Status')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('is_from_delay', models.BooleanField(default=False, verbose_name='Is From Delay')),
                ('rent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rent.rent', verbose_name='Rent Info')),
            ],
            options={
                'verbose_name': 'Subscribe',
                'verbose_name_plural': 'Subscribe',
                'ordering': ('-create_at',),
            },
        ),
    ]
