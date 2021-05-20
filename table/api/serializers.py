from rest_framework import serializers

from ..models import SimpleTable


class SimpleTableListSerializers(serializers.ModelSerializer):

    class Meta:
        model = SimpleTable
        fields = ['name', 'quantity', 'distance', 'time_stamp']
