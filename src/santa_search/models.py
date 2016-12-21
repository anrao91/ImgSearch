from redisco import models

class Image(models.Model):
    url = models.Attribute(required=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ListField(str)
