"""
URL configuration for book project.

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from book1.views import hello_view, anekdot_view, main_view, book_list_view, book_detail_view, book_create_view, review_create_view
urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_view, name="hello_view"),
    path('fun/', anekdot_view, name='anekdot_view'),
    path('', main_view, name='main_view'),
    path('books/', book_list_view, name='book_list_view'),
    path("book/<int:book_id>/", book_detail_view, name='book_detail_view'),
    path("books/create/", book_create_view, name='post_create_view'),
    path("books/create_review/", review_create_view, name='review_create_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

