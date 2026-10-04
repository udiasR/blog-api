from decimal import Decimal
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models import (
    CharField,
    BooleanField,
    ForeignKey,
    DecimalField,
    UniqueConstraint,
    TextField,
    ManyToManyField,
    SlugField,
    PROTECT,
)

from apps.abstracts.models import AbstractBaseModel

# Create your models here.
class Category(AbstractBaseModel):
    """Category database table."""

    NAME_MAX_LEN = 100

    name = CharField(
        max_length=NAME_MAX_LEN,
    )
    slug = SlugField(unique=True)


class Tag(AbstractBaseModel):
    """Tag database table."""

    NAME_MAX_LEN = 50

    name = CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )
    slug = SlugField(unique=True)



class Post(AbstractBaseModel):
    """Post database table."""

    NAME_MAX_LEN = 200


    author = ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = CharField(
        max_length=NAME_MAX_LEN,
    )
    slug = SlugField(
        unique=True
    )
    body = TextField()
    category = ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = ManyToManyField(
        to = Tag,
        blank=True,
    )
    status = CharField()


class Comment(AbstractBaseModel):
    """Comment database table."""

    NAME_MAX_LEN = 50

    post = ForeignKey(
        to = Post,
        on_delete=models.CASCADE,
    )
    slug = SlugField(unique=True)
    author = ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = TextField()
    

