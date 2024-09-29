from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre='LabTest',
            ciudad='Quito',
            pais='Ecuador'
        )

    def test_laboratorio_nombre_ciudad_pais(self):
        # Obtener el laboratorio creado en setUpTestData
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        
        # Verificar los datos
        self.assertEqual(laboratorio.nombre, 'LabTest')
        self.assertEqual(laboratorio.ciudad, 'Quito')
        self.assertEqual(laboratorio.pais, 'Ecuador')

class LaboratorioURLTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre='LabTest',
            ciudad='Quito',
            pais='Ecuador'
        )

    def test_laboratorio_list_url(self):
        # Verificar que la URL devuelve HTTP 200
        response = self.client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)

class LaboratorioTemplateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre='LabTest',
            ciudad='Quito',
            pais='Ecuador'
        )

    def test_laboratorio_list_view_uses_correct_template(self):
        # Usar reverse para obtener la URL por nombre
        response = self.client.get(reverse('laboratorio_list'))
        
        # Verificar que la respuesta sea HTTP 200
        self.assertEqual(response.status_code, 200)
        
        # Verificar que se esté utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')
        
        # Verificar que el contenido HTML contiene el nombre del laboratorio creado
        self.assertContains(response, 'LabTest')
