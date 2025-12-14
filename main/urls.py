from django.urls import path
from .views import (
    company_all_view, detail_company_view, create_company_view,
    update_company_view, update_patch_company_view, delete_company_view,
    
    EmployeeAPIView, EmployeeDELETEUPDATEDETAILView,ProjectAPIView, ProjectDELETEUPDATEDETAILView
    )

urlpatterns = [
    path("companies", company_all_view, name="all-companies"),
    path("company/<int:pk>/", detail_company_view, name="detail-company"),
    path("company/create/", create_company_view, name="create-company"),
    path("company/update/<int:pk>/", update_company_view, name="update-company"),
    path("company/patch/update//<int:pk>/", update_patch_company_view, name="update-patch-company"),
    path("company/delete/<int:pk>/", delete_company_view, name="delete-company"),
    
    path("employees/", EmployeeAPIView.as_view(), name="all-employees"),
    path("employee/<int:pk>/", EmployeeDELETEUPDATEDETAILView.as_view(), name="employee-changes"),
    
    path("projects/", ProjectAPIView.as_view(), name="all-projects"),
    path("project/<int:pk>/", ProjectDELETEUPDATEDETAILView.as_view(), name="project-changes"),
    
]