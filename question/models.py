from django.db import models

class Anquan(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)

class Xianchang(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)
