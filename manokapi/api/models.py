from django.db import models
from rest_framework.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class Order(models.Model):
    PENDING = 'PENDING'
    PROCESSED = 'PROCESSED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSED, 'Processed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.status == self.PENDING:
            pending_orders = Order.objects.filter(user=self.user, status=self.PENDING)
            if self.pk is None and pending_orders.exists():
                raise ValidationError("A user can only have one pending order at a time.")
            elif self.pk is not None and pending_orders.exclude(pk=self.pk).exists():
                raise ValidationError("A user can only have one pending order at a time.")
        super().clean()

    def __str__(self):
        return f"Order {self.id} - {self.status} - {self.user.username}"