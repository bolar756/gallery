# Generated by Django 4.2.1 on 2024-08-22 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appgallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtItems',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='art_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('facebook_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('whatsapp_link', models.URLField()),
                ('shop_bio', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ArtItem',
        ),
        migrations.AddField(
            model_name='artitems',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appgallery.category'),
        ),
        migrations.AddField(
            model_name='artitems',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appgallery.shop'),
        ),
    ]
