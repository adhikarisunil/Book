# Generated by Django 4.0 on 2023-08-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
