# Generated by Django 4.1 on 2022-09-12 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'To do'), (1, 'In progress'), (2, 'Done')], default=0)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name', 'slug')},
            },
        ),
    ]
