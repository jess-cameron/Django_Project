from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()

class UserFavorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    news_story = models.ForeignKey(NewsStory, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'news_story')


