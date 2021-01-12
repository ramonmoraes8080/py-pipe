from uuid import uuid4
from django.db import models
from django.conf import settings


def upload_to_document(instance, filename):
    return f"{settings.PIPE_UPLOAD_TO}/{str(instance.pk or uuid4())}"


class Node(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Document(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    content = models.FileField(upload_to=upload_to_document)
