from hr.models import HR
from rest_framework import serializers

class HRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HR
        fields = "__all__"

