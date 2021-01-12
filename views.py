import re
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    )
from django_filters import rest_framework as filters
from pipe.serializers import DocumentSerializer
from pipe.models import (
    Document,
    )


class DocumentFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    path = filters.CharFilter(field_name="path", lookup_expr="icontains")
    ext = filters.CharFilter(field_name="extension", lookup_expr="exact")

    class Meta:
        model = Document
        fields = [
            "name",
            ]


class DocumentCreateView(CreateAPIView):
    serializer_class = DocumentSerializer


class DocumentSearchView(ListAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DocumentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        content_expr = self.request.GET.get('content_expr')
        ret = []
        if content_expr:
            for model in queryset:
                # TODO how to handle actual binary data?
                with open(model.content.path, "rb") as f:
                    file_content = f.read().decode("utf-8")
                    if re.search(content_expr, file_content):
                        print(f"Bingo for {model.pk}")
                        ret.append(model.pk)
        if ret:
            return queryset.filter(pk__in=ret)
        return queryset
