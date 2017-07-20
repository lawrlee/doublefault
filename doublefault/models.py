from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    owner = models.ForeignKeyField(User, related_field='posts')
    upvotes = models.ManyToManyField(User, related_field='upvoted_posts')
    downvotes = models.ManyToManyField(User, related_field='downvoted_posts')
    parent_post = models.ForeignKeyField(self, related_field='child_posts')

    @property
    def score(self):
        return self.upvotes.count() - self.downvotes.count()

class Question(Post):
    owner = models.ForeignKeyField(User, related_field='questions')
    tags = models.ManyToManyField(Tag, related_field='questions')
    accepted_answer = models.OneToOneField(Answer, related_field='accepted')
    views = models.PositiveIntegerField()
    parent_post = None


class Answer(Post):
    owner = models.ForeignKeyField(User, related_field='answers')
    question = models.ForeignKeyField(Question, related_field='answers')


class Tag(models.Model):
    name = models.CharField(unique=True)
    users = models.ManyToManyField(User, related_field='following')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Tag, self).save(*args, **kwargs)
