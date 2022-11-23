"""HighwayWebApp URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('highway/',views.highway,name='highway'),
    path('highway/insert',views.insert,name='inserthighway'),
    path('highway/sortHighways',views.sortHighways,name='sorthighway'),
    path('edithighway/<str:id>',views.editHighway,name='edithighway'),
    path('updatehighway/<str:id>', views.updateHighway,name='updatehighway'),
    path('deletehighway/<str:id>',views.deleteHighway,name='deletehighway'),
    path('tenders/',views.tenders,name='tenders'),
    path('tenders/sortTenders',views.sortTenders,name='sorttenders'),
    path('tenders/insertTenders',views.insertTenders,name='inserttenders'),
    path('edittender/<int:id>',views.editTender,name='edittender'),
    path('updateTender/<int:id>',views.updateTender,name='updatetender'),
    path('deletetender/<int:id>',views.deleteTender,name='deletetender'),
    path('query/',views.runquery,name='query1'),
    path('query2/',views.runquery2,name='query2'),
    path('query3/',views.runquery3,name='query3'),
    path('search/',views.search,name='search'),
    path('searchtender/',views.searchtender,name='search1')
]
