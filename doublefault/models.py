from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    owner = models.ForeignKey(User)
    upvotes = models.ManyToManyField(User, related_name='upvoted_posts')
    downvotes = models.ManyToManyField(User, related_name='downvoted_posts')
    parent_post = models.ForeignKey("self", related_name='child_posts')

    @property
    def score(self):
        return self.upvotes.count() - self.downvotes.count()

class Question(Post):
    tags = models.ManyToManyField("Tag", related_name='questions')
    accepted_answer = models.OneToOneField("Answer", related_name='accepted')
    views = models.PositiveIntegerField()
    parent_post = None


class Answer(Post):
    question = models.ForeignKey("Question", related_name='answers')


class Tag(models.Model):
    name = models.CharField(unique=True)
    users = models.ManyToManyField(User, related_name='following')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Tag, self).save(*args, **kwargs)
