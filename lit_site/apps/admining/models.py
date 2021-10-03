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
    picture_file = models.ImageField("имя картинки", upload_to='lit_site/static/images')

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

class Appeal(models.Model):
    appealer_name = models.CharField("имя соискателя", max_length= 100)
    appealer_email = models.EmailField("E-mail соискателя", max_length= 50, default="jione_doe@example.com")
    appealer_message = models.TextField("Сообщение сосикателя")

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
