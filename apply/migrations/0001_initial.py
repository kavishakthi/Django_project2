# Generated by Django 3.2.19 on 2023-06-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dbform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(default=None)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]
