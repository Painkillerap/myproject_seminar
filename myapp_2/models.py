from django.db import models

from django.utils import timezone

base_coin = []


class Coin(models.Model):
    result = models.CharField(max_length=10)
    throw_time = models.DateTimeField(default=timezone.now)

    @staticmethod
    def statistic(count):
        res_heads = 0
        res_tails = 0
        for i in range(count):
            if base_coin[i].result == True:
                res_heads += 1
            else:
                res_tails += 1
        return {'Орел': res_heads, 'Решка': res_tails}


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_body = models.TextField()
    date_publication = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='post')
    count_view = models.IntegerField(default=0)
    publication = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_create = models.DateField(auto_now=True)
    date_change = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.comment}'
