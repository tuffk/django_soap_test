from django.db import models


class Question(models.Model):
    question_q = models.CharField(max_length=255)
    question_a = models.CharField(max_length=255)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f'Pregunta: {self.question_q}\nRespuesta: {self.question_a}\n'

    @property
    def greet(self):
        return f"hola {self.question_q}"

    def area(self, x, y):
        lalala()
        return x * y


def lalala():
    print("lalala")
