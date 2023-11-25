from rest_framework import serializers
from app.models import *
class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=True, max_length=20)
    age = serializers.IntegerField()
    email = serializers.EmailField(required=False)
    address = serializers.CharField(max_length=250)
    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class EmployeeSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeSerializerHyperModel(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(many=True, view_name='employee-detail', lookup_field='id',read_only=True,format='html')
    class Meta:
        model = Employee
        fields = ['url','id','name','age','email','address']
        # fields = "__all__"

