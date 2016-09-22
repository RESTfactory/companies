from rest_framework import serializers
from .models import App, OrganizationalUnitType, OrganizationalUnit

class OrganizationalUnitTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationalUnitType

class OrganizationalUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationalUnit

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
