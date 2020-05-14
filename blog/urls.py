from django.conf.urls import url, include
from blog.views import first

urlpatterns = [
    url(r'', first),

]
