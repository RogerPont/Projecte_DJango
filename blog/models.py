from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    """
    Model que representa un autor amb el seu nom, cognom, email i biografia.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    @property
    def name(self):
        """
        Retorna el nom complet de l'autor.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Retorna una representació en cadena de l'autor, que és el seu nom complet.
        """
        return self.name


class Tag(models.Model):
    """
    Model que representa una etiqueta (tag) per categoritzar posts.
    """

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        """
        Retorna el nom de l'etiqueta.
        """
        return self.name


class Post(models.Model):
    """
    Model que representa una publicació (post) de la biblioteca virtual.
    Inclou títol, slug, contingut, resum, data, autor, etiquetes i imatge.
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        """
        Retorna el títol de la publicació.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Guarda la publicació i genera automàticament un slug a partir del títol si no existeix.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
