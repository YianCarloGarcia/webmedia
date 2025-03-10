from django import forms
from .models import estudiante, qrScan

class estudianteform(forms.ModelForm):
    class Meta:
        model = estudiante
        fields = '__all__'

class qrform(forms.ModelForm):
    class Meta:
        model = qrScan
        fields = '__all__'

