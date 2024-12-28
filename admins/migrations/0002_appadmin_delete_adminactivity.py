# Generated by Django 5.1.4 on 2024-12-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=100)),
                ('app_link', models.CharField(max_length=100)),
                ('app_category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=1)),
                ('app_icon', models.ImageField(upload_to='document')),
            ],
        ),
        migrations.DeleteModel(
            name='AdminActivity',
        ),
    ]
