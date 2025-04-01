"""
URL configuration for moviereviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie import views as movieViews
from movie.views import movie_recommendation


from django.conf.urls.static import static
from django.conf import settings

from movie.views import home, about, statistics_view, signup, movie_recommendation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('news/', include('news.urls')),
    path('statistics/', statistics_view, name='statistics'),
    path('signup/', signup, name='signup'),
    path('recommend/', movie_recommendation, name='movie_recommendation'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
