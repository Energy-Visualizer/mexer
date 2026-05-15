from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.db.models.deletion import CASCADE


class EvizUser(DjangoUser):
    """Model representing a database table named 'EvizUser'."""

    institution_type = models.CharField(
        max_length=10,
        default="Other",
        choices={
            "Academic": "Academic",
            "Government": "Government",
            "Industry": "Industry",
            "Non-Profit": "Non-Profit",
            "Other": "Other",
        },
    )
    institution_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class EmailAuthCode(models.Model):
    """Model for storing email auhtentication codes and associated account information."""

    code = models.TextField(max_length=255, primary_key=True)
    account = models.ForeignKey(to=EvizUser, on_delete=CASCADE)


class PassResetCode(models.Model):
    """Model for storing password reset codes and the associated user."""

    code = models.TextField(max_length=255, primary_key=True)
    user = models.ForeignKey(EvizUser, on_delete=models.CASCADE)
