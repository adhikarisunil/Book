# Generated by Django 4.0 on 2023-08-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_poem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='poet_name',
            new_name='author',
        ),
        migrations.AddField(
            model_name='nobel',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]