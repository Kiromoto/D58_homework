# Generated by Django 4.2.3 on 2023-07-23 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.FileField(blank=True, default='uploads/ava_default.png', upload_to='uploads/', verbose_name='Загрузить аватарку'),
        ),
    ]
