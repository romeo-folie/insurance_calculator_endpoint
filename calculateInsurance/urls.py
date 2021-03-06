from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from calculateInsurance import views

app_name = 'calculateInsurance'
urlpatterns= [
    url(r'^cars/$', views.CarList.as_view(), name='car-list'),
    # url(r'^cars/$', views.car_list, name='car-list'),
    url(r'^cars/(?P<pk>\w+)/$', views.CarDetail.as_view(), name='car-detail'),
    # url(r'^cars/(?P<pk>[0-9]+)/$', views.car_detail, name='car-detail')
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\w+)/$', views.UserDetail.as_view()),
    url(r'^cars/(?P<pk>\w+)/highlight/$', views.CarHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
