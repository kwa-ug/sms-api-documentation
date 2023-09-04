import requests
from django.contrib import admin

from sms.models import Sms, SmsSettings


# Register your models here.
class smsBaseModelAdmin(admin.ModelAdmin):
    model = Sms
    def get_search_fields(self, request):
        model = self.model
        excluded_field_names = ['id', 'updated_date', 'created_date']
        search_fields = []

        for field in model._meta.fields:
            if (
                not field.is_relation
                and field.name not in excluded_field_names
                and field.related_model is None
            ):
                search_fields.append(field.name)

        return search_fields

    def get_list_display(self, request):
        model = self.model
        list_display = [field.name for field in model._meta.fields if field.name not in ['id']]
        return list_display

class SmsAdmin(smsBaseModelAdmin):
    model = Sms

    def has_delete_permission(self, request, obj=None):
        return False

    def get_list_display(self, request):
        model = self.model
        list_display = [field.name for field in model._meta.fields if field.name not in ['id']]
        if request.user.is_superuser:
            list_display.remove("response")
        return list_display

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        # Construct the data for the API request
        smsSettings = SmsSettings.objects.all().first()
        data = {
            "username": smsSettings.username,
            "primary_sms_api_key": smsSettings.primary_sms_api_key,
            "phone_number": obj.phone_number,  # Replace with the appropriate field in your Sms model
            "message": obj.message,  # Replace with the appropriate field in your Sms model
        }

        # Send the HTTP POST request to the API
        response = requests.post("https://sms.kwaug.net/api/postmessage/", json=data)

        # Check if the request was successful (you can customize this check based on the API response)
        feedback = response.json()
        if feedback.get('error'):
            obj.sent = False
        obj.response = str(feedback)
        super().save_model(request, obj, form, change)

admin.site.register(Sms, SmsAdmin)
class SmsSettingsAdmin(smsBaseModelAdmin):
    model = SmsSettings

    def has_add_permission(self, request):
        if SmsSettings.objects.all().count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(SmsSettings, SmsSettingsAdmin)