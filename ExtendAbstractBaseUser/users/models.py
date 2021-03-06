from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

"""
Kullanıcı Modelini Özel Bir Model Kullanarak Genişletme AbstractBaseUser'ı Genişletme
AbstractBaseUser yalnızca kimlik doğrulama işlevine sahiptir, alt sınıf oluşturduğunuzda kullanmak için kullanacağınız alanları sağlayabileceğiniz gerçek alanlara sahip değildir.
Django, özel bir modele başvuran AUTH_USER_MODEL ayarı için bir değer sağlayarak varsayılan kullanıcı modelini geçersiz kılmanıza olanak tanır:
#settings.py
AUTH_USER_MODEL = 'myapp.MyUser'
Bu model, varsayılan kullanıcı modeliyle aynı şekilde davranır, ancak ihtiyaç duyulursa gelecekte bunu özelleştirebileceksiniz:
"""


class MyUserManager(BaseUserManager):
    
    def create_user(self, email, date_of_birth, password=None):
        
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    date_of_birth = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        
        return self.is_admin
    