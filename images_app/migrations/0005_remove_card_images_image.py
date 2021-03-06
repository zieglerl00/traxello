# Generated by Django 4.0.3 on 2022-06-24 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0004_card_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images_app.card')),
            ],
        ),
    ]
