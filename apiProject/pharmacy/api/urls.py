from django.urls import path
from .views import LineListApiView, SelectedLineStationListApiView, StationToDongApiView
from .views import HospitalListApiView, PharmacyListApiView
from .views import TopViewPLAPIView, PharmacylocationListApiView, PharmacylocationDetailApiView, ConvenienceListApiView

urlpatterns = [
    # 지하철
    path('getLines/', LineListApiView.as_view(), name = 'get-lines'),
    path('getStationsByLine/<str:line>/', SelectedLineStationListApiView.as_view(), name = 'get-line-stations'),
    path('getDongBySearch/<str:name>/', StationToDongApiView.as_view(), name = 'get-search-dong'),
    path('getDongBySelect/<str:name>/', StationToDongApiView.as_view(), name = 'get-select-dong'),

    # 약국 입지 검색 및 디테일페이지
    path('search/<str:dong>/', PharmacylocationListApiView.as_view(), name = 'search-dong'),
    
    path('detail/<int:index>/', PharmacylocationDetailApiView.as_view(), name = 'detail-pharmacyLocation'),
    path('detail/<int:index>/hospital/', HospitalListApiView.as_view(), name = 'detail-hospital'),
    path('detail/<int:index>/pharmacy/', PharmacyListApiView.as_view(), name = 'detail-pharmacy'),
    path('detail/<int:index>/convenience/', ConvenienceListApiView.as_view(), name = 'detail-convenience'),

    # 인기 약국 입지
    path('getTop5/', TopViewPLAPIView.as_view(), name = 'top5'),
] 