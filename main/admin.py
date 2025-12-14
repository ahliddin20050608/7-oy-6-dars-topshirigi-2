from django.contrib import admin
from .models import Company, Employee, Project

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'phone', 'slug')
    prepopulated_fields = {'slug': ('name',)}  


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'gender', 'company', 'profession')
    list_filter = ('gender', 'profession', 'company')
    search_fields = ('name', 'phone')



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee', 'end_date', 'is_active')
    list_filter = ('is_active', 'end_date')
    search_fields = ('name', )
