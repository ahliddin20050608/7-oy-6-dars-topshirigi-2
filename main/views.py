from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Employee, Project
from .serializers import CompanySerializer, EmployeeSerializer, ProjectSerializer


@api_view()
def company_all_view(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_company_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(company)
    return Response(serializer.data)


@api_view(['POST'])
def create_company_view(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_company_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(company, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(["PATCH"])
def update_patch_company_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(company, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(["DELETE"])
def delete_company_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return Response({"message":"Company deleted!"})


class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class EmployeeDELETEUPDATEDETAILView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)
    
    def get(self, request, pk):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self, request, pk):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        employee = self.get_object(pk=pk)
        employee.delete()
        return Response({"message":"Employee deleted!"})
            


class ProjectAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        ser = ProjectSerializer(projects, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = ProjectSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
class ProjectDELETEUPDATEDETAILView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)
    
    def get(self, request, pk):
        projects = self.get_object(pk=pk)
        ser = ProjectSerializer(projects)
        return Response(ser.data)
    
    def put(self, request, pk):
        project = self.get_object(pk=pk)
        ser = ProjectSerializer(project, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    def patch(self, request, pk):
        project = self.get_object(pk=pk)
        ser = ProjectSerializer(project, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def delete(self,request, pk):
        project = self.get_object(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        