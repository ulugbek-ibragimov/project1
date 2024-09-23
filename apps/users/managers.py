from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not login:
            raise ValueError("The given login must be set")

        user = self.model(login=login, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user


    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(login, password, **extra_fields)

