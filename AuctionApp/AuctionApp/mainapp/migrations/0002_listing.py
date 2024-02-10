# Generated by Django 4.1.3 on 2022-11-30 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('image_url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('open', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
