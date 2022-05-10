from django.db import models
from users.models import MyUser

GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    cust_gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    cust_email = models.EmailField(max_length = 254, unique=True, null=True)
    cust_contact = models.BigIntegerField(unique=True)
    user = models.ForeignKey(MyUser,default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cust_name

EMP_DEPT_CHOICES = [('Hair','Hair'),('Skin','Skin'),('Nails','Nails'),('Tattoo','Tattoo')]

class EmpDept(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=50,choices=EMP_DEPT_CHOICES)
    # user = models.ManyToManyField(MyUser,default=1, on_delete=models.CASCADE)
    user = models.ManyToManyField(MyUser)
    def __str__(self):
        return self.dept_name
    
    
class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    profile_pic = models.ImageField(null=True, blank=True,default = 'emp_profile_pics/employee.png',upload_to = 'emp_profile_pics')
    emp_name = models.CharField(max_length=50)
    emp_gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    emp_contact = models.BigIntegerField(unique=True, null=False)
    role = models.CharField(max_length=50)
    emp_dob = models.DateField(null=False)
    emp_doj = models.DateField(null=False)
    emp_salary = models.FloatField()
    dept = models.ForeignKey(EmpDept,null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser,default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.emp_name
    
GENDER_SERVICE_CHOICES = [('Male','Male'),('Female','Female'),('Child(below 12 years)','Child(below 12 years)'),('Others','Others')]

class Services(models.Model):
    serv_id = models.BigAutoField(primary_key=True)
    serv_name = models.CharField(max_length=150,null=False)
    serv_price = models.DecimalField(max_digits=6, decimal_places=2)
    gender = models.CharField(max_length=50,default='Male', choices=GENDER_SERVICE_CHOICES)
    serv_desc = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.serv_name
    
    
class Appointment(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    app_date = models.DateTimeField(null=False)
    customer = models.ForeignKey(Customer,null=True,related_name='customer',on_delete=models.CASCADE)
    ucustomer = models.ForeignKey(MyUser,null=True,related_name='ucustomer',on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)
    staff = models.ManyToManyField(Employee,related_name='employee')
    user = models.ForeignKey(MyUser,default=1,related_name='user', on_delete=models.CASCADE)
    
    def __str__(self):
        if self.customer:
            return f"{self.customer}'s Appointment"
        else:
            return f"{self.ucustomer}'s Appointment"
            
WEEKDAYS = [
  ("Monday", "Monday"),
  ("Tuesday", "Tuesday"),
  ("Wednesday", "Wednesday"),
  ("Thursday", "Thursday"),
  ("Friday", "Friday"),
  ("Saturday", "Saturday"),
  ("Sunday", "Sunday"),
]
  
class BusinessHours(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=20,choices=WEEKDAYS)
    open_time = models.TimeField()
    close_time = models.TimeField()
    
    def __str__(self):
        return f"{self.days} {self.open_time}-{self.close_time} "   

class Business(models.Model):
    b_id = models.AutoField(primary_key=True)
    profile_img = models.ImageField(default = 'business_profile_pics/salon.jpeg',upload_to = 'business_profile_pics')
    b_name = models.CharField(max_length=50)
    b_email = models.EmailField(max_length = 254, unique=True, null=True)
    b_contact = models.BigIntegerField(unique=True)
    b_address = models.TextField(null=True)
    services = models.ManyToManyField(Services)
    employee = models.ManyToManyField(Employee)
    b_hours = models.ManyToManyField(BusinessHours)
    user = models.ForeignKey(MyUser,default=1, on_delete=models.CASCADE)

