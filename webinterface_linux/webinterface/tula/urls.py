from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'tula'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('edit/<file_name>', views.editview, name='edit'),
    path('edit_rejected/<file_name>', views.editview_rejected, name='edit_rejected'),
    path('switch/<file_name>', views.switch, name='switch'),
    path('switch_rejected/<file_name>', views.switch_rejected, name='switch_rejected'),
    path('train/', views.TrainView, name='train'),
    path('real_time_view/', views.RealTimeView, name='real_time_view'),
    path('real_time_view/topframe', views.TopFrameView, name='topframe'),
    path('real_time_view/bottomframe', views.BottomFrameView, name='bottomframe'),
    path('accepted_list/', views.accepted_list, name='accepted_list'),
    path('rejected_list/', views.rejected_list, name='rejected_list'),
    path('list_choice/', views.list_choice, name='list_choice'),
    path('real_time_view/recent', views.recent, name='recent'),
]