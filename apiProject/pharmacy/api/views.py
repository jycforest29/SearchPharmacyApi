from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from pharmacy.models import Line, Station, Pharmacylocation, Hospital, Pharmacy, Convenience
from .serializers import LineSerializer, StationSerializer, DongSerializer, HospitalSerializer, PharmacylocationSerializer, PharmacySerializer, ConvenienceSerializer
from rest_framework import status
from rest_framework.response import Response

# 지하철 호선 정보 보냄
class LineListApiView(APIView):
    def get(self, request):
        datas = Line.objects.all()
        serializer = LineSerializer(datas, many = True)
        return Response(serializer.data)

# 선택한 호선의 역 정보 보냄
class SelectedLineStationListApiView(APIView):
    def get(self, request, line):
        datas = Station.objects.filter(line = line).order_by('name').values('name').distinct()
        serializer = StationSerializer(datas, many = True)
        return Response(serializer.data)

# 역 객체의 역명이 속하는 동 정보 보냄
class StationToDongApiView(APIView):    
    def get(self, request, name):
        datas = Station.objects.filter(name = name).order_by('dong').values('dong').distinct()
        serializer = DongSerializer(datas, many = True)
        return Response(serializer.data)
    
# SearchFragment에서 특정 동으로 검색한 결과 보냄
class PharmacylocationListApiView(APIView):

    def get(self, request, dong):
        datas = Pharmacylocation.objects.filter(dong = dong).order_by('-hospitalperpharmacy')
        serializer = PharmacylocationSerializer(datas, many = True)
        return Response(serializer.data)

# DetailFragment에 PharmacyLocation에 대한 정보 보냄
class PharmacylocationDetailApiView(APIView):

    def get_object(self, index):
        # index as pk
        data = get_object_or_404(Pharmacylocation, index = index)
        return data

    def get(self, request, index):
        data = self.get_object(index)
        data.viewcount += 1
        data.save()
        serializer = PharmacylocationSerializer(data, many = False)

        return Response(serializer.data)

# DetailFragment에서 Hospital에 대한 정보 보냄
class HospitalListApiView(APIView):

    def get(self, request, index):
        pharmacylocation = get_object_or_404(Pharmacylocation, index = index)
        datas = Hospital.objects.filter(loadaddress = pharmacylocation.loadaddress)
        serializer = HospitalSerializer(datas, many = True)

        return Response(serializer.data)

# DetailFragment에 Pharmacy에 대한 정보 보냄
class PharmacyListApiView(APIView):

    def get(self, request, index):
        pharmacylocation = get_object_or_404(Pharmacylocation, index = index)
        datas = Pharmacy.objects.filter(loadaddress = pharmacylocation.loadaddress)
        serializer = PharmacySerializer(datas, many = True)

        return Response(serializer.data)

# DetailFragment에 Pharmacy에 대한 정보 보냄
class ConvenienceListApiView(APIView):

    def get(self, request, index):
        pharmacylocation = get_object_or_404(Pharmacylocation, index = index)
        datas = Convenience.objects.filter(loadaddress = pharmacylocation.loadaddress)
        serializer = ConvenienceSerializer(datas, many = True)
        return Response(serializer.data)

# MainFragment에 인기 입지 5개 보냄
class TopViewPLAPIView(APIView):

    def get(self, request):
        # 최소 조회수 5개 이상
        datas = Pharmacylocation.objects.filter(viewcount__gte = 5).order_by('-viewcount')[:5]
        serializer = PharmacylocationSerializer(datas, many = True)
        return Response(serializer.data)