from django.db import models
from django.utils.text import slugify



class GenderChoice(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"


class ProfessionChoice(models.TextChoices):
    DEVELOPER = "developer", "Developer"
    DESIGNER = "designer", "Designer"
    MANAGER = "manager", "Manager"
    TESTER = "tester", "Tester"
    DEVOPS = "devops", "DevOps"
    

class Company(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    phone = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Company.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        return super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=50 ,choices=GenderChoice.choices, default=GenderChoice.MALE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    profession = models.CharField(max_length=100 ,choices=ProfessionChoice.choices, default=ProfessionChoice.DEVELOPER)
    
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="projects")
    end_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name