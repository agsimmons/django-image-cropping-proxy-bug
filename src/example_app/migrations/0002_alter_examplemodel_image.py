# Generated by Django 3.2.16 on 2022-12-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]