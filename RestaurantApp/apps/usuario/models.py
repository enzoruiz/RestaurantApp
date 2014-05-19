from django.db import models

# Create your models here.
class Persona(models.Model):
	cDni = models.CharField(primary_key=True, max_length=8)
	cNombre = models.CharField(max_length=45)
	cApellidoPaterno = models.CharField(max_length=45)
	cApellidoMaterno = models.CharField(max_length=45)
	cSexo = models.CharField(max_length=1)
	dFechaNacimiento = models.DateField()
	cDireccion = models.CharField(max_length=140)
	cTelefono = models.CharField(max_length=25)
	cDepartamento = models.CharField(max_length=25)
	cProvincia = models.CharField(max_length=25)
	cDistrito = models.CharField(max_length=25)
	cEmail = models.EmailField()

	def __str__(self):
		return self.cDni + ' - ' + self.cNombre + ' ' + self.cApellidoMaterno + ' ' + self.cApellidoMaterno

class Cliente(models.Model):
	persona = models.OneToOneField(Persona)
	cTipoPersona = models.CharField(max_length=45)
	cRuc = models.CharField(max_length=25)
	dFechaCreacion = models.DateTimeField(auto_now_add=True)
	dFechaModificacion = models.DateTimeField(auto_now=True)
	cUsuarioModificacion = models.CharField(max_length=45)
	cEstado = models.CharField(max_length=45)

	def __str__(self):
		return self.persona.cDni + ' - ' + self.persona.cNombre + ' ' + self.persona.cApellidoMaterno + ' ' + self.persona.cApellidoMaterno

# class Empleado(models.Model):
# 	persona = models.ForeignKey(Persona)
# 	sucursal