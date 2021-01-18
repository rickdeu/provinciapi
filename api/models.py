from django.db import models

class Provincia(models.Model):
    province = models.CharField(max_length=200,default='', verbose_name="Province")
    capital = models.CharField(max_length=200,default='', verbose_name="Capital")

    def __str__(self):
        return self.province
    class Meta:
        ordering = ['province']
class Municipio(models.Model):
    municipe = models.CharField(verbose_name="Municipe",default='', max_length=200)
    id_province = models.ForeignKey(Provincia,related_name='id_provincia',default='',verbose_name="Province", on_delete=models.CASCADE)
    def __str__(self):
        return self.municipe
    class Meta:
        ordering = ['id_province','municipe']


class Bairro(models.Model):
    neighbood = models.CharField(verbose_name="Neighbood",default='', max_length=200)
    street = models.CharField(verbose_name="Street",default='', max_length=200)
    id_municipe = models.ForeignKey(Municipio,verbose_name="Municipe",default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.neighbood +' '+self.street
    class Meta:
        ordering = ['neighbood']

