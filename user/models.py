from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )

    role_name = models.CharField(max_length=10, choices=ROLES, null=True)
    email = models.CharField(max_length=45, null=True, unique=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    position = models.CharField(max_length=45, null=True)
    funded_by = models.CharField(max_length=45, null=True)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    investment_report = models.ForeignKey('InvestmentReport', on_delete=models.CASCADE, null=True, related_name='custom_users')
    training = models.ForeignKey('Training', on_delete=models.CASCADE, null=True, related_name='custom_users')
    evaluation = models.ForeignKey('Evaluation', on_delete=models.CASCADE, null=True, related_name='custom_users')

    # def __str__(self):
    #     return self.first_name

    def is_admin(self):
        return self.role_name == 'admin'

    def is_employee(self):
        return self.role_name == 'employee'

    class Meta:
        db_table = 'custom_user'




class InvestmentReport(models.Model):
    investment_report_id = models.CharField(primary_key=True, max_length=45)
    employee_name = models.CharField(max_length=45)
    scale = models.CharField(max_length=45)
    point_on_scale = models.DecimalField(max_digits=10, decimal_places=0)
    funded_by = models.CharField(max_length=45)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0)
    weekly_hours = models.DecimalField(max_digits=10, decimal_places=0)
    gross_weekly = models.DecimalField(max_digits=10, decimal_places=0)
    full_day_rate = models.DecimalField(max_digits=10, decimal_places=0)
    half_day_rate = models.DecimalField(max_digits=10, decimal_places=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=0)
    # Removed Admin ref
    evaluation = models.ForeignKey('Evaluation', on_delete=models.CASCADE, related_name='investment_reports')
    employee = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='investment_reports')
    training = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='investment_reports')

    
    class Meta:
        db_table = 'investment_report'


class Evaluation(models.Model):
    evaluation_id = models.CharField(primary_key=True, max_length=45)
    employee_name = models.CharField(max_length=45)
    job_title = models.CharField(max_length=45)
    training_course = models.TextField()
    training_provider = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    certification = models.IntegerField()
    certification_reason = models.TextField()
    objective = models.TextField()
    topics = models.TextField()
    usefulness = models.TextField()
    three_important_points = models.TextField()
    topic_relevant = models.IntegerField()
    encouragement = models.IntegerField()
    material_helpfulness = models.IntegerField()
    objective_met = models.IntegerField()
    time_sufficient = models.IntegerField()
    expectation_met = models.IntegerField()
    # Removed Admin ref
    investment_report = models.ForeignKey('InvestmentReport', on_delete=models.CASCADE, related_name='evaluations')
    employee = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='evaluations')
    training = models.ForeignKey('Training', on_delete=models.CASCADE, related_name='evaluations')

    class Meta:
        db_table = 'evaluation'


class Training(models.Model):
    training_id = models.CharField(primary_key=True, max_length=45)
    employee_name = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    length_of_service = models.CharField(max_length=45)
    application_date = models.DateField()
    training_name = models.CharField(max_length=45)
    training_provider = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    training_hours = models.IntegerField()
    application_status = models.IntegerField()
    current_status = models.IntegerField()
    delivery_method = models.IntegerField()
    aims_and_objective = models.TextField()
    expected_outcome = models.TextField()
    total_cost = models.IntegerField()
    bjc_contribution = models.TextField()
    employee_contribution = models.TextField()
    employee_qualification = models.TextField()
    # Removed Admin ref
    evaluation = models.ForeignKey('Evaluation', on_delete=models.CASCADE, related_name='trainings')
    investment_report = models.ForeignKey('InvestmentReport', on_delete=models.CASCADE, related_name='trainings')
    employee = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='trainings')
    
    class Meta:
        db_table = 'training'