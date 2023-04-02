from django.urls import path
from . import views

urlpatterns=[
     path('',views.test,name="home"),
     path('messagepage/<int:pk>',views.messagepage,name="messagepage"),
     path('placecreate',views.placecreate,name="placecreate"),
     path('cr',views.cr,name="cr"),
     path('deletepage/<int:pk>',views.deletepage,name="deletepage"),
      path('userlogin',views.user_login,name="userlogin"),
      path('userregister',views.user_register,name="userregister"),
      path('userlogout',views.user_logout,name="userlogout"),
]