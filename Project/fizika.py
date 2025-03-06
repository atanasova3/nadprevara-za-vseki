from django.db import models
from datetime import date, time

class PhysicsCompetition(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time} at {self.location}"

# Creating competition instances correctly
competitions = [
    PhysicsCompetition(name="Национална Олимпиада по Физика", date=date(2025, 3, 15), time=time(10, 0), location="София"),
    PhysicsCompetition(name="Регионално Състезание", date=date(2025, 4, 10), time=time(14, 0), location="Пловдив"),
    PhysicsCompetition(name="Училищно Състезание", date=date(2025, 5, 5), time=time(9, 30), location="Варна")
]

# Saving the objects to the database
for competition in competitions:
    competition.save()
