from django import forms
from .models import Laboratorio

from .models import Producto, DirectorGeneral

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']

class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre', 'laboratorio', 'especialidad']