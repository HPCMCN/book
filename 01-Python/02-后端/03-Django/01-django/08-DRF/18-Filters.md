```python
# filters.py
from django_filters import FilterSet, filters

from . import models


class UserFilterSet(FilterSet):
    depart = filters.CharFilter(label="depart", method="filter_depart")
    depart__in = filters.CharFilter(label="depart", method="filter_depart__in")

    org = filters.CharFilter(label="org", method="filter_org")
    org__in = filters.CharFilter(label="org", method="filter_org__in")

    depart_name = filters.CharFilter(label="depart_name", method="filter_depart_name")
    depart_name__icontains = filters.CharFilter(label="depart_name", method="filter_depart_name__icontains")
    
    role = filters.CharFilter(field_name="user_roles__roles__code")

    role_id = filters.CharFilter(field_name="user_roles__roles__id")
    role_id__in = filters.BaseInFilter(field_name="user_roles__roles__id", lookup_expr="in")


    class Meta:
        model = models.Users
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "in", "icontains"],
            "username": ["exact", "in", "icontains"],
            "last_login": ["isnull"],
        }
       
    @property
    def qs(self):
        qs = super().qs
        return qs

    def filter_depart(self, qs, name, value):
        return qs.filter(depart__depart_id=value)

    def filter_depart__in(self, qs, name, value):
        return qs.filter(depart__depart_id__in=value.split(","))

    def filter_org(self, qs, name, value):
        return qs.filter(depart__depart__organization_id=value)

    def filter_org__in(self, qs, name, value):
        return qs.filter(depart__depart__organization_id__in=value.split(","))

    def filter_depart_name(self, qs, name, value):
        return qs.filter(depart__depart__organization__name=value)

    def filter_depart_name__icontains(self, qs, name, value):
        return qs.filter(depart__depart__organization__name__icontains=value)

    
# views.py
class UsersViewSet(viewsets.ModelViewSet):

    pagination_class = pagination.PageNumberPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsOwner,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = filters.UserFilterSet
    search_fields = ("name", "username")
    queryset = models.Users.objects.all()
    
# urls.py
from django.urls import include, path, re_path

urlpatterns = []
routes = DefaultRouter()
routes.register("users", viewset=views.UsersViewSet, basename="users")
urlpatterns += routes.urls
```

