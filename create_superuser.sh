echo "
from django.contrib.auth.models import User
try:
	User.objects.create_superuser('admin', 'admin@mail.com', 'admin')
except:
	pass
" | python manage.py shell 
