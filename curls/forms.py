from crispy_forms.helper import FormHelper
from django import forms

from curl_admin.models import Appointment, Employee, Services
from users.models import MyUser



class UserAppointmentForm(forms.ModelForm):
    
    # def __init__(self,user, *args, **kwargs):
    #     super(UserAppointmentForm, self).__init__(*args, **kwargs)
    #     self.fields['services'].label = "Services"
    #     self.fields['app_date'].label = "Appointment Date"
    #     self.fields['staff'].label = "Staff"
    #     self.fields['ucustomer'].label = "UCustomer"
        
        
    def __init__(self,*args, **kwargs):
        # First pop your kwargs that may bother the parent __init__ method
        print(kwargs.keys())
        self.user_id = kwargs.pop('user_id')
        self.ucustomer = kwargs.pop('ucustomer')
        print(self.ucustomer)
        # Then, let the ModelForm initialize:
        super(UserAppointmentForm, self).__init__(*args,**kwargs)
        # Finally, access the fields dict that was created by the super().__init__ call
        self.fields['ucustomer'].queryset = MyUser.objects.filter(id=self.ucustomer)
        self.fields['services'].queryset = Services.objects.filter(user_id=self.user_id)
        self.fields['staff'].queryset = Employee.objects.filter(user_id=self.user_id)
        self.fields['user'].queryset = MyUser.objects.filter(id=self.user_id)
        
        
    class Meta:
        
        model = Appointment
        fields = '__all__'
        exclude = ('customer',)
        
        widgets = {
            'services' :  forms.SelectMultiple(attrs={'class':'list-unstyled'}),
            'app_date' : forms.DateTimeInput(attrs={'type':'datetime-local','placeholder':'Date & Time','class':'form-control'}),
            'staff' :  forms.SelectMultiple(attrs={'class':'list-unstyled'}),
        }
        
