from django.contrib import admin
from django.urls import path
from diary.views import home, RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView, \
    search

app_name = 'diary'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', home, name='home'),
    path('record/new/', RecordCreateView.as_view(), name='record_create'),
    path('record/list/', RecordListView.as_view(), name='record_list'),
    path('record/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('record/<int:pk>/update', RecordUpdateView.as_view(), name='record_update'),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),

    path('record/search/', search, name='search'),
    ]
