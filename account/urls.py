from django.contrib.auth import get_user
from django.urls import path
from account.views import *
from django.contrib.auth.decorators import login_required


app_name = 'account'
urlpatterns = [

    # path('', login_required(AccountHomeView.as_view()), name="account"),
    # path('security/', login_required(AccountSecurityView.as_view()) , name="account-security"),
    # path('settings/', login_required(AccountSettingsView.as_view()) , name="account-settings"),

]