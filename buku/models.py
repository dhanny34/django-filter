from django.db import models


class Penerbit(models.Model):
    nama = models.CharField(max_length=30)
    alamat = models.CharField(max_length=50)
    kota = models.CharField(max_length=60)
    provinsi = models.CharField(max_length=30)
    negara = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.nama


class Penulis(models.Model):
    nama_depan = models.CharField(max_length=30)
    nama_belakang = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.nama_depan, self.nama_belakang)


class Buku(models.Model):
    judul = models.CharField(max_length=100)
    penulis = models.ManyToManyField(Penulis)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
    tangga_publikasi = models.DateField()

    def __str__(self):
        return self.judul
