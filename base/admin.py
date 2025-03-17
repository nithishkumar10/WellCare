from django.contrib import admin
from . models import User_Model, Contact_Us, PredictionResult
# Register your models here.
admin.site.register(User_Model)
admin.site.register(Contact_Us)
admin.site.register(PredictionResult)