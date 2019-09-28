# Generated by Django 2.2.4 on 2019-09-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projecttech',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]