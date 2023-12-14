# Generated by Django 4.2 on 2023-12-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], default='S', max_length=2),
        ),
    ]
