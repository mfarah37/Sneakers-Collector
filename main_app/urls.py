from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_resale/', views.add_resale, name='add_resale'),
    path('sneakers/<int:sneaker_id>/assoc_condition/<int:condition_id>', views.assoc_condition, name='assoc_condition'),
    path('sneakers/<int:sneaker_id>/unassoc_condition/<int:condition_id>', views.unassoc_condition, name='unassoc_condition'),
    path('conditions/', views.ConditionList.as_view(), name='conditions_index'),
    path('conditions/<int:pk>/', views.ConditionDetail.as_view(), name='conditions_detail'),
    path('conditions/create/', views.ConditionCreate.as_view(), name='conditions_create'),
    path('conditions/<int:pk>/update/', views.ConditionUpdate.as_view(), name='conditions_update'),
    path('conditions/<int:pk>/delete/', views.ConditionDelete.as_view(), name='conditions_delete'),
    path('sneakers/<int:sneaker_id>/add_photo/', views.add_photo, name='add_photo'),
] 
