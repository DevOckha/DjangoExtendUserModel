from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Bire Bir Bağlantı Kullanarak Kullanıcı Modelini Genişletme

Kullanıcı Modeli ile ilgili ekstra bilgileri depolamak için yeni bir Django Modeli oluşturacağız
"""

class Profile(models.Model):
    user = models.OneToOneRel(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=512)
    location = models.CharField(max_length=128, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    
    """Şimdi sihrin gerçekleştiği yer burasıdır: Artık sinyalleri tanımlayacağız, böylece Kullanıcı örnekleri oluşturduğumuzda/güncellediğimizde Profil modelimiz otomatik olarak oluşturulacak/güncellenecektir."""
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
    
    instance.profile.save()


"""Genel olarak konuşursak, asla Profilin kaydetme yöntemini çağırmanız gerekmeyecek. Her şey Kullanıcı modeli üzerinden yapılır."""

    