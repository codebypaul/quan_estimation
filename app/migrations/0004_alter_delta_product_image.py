# Generated by Django 5.2 on 2025-04-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_delta_description_alter_delta_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delta',
            name='product_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
