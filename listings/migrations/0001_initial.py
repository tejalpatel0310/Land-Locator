<<<<<<< HEAD
# Generated by Django 3.2.3 on 2021-06-13 17:13

import datetime
from django.db import migrations, models
=======
# Generated by Django 3.2.3 on 2021-06-04 13:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        ('landowners', '0001_initial'),
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='LandownerListingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('sale_type', models.CharField(choices=[('for Rent', 'For Rent'), ('for Lease', 'For Lease')], default='for Rent', max_length=50)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['complete'],
            },
        ),
        migrations.CreateModel(
=======
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
<<<<<<< HEAD
                ('sale_type', models.CharField(choices=[('for Rent', 'For Rent'), ('for Lease', 'For Lease')], default='for Rent', max_length=50)),
                ('contact_number', models.CharField(default='', max_length=15)),
=======
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
<<<<<<< HEAD
=======
                ('landowner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='landowners.landowners')),
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
            ],
        ),
    ]
