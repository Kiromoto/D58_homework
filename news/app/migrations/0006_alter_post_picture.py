# Generated by Django 4.2.3 on 2023-07-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_subscriber_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, default='uploads/default.jpg', upload_to='uploads/', verbose_name='Загрузить картинку для новости'),
        ),
    ]
