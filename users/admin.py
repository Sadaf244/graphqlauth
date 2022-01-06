from django.contrib import admin
from .models import SchoolUser
from django.apps import apps

admin.site.register(SchoolUser)
admin.site.register(Subscription)
app=apps.get_app_config('graphql_auth')
for model_name,model in app.models.items():
    admin.site.register(model)
