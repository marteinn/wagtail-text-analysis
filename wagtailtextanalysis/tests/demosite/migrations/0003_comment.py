# Generated by Django 2.1.8 on 2019-04-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosite', '0002_auto_20190418_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('sentiment', models.DecimalField(decimal_places=6, max_digits=7)),
            ],
        ),
    ]