from django.db import models
from django.contrib.auth.models import User


class AbstractPost(models.Model):
    """
    The abstract model that defines the common fields for all subclasses
    """
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)
    upvotes = models.ManyToManyField(User, related_name='%(class)s_upvoted')
    downvotes = models.ManyToManyField(User, related_name='%(class)s_downvoted')

    @property
    def score(self):
        return self.upvotes.count() - self.downvotes.count()

    class Meta:
        abstract = True


class Comment(AbstractPost):
    """
    A generic comment model. Comments can be added to questions or answers.
    """
    # TODO: a comment can be only attached to either a question or an answer, but not both. How to enforce this?
    question = models.ForeignKey('Question', null=True, related_name='comments')
    answer = models.ForeignKey('Answer', null=True, related_name='comments')


class Question(AbstractPost):
    """
    A question model. Questions can be tagged with multiple `Tag` objects. The `views` field should increment itself
    on a page load/view. Each question can have one accepted `answer` object.
    """
    tags = models.ManyToManyField('Tag', related_name='questions')
    # TODO: accepting an answer is creating a 1-to-1 entry between the question and answer, but it doesn't validate
    #       whether the question and answer are related already. Should there be a limit_choices_to parameter here?
    #       Or a different way of denoting whether an answer is accepted?
    accepted_answer = models.OneToOneField('Answer', null=True, related_name='accepted')
    views = models.PositiveIntegerField(default=0)


class Answer(AbstractPost):
    """
    An answer object must be associated with a question object.
    """
    question = models.ForeignKey('Question', related_name='answers')


class Tag(models.Model):
    """
    Tag names are lower case strings (enforced on save). They can be associated to many Questions. Users can "follow"
    specific "tags" to be alerted when a new question is created that contains said tag(s).
    """
    name = models.CharField(unique=True, max_length=128)
    users = models.ManyToManyField(User, related_name='following')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Tag, self).save(*args, **kwargs)
