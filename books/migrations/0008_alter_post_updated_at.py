# Generated by Django 4.0 on 2023-08-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_post_author_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
