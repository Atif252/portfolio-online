from django.db import models

class Project(models.Model):

    POGRAMMING_LANG_CHOICES = (
		('python', 'Python'),
		('js', 'Javascript'),
        ('django', 'Django'),
	)

    title				= models.CharField(max_length=2200, null=False, blank=True)
    detail              = models.CharField(max_length=2200, null=True, blank=True)
    image				= models.ImageField(null=False, blank=False)
    date_published		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
    lang                = models.CharField(max_length=200, choices=POGRAMMING_LANG_CHOICES, null=False)
   
    objects = models.Manager()

    def __str__(self):
        return self.title