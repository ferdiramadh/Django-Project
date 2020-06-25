from django.db import models


# class Position(models.Model):
#     title = models.CharField(max_length=50)


# class Employee(models.Model):
#     fullname = models.CharField(max_length=100)
#     mobile = models.CharField(max_length=15)
#     position = models.ForeignKey(Position, on_delete=models.CASCADE)

class Member(models.Model): 
    fname = models.CharField(max_length=50) 
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lastname