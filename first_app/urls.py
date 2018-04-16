from django.urls import path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'formPage',views.form_name_view, name='form_name'),
]

