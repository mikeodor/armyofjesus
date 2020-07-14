from django.urls import path
from . import views
# app_name ='app_name'
urlpatterns=[
    path("",views.index ,name='home'),
    path("sermon/", views.sermonlist.as_view(), name='sermon'),
    path("Ministry/",views.Ministry ,name='department'),
    path("video/", views.bloghome.as_view(), name='video'),
    path('<int:year>/<int:month>/',views.bloghome.as_view(month_format='%m'), name="archive_month_numeric"),
    path("detail/<int:pk>/", views.detailpost.as_view(), name='detail'),
    path('contact/',views.contact, name='contact'),
    path("videodetail/<int:pk>/", views.videodetail.as_view(), name='detailvideo'),
    path("donation/", views.donationpage, name='donation'),
    path('payment/',views.payment, name='payment'),
    path("prayerpoints/", views.prayerpoint.as_view(), name='prayers'),
    path("prayerdetail/<int:pk>/", views.test.as_view(), name='detailprayer'),
]