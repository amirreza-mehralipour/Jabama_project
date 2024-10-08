# Generated by Django 5.1 on 2024-09-10 13:02

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1, message='rating must be between 1-5'), django.core.validators.MaxValueValidator(5, message='rating must be between 1-5')])),
                ('comment', models.TextField()),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales_app.sales')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
