# Generated by Django 2.1.5 on 2019-06-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fr_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuresitems',
            name='title',
            field=models.CharField(default='Titulo', max_length=60),
            preserve_default=False,
        ),
    ]