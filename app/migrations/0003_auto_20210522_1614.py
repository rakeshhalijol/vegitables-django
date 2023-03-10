# Generated by Django 2.2.14 on 2021-05-22 10:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 10, 44, 13, 625503, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quntity', models.IntegerField(default=1)),
                ('ordered_on', models.DateField(default=datetime.datetime(2021, 5, 22, 10, 44, 13, 625503, tzinfo=utc))),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Vegitable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
