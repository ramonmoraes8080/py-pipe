import os
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    FileField,
    )
from pipe.models import Document


class DocumentSerializer(Serializer):
    name = CharField(read_only=True)
    extension = CharField(read_only=True)
    path = CharField()
    content = FileField()

    def save(self):
        path = self.validated_data["path"]
        content = self.validated_data["content"]
        name = os.path.basename(path)
        path = os.path.dirname(path)
        extension = name.split(".")[1]
        model = Document(
            name=name,
            path=path,
            extension=extension,
            content=content,
            )
        model.save()
