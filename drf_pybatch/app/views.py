from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Employee
from app.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


@api_view(['GET', 'POST'])
def employee_list_post(request):
    """
    List all code employee, or create a new employee.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def employee_detail(request,id):
    """
    List all code employee, or create a new employee.
    """
    try:
        empl_ob = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = EmployeeSerializer(empl_ob)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(empl_ob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        empl_ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeList(APIView):
    def get(self,request,format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EmployeeSerializerModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        serializer = EmployeeSerializer(self.get_object(id))
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id,format=None):
        serializer = EmployeeSerializerModel(self.get_object(id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        emp_object = self.get_object(id)
        emp_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeListHyper(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerHyperModel

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeDetailHyper(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializerModel

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EmployeeListLc(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer