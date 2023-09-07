# Generated by Django 4.2.5 on 2023-09-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.FloatField(help_text='in minutes')),
                ('ingredients', models.CharField(max_length=350)),
                ('description', models.TextField()),
                ('pic', models.ImageField(default='no_image.svg', upload_to='recipes')),
            ],
        ),
    ]
