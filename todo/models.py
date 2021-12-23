from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nom de la tâche')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'

    def __str__(self):
        return self.name
