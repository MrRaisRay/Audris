from django.db import models
# Create your models here.

class About(models.Model):
    about_text = models.TextField("текст 'О НАС'")

class Vacancy(models.Model):
    vacancy_title = models.CharField("название вакансии", max_length= 200)

class Picture(models.Model):
    picture_file = models.ImageField("имя картинки")

class Appeal(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete= models.CASCADE)
