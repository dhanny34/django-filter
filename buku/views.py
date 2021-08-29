from django.shortcuts import render
from .models import Buku


def CariView(request):
    qs = Buku.objects.all()

    judul = request.GET.get('judul')
    tahun = request.GET.get('tahun')

    # filter disini
    if judul != '' and judul is not None:
        qs = qs.filter(judul__icontains=judul)

    if tahun != '' and tahun is not None:
        qs = qs.filter(tangga_publikasi__icontains=tahun)

    context = {
        'queryset': qs
    }

    return render(request, "cari.html", context)