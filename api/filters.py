from api.models import Survey
import django_filters


class SurveyFilter(django_filters.FilterSet):

    keyword = django_filters.CharFilter(method="filter_keyword")

    def filter_keyword(self, queryset, name, value):
        queryset = queryset.filter(name__icontains=value)
        return queryset

    class Meta:
        model = Survey
        fields = ['id', 'keyword']
