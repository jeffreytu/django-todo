from django.db import models

# Create your models here.
# Model is a representation of the data we want to store in the database

# What kind of data do we need in a ToDo?
class ToDo(models.Model):
    #SQL table with a column called name and restriction on length of 100
    name = models.CharField(max_length=100)
    due_date = models.DateField()

    #string method used to return a string representation
    def __str__(self):
        return self.name