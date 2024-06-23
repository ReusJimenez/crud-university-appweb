from django import forms
from app.models import Alumno
from datetime import date

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"

    codigo = forms.CharField(
        label="Código", widget=forms.TextInput(attrs={"class": "input"})
    )
    nombres = forms.CharField(
        label="Nombres", widget=forms.TextInput(attrs={"class": "input"})
    )
    apellidos = forms.CharField(
        label="Apellidos", widget=forms.TextInput(attrs={"class": "input"})
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento", widget=forms.DateInput(attrs={"class": "input", "type": "date"}),
    )
    edad = forms.IntegerField(
        widget=forms.HiddenInput(), required=False
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "input"})
    )
    telefono = forms.CharField(
        label="Teléfono", widget=forms.TextInput(attrs={"class": "input"})
    )
    estado_estudio = forms.BooleanField(
        label="Estado de Estudio (Activo o Inactivo)", required=False, widget=forms.CheckboxInput(attrs={"class": "checkbox"})
    )
    
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['codigo'].disabled = True
