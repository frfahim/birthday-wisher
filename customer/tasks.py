from celery import shared_task
from celery.utils.log import get_task_logger
from django.core import mail
from django.conf import settings
from django.utils import timezone

from .models import Customer

logger = get_task_logger(__name__)


@shared_task
def send_birthday_wish():
    """
    This task run everyday at 12.01 AM
    - check which customer has birthday today and send a birthday wish to them
    """
    customers = Customer.objects.filter(
        birthdate=timezone.localdate()
    )
    emails = list()
    for customer in customers:
        message = f"Hi {customer.name}, Wishing you the biggest slice of happy today."
        email_message = mail.EmailMessage(
            subject=f"Happy birthday, {customer.name}",
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[customer.email],
        )
        emails.append(email_message)

    # this will create single connection to send all emails at once
    with mail.get_connection() as connection:
        connection.send_messages(emails)

    logger.info(f"Wishes happy birthday to {customers.count()}")
