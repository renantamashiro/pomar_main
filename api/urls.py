from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('api/specie/', views.SpecieList.as_view(), name='specie-list'),
    path('api/specie/<int:pk>/', views.SpecieDetail.as_view(), name='specie-detail'),
    path('api/tree/', views.TreeList.as_view(), name='tree-list'),
    path('api/tree/new/', views.TreeNew.as_view(), name='tree-new'),
    path('api/tree/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
    path('api/tree-group/', views.TreeGroupList.as_view(), name='tree-group-list'),
    path('api/tree-group/new/', views.TreeGroupNew.as_view(), name='tree-group-new'),
    path('api/tree-group/<int:pk>/', views.TreeGroupDetail.as_view(), name='tree-group-detail'),
    path('api/harvest/', views.HarvestList.as_view(), name='harvest-list'),
    path('api/harvest/new/', views.HarvestNew.as_view(), name='harvest-new'),
    path('api/harvest/<int:pk>/', views.HarvestDetail.as_view(), name='harvest-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)