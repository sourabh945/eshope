
### django imports
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


### utils imports
from user.utils import validate_phone_no , validate_name

class USER_MANAGER(BaseUserManager):

    def create(self,name,phone,email,password,*args,**kwargs):

        if not name or not email or not phone or not validate_name(name) or not validate_phone_no(phone):
            raise ValidationError('name, phone no and email is neccessary for registations')

        email = self.normalize_email(email)
        user = self.model(name,phone,email,*args,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
