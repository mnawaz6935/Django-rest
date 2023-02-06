# Generated by Django 4.1.6 on 2023-02-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('education', models.TextField()),
                ('city', models.TextField()),
                ('contact', models.TextField()),
                ('ppsc_attempts', models.TextField()),
                ('gender', models.TextField()),
                ('purpose', models.TextField()),
                ('category', models.TextField()),
                ('device_id', models.TextField()),
                ('device_name', models.TextField()),
                ('signup_date', models.DateTimeField(auto_now=True)),
                ('membership_start_date', models.DateTimeField(auto_now=True)),
                ('membership_end_date', models.DateTimeField(auto_now=True)),
                ('device_login_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
