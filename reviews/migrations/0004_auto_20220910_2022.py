# Generated by Django 2.2.5 on 2022-09-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_cleanliness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(null=True),
        ),
    ]
