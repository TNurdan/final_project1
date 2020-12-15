from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('player/<int:pk>', 
    	 views.PlayerDetailView.as_view(), name='player_detail'),
]
urlpatterns += [   
    path('clubs/', views.ClubListView.as_view(), name='clubs'),
    path('club/<int:pk>',
         views.ClubDetailView, name='club-detail'),
]