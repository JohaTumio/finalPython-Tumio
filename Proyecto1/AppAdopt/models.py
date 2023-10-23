from django.db import models

class Animal(models.Model):
    ESPECIE_CHOICES = (
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
)
    SEXO_CHOICES=(
    ('Hembra', 'Hembra'),
    ('Macho', 'Macho'),
    )

    TAMANO_CHOICES = (
        ('Chico', 'Chico'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    )

    imagen = models.ImageField(upload_to="animal_images/", null=True, blank=True)
    nombre = models.CharField(max_length=40)
    sexo = models.CharField(max_length=20, choices=SEXO_CHOICES)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=40, choices=TAMANO_CHOICES)
    raza = models.CharField(max_length=40)
    caracteristicas = models.TextField(blank=True)
    cuidados_especiales = models.CharField(max_length=40, null=True, blank=True, verbose_name="Cuidados Especiales")
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES, blank=True)

    def __str__(self):
        return f"Nombre:{self.nombre} | Raza:{self.raza} | Especie:{self.especie}"
    
    def save(self, *args, **kwargs):
        # Capitalizar la primera letra del nombre antes de guardar
        self.nombre = self.nombre.capitalize()
        self.raza = self.raza.capitalize()
        super(Animal, self).save(*args, **kwargs)

class Profesional(models.Model):
    ESPECIALIDAD_CHOICES = (
    ('Veterinario General', 'Veterinario General'),
    ('Veterinario de Animales Exóticos', 'Veterinario de Animales Exóticos'),
    ('Emergencias y Cuidados Críticos', 'Emergencias y Cuidados Críticos'),
    ('Cirujano Veterinario', 'Cirujano Veterinario'),
    ('Dentista Veterinario', 'Dentista Veterinario'),
    ('Dermatólogo Veterinario', 'Dermatólogo Veterinario'),
    ('Cardiólogo Veterinario', 'Cardiólogo Veterinario'),
    ('Oftalmólogo Veterinario', 'Oftalmólogo Veterinario'),
    ('Oncólogo Veterinario', 'Oncólogo Veterinario'),
    ('Neurólogo Veterinario', 'Neurólogo Veterinario'),
    ('Radiología Veterinaria', 'Radiología Veterinaria'),
    ('Rehabilitación Veterinaria', 'Rehabilitación Veterinaria'),
)

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    especialidad = models.CharField(max_length=40, choices=ESPECIALIDAD_CHOICES, blank=True)

    def __str__(self):
        return f"Nombre:{self.nombre} | Apellido:{self.apellido} | Especialidad:{self.especialidad}"
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        super(Profesional, self).save(*args, **kwargs)

class Cuidador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre:{self.nombre} | Apellido:{self.apellido}"
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.direccion = self.direccion.capitalize()
        super(Cuidador, self).save(*args, **kwargs)

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Adopción de {self.animal.nombre} por {self.nombre} {self.apellido}"
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.direccion = self.direccion.capitalize()
        super(Adopcion, self).save(*args, **kwargs)
