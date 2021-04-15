import uuid as uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import User


class BaseModel(models.Model):
    """parent model which will be inherited by all other child models"""
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'It tells if fields can be active or not. '
            'Unselect this instead of deleting.'
        ),
    )
    is_delete = models.BooleanField(_('delete'), default=False)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class MovieCollection(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_collections')

    class Meta:
        db_table = 'movie_collection'
        verbose_name = _('Movie Collection')
        verbose_name_plural = _('Movie Collections')

    def __str__(self):
        return self.uuid.__str__()


class MovieGenre(models.Model):
    collection = models.ForeignKey(MovieCollection, on_delete=models.CASCADE, related_name='collection_movies',
                                   db_index=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    movie_uuid = models.CharField(max_length=100)

    class Meta:
        db_table = 'movie_genre'
        verbose_name = _('Movie Genre')
        verbose_name_plural = _('Movie Genres')
