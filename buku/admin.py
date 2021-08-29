from django.contrib import admin
from .models import Buku, Penerbit, Penulis

# Register your models here.
admin.site.register(Buku)
admin.site.register(Penulis)
admin.site.register(Penerbit)