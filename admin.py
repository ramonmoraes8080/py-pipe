from django.contrib import admin
from pipe.models import (
    Document,
    )


class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Document, DocumentAdmin)
