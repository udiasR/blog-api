from decimal import Decimal

from django.db.models import (
    CharField,
    BooleanField,
    ForeignKey,
    DecimalField,
    UniqueConstraint,
    TextField,
    ManyToManyField,
    EmailField,
    PROTECT,
)

from apps.abstracts.models import AbstractBaseModel

# Create your models here.
class User(AbstractBaseModel):
    """User database table."""

    NAME_MAX_LEN = 50

    email = EmailField()
    first_name = CharField(
        max_length=NAME_MAX_LEN,
    )
    last_name = CharField(
        max_length=NAME_MAX_LEN,
    )
    is_active = BooleanField(
        default=True,
    )
    is_staff = BooleanField(
        default=False,
    )




