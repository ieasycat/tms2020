# Generated by Django 3.1.7 on 2021-03-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('species', models.CharField(max_length=10)),
                ('data_crate', models.DateTimeField()),
                ('image_type', models.CharField(max_length=5)),
            ],
        ),
    ]
