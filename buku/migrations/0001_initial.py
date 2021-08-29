# Generated by Django 3.2.6 on 2021-08-29 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penerbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('alamat', models.CharField(max_length=50)),
                ('kota', models.CharField(max_length=60)),
                ('provinsi', models.CharField(max_length=30)),
                ('negara', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=30)),
                ('nama_belakang', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('tangga_publikasi', models.DateField()),
                ('penerbit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buku.penerbit')),
                ('penulis', models.ManyToManyField(to='buku.Penulis')),
            ],
        ),
    ]