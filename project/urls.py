
from account.views import login_view, logout_view, register_view
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rapport.urls')),

    path('login/', login_view , name="login"),
    path('logout/', logout_view , name="logout"),
    path('account/register/', register_view , name="register"),

]
