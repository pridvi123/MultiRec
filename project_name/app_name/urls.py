from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),
    path('save_page1/', views.save_page1, name='save_page1'),
    path('page2/<int:name_id>/', views.page2, name='page2'),
    path('save_page2/<int:name_id>/', views.save_page2, name='save_page2'),
    path('page3/<int:name_id>/', views.page3, name='page3'),
]