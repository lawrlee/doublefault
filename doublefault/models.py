from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    owner = models.ForeignKey(User)
    upvotes = models.ManyToManyField(User, related_name='upvoted_posts')
    downvotes = models.ManyToManyField(User, related_name='downvoted_posts')
    parent_post = models.ForeignKey('self', related_name='child_posts')

    @property
    def score(self):
        return self.upvotes.count() - self.downvotes.count()

class QuestionPost(Post):
    tags = models.ManyToManyField('Tag', related_name='questions')
    accepted_answer = models.OneToOneField('AnswerPost', related_name='accepted')
    views = models.PositiveIntegerField()
    parent_post = None


class AnswerPost(Post):
    question = models.ForeignKey('QuestionPost', related_name='answers')


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=128)
    users = models.ManyToManyField(User, related_name='following')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Tag, self).save(*args, **kwargs)
