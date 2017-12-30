
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^home/$',views.index, name="home"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^$',auth_views.login,kwargs = {'template_name':'login_app/home.html', "redirect_authenticated_user":True},name="login"),
    url(r'^slot_viewer/$',views.slot_viewer,name='slot_viewer'),
    url(r'^logout/$',auth_views.logout,{'template_name':'login_app/logout.html',},name="logout")
]