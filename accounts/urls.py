from django.conf.urls import url, include
from . import url_reset
from .views import index, register, profile, logout, login

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    ]