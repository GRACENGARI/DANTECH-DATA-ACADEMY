# Generated by Django 4.2.5 on 2024-12-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_organazations_icon_organazations_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='image', upload_to='pictures')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]