from django.urls import path
from . import views
app_name='taskapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:id>/',views.TaskDetailView.as_view(),name='cbvdetail')
]
