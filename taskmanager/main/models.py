from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Name of task', max_length=70)
    task = models.TextField('About task')

    def __str__(self):
        return self.title

  #Change name of table
    class Meta:
      verbose_name = 'Specific task'
      verbose_name_plural = 'All tasks'