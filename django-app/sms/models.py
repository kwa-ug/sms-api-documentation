from django.core.exceptions import ValidationError
from django.db import models
import re

# Create your models here.
def format_phone_number(phone_number):
    # Remove all non-digit characters
    number = re.sub(r'\D', '', phone_number)

    # Check if the number starts with a valid Uganda country code
    if number.startswith('0'):
        # Replace the leading '0' with the Uganda country code '+256'
        number = number[1:]

    if number.startswith("256"):
        number = number[3:]

    number = "256" + number

    # get_network(number)

    # Validate the character count
    if len(number) != 12:
        raise ValidationError("Invalid phone number")

    # Return the formatted phone number
    return number

class Sms(models.Model):
    class Meta:
        verbose_name = "SMS"
        verbose_name_plural = "SMS"
    phone_number = models.CharField(max_length=20, validators=[format_phone_number,])
    message = models.TextField()
    sent = models.BooleanField(default=True, editable=False)
    response = models.TextField(null=True, blank=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.pk, self.phone_number)

    def __unicode__(self):
        return "%s %s" % (self.pk, self.phone_number)
    
    def save(self):
        if not self.pk:
            self.phone_number = format_phone_number(self.phone_number)
        super().save()

class SmsSettings(models.Model):
    class Meta:
        verbose_name = "SMS Configuration"
        verbose_name_plural = "SMS Configurations"

    username = models.CharField(max_length=40, help_text="Username from bulky sms sender")
    primary_sms_api_key = models.CharField(max_length=40, help_text="Primary SMS Key from bulky sms sender")
    secondary_sms_api_key = models.CharField(max_length=40, help_text="Secondary SMS Key from bulky sms sender")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.pk, self.username)

    def __unicode__(self):
        return "%s %s" % (self.pk, self.username)