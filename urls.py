from django.urls import path
from pipe.views import (
    DocumentCreateView,
    DocumentSearchView,
    )


urlpatterns = [
    path('upload', DocumentCreateView.as_view(), name='document-create'),
    path('search', DocumentSearchView.as_view(), name='document-search'),
    ]
