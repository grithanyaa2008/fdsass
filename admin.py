from django.contrib.auth.models import User
u = User.objects.get(username="grithanyaa")
u.is_staff=True
u.is_superuser=True
u.save()

print(u.is_staff, u.is_superuser, u.is_active)

