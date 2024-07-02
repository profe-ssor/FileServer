import django_filters # type: ignore
from .models import WeddingCards, EngagementCards, BirthdayCards, AdmissionForms

class WeddingCardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = WeddingCards
        fields = ['title', 'description']


class EngagementCardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = EngagementCards
        fields = ['title', 'description']


class BirthdayCardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = BirthdayCards
        fields = ['title', 'description']


class AdmissionCardFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = AdmissionForms
        fields = ['title', 'description']
