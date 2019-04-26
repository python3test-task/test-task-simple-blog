from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.utils.text import slugify
from uuslug import slugify  # slugify из библеотеки uuslug делает транслитерацию кирилици в латиницу


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200)
    users_readers = models.ManyToManyField('auth.User', related_name='posts_readers', blank=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, self.slug])

    # создаем slug из title, в случае если пост создан через интерфейс сайта (а не через админку)
    def save(self, *args, **kwargs):
        if not self.slug:
            #self.slug = slugify(self.title, allow_unicode=True)
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Contact(models.Model):
    # user_from: ForeignKey для пользователя, который создает связь
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    # user_to: ForeignKey для пользовтеля являющегося отслеживаемым
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

# динамически добавляем поле к User
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

