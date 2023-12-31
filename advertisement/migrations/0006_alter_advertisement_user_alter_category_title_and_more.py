# Generated by Django 4.2.4 on 2023-09-11 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0005_city_alter_advertisement_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='advertisements', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=48, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='advertisements', to='advertisement.city', verbose_name='city'),
        ),
    ]
