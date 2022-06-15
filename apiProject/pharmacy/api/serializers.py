from rest_framework import serializers
from pharmacy.models import Line, Station, Pharmacylocation, Hospital, Pharmacy, Convenience

# 모든 필드
class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ['name']

# 역 이름
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['name']

# 동 이름
class DongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['dong']

# 모든 필드
class PharmacylocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacylocation
        fields = ['loadaddress', 'hospitalcount', 'doctorcount', 'pharmacycount',  'dong', 'hospitalperpharmacy', 'doctorperpharmacy','index', 'viewcount', 'conveniencecount', 'convenienceperpharmacy']

# index 제외 모든 필드
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['loadaddress', 'name', 'type', 'address', 'startdate', 'totaldoctor']

# index 제외 모든 필드
class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['loadaddress', 'name', 'address', 'startdate']

# index 제외 모든 필드
class ConvenienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenience
        fields = ['loadaddress', 'name', 'address', 'startdate']