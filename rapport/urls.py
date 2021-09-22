from rapport.excel import ToExcelFileView
from django.urls import path

from rapport.views import (
    RapportDeleteView,
    RapportDetailView,
    RapportFilterView,
    RapportListView,
    # RapportDetailView,
    RapportCreateView,
    RapportUpdateView,
    UserRapportListView,
    # RapportUpdateView,
    # RapportDeleteView,
)

app_name = 'rapport'
urlpatterns = [
    path('', RapportListView.as_view(), name='rapport-list'),
    path('user/rapports/<int:pk>', UserRapportListView.as_view(), name='user-rapports'),
    path('user/rapport/<int:pk>/', RapportListView.as_view(), name='rapport-list'),
    path('rapport/<int:pk>/', RapportDetailView.as_view(), name='rapport-detail'),
    path('rapport/create/', RapportCreateView.as_view(), name='rapport-create'),
    path('rapport/<int:pk>/update/', RapportUpdateView.as_view(), name='rapport-update'),
    path('rapport/<int:pk>/delete/', RapportDeleteView.as_view(), name='rapport-delete'),


    path('rapport/excel/', ToExcelFileView.as_view(), name='rapport-excel'),
    path('rapport/filter/', RapportFilterView.as_view(), name='rapport-filter'),
]
