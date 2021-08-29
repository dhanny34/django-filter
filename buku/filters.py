import django_filters

from .models import Buku

class BukuFilter(django_filters.FilterSet):
	class Meta:
		model = Buku
