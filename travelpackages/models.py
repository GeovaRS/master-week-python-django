from django.db import models
import os

# Create your models here.

class TravelPackage(models.Model):
 name = models.CharField(max_length=255, verbose_name="Nome")
 original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Original")
 discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço com Desconto")
 image = models.ImageField(upload_to="travelpackages", verbose_name="Imagem")
 description = models.TextField(verbose_name="Descrição", blank=True, null=True)
 created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
 updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado em")

 # Sobrescrever o Método save no Modelo
 def save(self, *args, **kwargs):
  # Verificar se o objeto já existe no banco de dados
  if self.pk:
   # Buscar o objeto atual no banco de dados
   old_image = TravelPackage.objects.get(pk=self.pk).image

   # Comparar se a imagem foi alterada
   if old_image and old_image != self.image:
    # Remover a imagem antiga do sistema de arquivos
     if os.path.isfile(old_image.path):
      os.remove(old_image.path)

  # Salvar novo registro
  super().save(*args, **kwargs)

 # Sobrescrever o Método delete do Django para Remover a Imagem
 def delete(self, *args, **kwargs):
  # Remover a imagem associada ao objeto
  if self.image and os.path.isfile(self.image.path):
   os.remove(self.image.path)

  # Excluir o registro
  super().delete(*args, **kwargs)

 def __str__(self):
  return self.name

 class Meta:
  db_table = "travelpackages"
  verbose_name = "pacote de viagem"
  verbose_name_plural = "pacotes de viagens"
