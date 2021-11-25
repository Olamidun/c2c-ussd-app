from django.urls import path
from . import views
app_name = 'loan_demo'

urlpatterns = [
    path('ussd', views.ussd_user),
    # path('get_customer', views.GetUssdUserAPIView.as_view())
]