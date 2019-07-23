"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views
from bank import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.redirect_root),
    path('fetchbank/',views.FetchBank.as_view(),name='fetchbank'),
    path('fetchifsc/',views.FetchIfsc.as_view(),name='fetchifsc'),
    path('fetchifsc/<path:querypath>/',views.FetchIfscView.as_view(),name='fetchifsc'),
    path('fetchbank/<path:querypath>/',views.FetchBankView.as_view(),name='fetchbank'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
