# Generated by Django 4.2.14 on 2024-08-05 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warcraft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='backgrounds/')),
            ],
        ),
    ]
