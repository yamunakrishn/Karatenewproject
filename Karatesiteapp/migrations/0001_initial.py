# Generated by Django 4.0.3 on 2022-07-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation_img', models.ImageField(null=True, upload_to='file')),
                ('affiliation_name', models.ImageField(null=True, upload_to='file')),
            ],
        ),
    ]