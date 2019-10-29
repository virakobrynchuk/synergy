from django.urls import path
from .views import (users_list,
                    users_detail,
                    users_create,
                    users_update,
                    users_delete,
                    groups_list,
                    groups_detail,
                    groups_create,
                    groups_update,
                    groups_delete,
                    index,
                    )

urlpatterns = [
    path('', index, name='index'),
    path('users/', users_list, name='users_list'),
    path('users/new/', users_create, name='users_create'),
    path('users/<pk>/update/', users_update, name='users_update'),
    path('users/<pk>/delete/', users_delete, name='users_delete'),
    path('users/<pk>/', users_detail, name='users_detail'),
    path('groups/', groups_list, name='groups_list'),
    path('groups/new/', groups_create, name='groups_create'),
    path('groups/<pk>/update/', groups_update, name='groups_update'),
    path('groups/<pk>/delete/', groups_delete, name='groups_delete'),
    path('groups/<pk>/', groups_detail, name='groups_detail'),
]