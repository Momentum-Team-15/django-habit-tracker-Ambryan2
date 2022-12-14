"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from habit import views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/logout/',views.logout, name='logout' ),
    path('accounts/login/',views.login,name='login'),
    path('', views.index, name='home'),
    path('habit/new', views.habit_new, name='habit_new'),
    path('habit/<int:pk>',views.habit_detail, name='habit_detail'),
    path('habit/<int:habitpk>/<str:yearpk>/<int:monthpk>/<int:daypk>',views.day_record, name='day_record'),
    path('habit/<int:habitpk>/<str:datepk>', views.edit_records, name="edit_records"),
    path('record/new_record/<int:habitpk>',views.new_record,name='new_record'),
    path('record/delete/<int:recordpk>', views.record_delete, name='record_delete'),
    path('habit/delete/<int:habitpk>', views.habit_delete, name='habit_delete'),
    path('habit/new/<int:habitpk>', views.habit_edit, name="habit_edit"),
    path('api/habits/', api_views.HabitListView)
]
