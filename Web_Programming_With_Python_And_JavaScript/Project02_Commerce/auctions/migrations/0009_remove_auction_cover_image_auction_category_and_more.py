# Generated by Django 5.0.1 on 2024-01-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auction_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Fashion', 'FASHION'), ('None', 'NONE'), ('Toys', 'TOYS'), ('Electronics', 'ELECTRONICS'), ('Home', 'HOME')], default='None', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]