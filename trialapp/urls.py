"""trialapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('addregister',views.addregister),
    path('login',views.login),
    path('addlogin',views.addlogin),
    path('logout',views.logout),
    path('addfood',views.addfood),
    path('addfoods',views.addfoods),
    path('viewfood',views.viewfood),
    path('viewfoodc',views.viewfoodc),
    path('indexx',views.indexx,name="indexx"),
    path('paid',views.paid,name="paid"),
    path('paidorder/<int:id>',views.paidorder,name="paidorder"),
    path('paidorder/paided',views.paided,name="paided"),
    path('homeback',views.homeback,name="homeback"),

    path('totalorder',views.totalorder,name="totalorder"),
    path('vieworderr',views.vieworderr,name="vieworderr"),

    path('payment/<int:id>',views.payment, name='payment'),

    path('approved/<int:id>',views.approved, name='approved'),

    path('delete/<int:id>',views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
    path('update/updates/<int:id>',views.updates, name='updates'),
    path('profile',views.profile),
    path('orderfood',views.orderfood),
    path('orderss/addorder',views.addorder,name='addorder'), 
    path('orderss/<int:id>',views.orderss, name='orderss'),
    path('vieworder',views.vieworder),
    path('viewpayment',views.viewpayment),
    path('viewcart',views.viewcart,name='viewcart'),
    path('viewcustomerorder/id',views.viewcustomerorder,name="viewcustomerorder"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)