from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    name = models.CharField(max_length= 50)
    age = models.IntegerField()
    email = models.EmailField()
    role = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


class matiere(models.Model):
    nom = models.CharField(max_length= 20)
    coeff = models.IntegerField()
    professeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class grade(models.Model):
    student = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(matiere, on_delete=models.CASCADE)
    grade = models.FloatField()