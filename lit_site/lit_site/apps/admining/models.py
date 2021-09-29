from django.db import models
# Create your models here.

class About(models.Model):
    about_text = models.TextField("текст 'О НАС'")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Vacancy(models.Model):
    vacancy_title = models.CharField("название вакансии", max_length= 200)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

class Picture(models.Model):
    picture_file = models.ImageField("имя картинки")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

class Appeal(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete= models.CASCADE)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
