# Generated by Django 4.2.1 on 2024-08-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgallery', '0002_artitems_category_shop_delete_artitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_logo',
            field=models.ImageField(default='static\\download (8).jpeg', upload_to='logo'),
        ),
    ]