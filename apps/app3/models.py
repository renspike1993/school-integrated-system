from django.db import models
from django.contrib.auth.models import User

class UploadedDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")
    filename = models.CharField(max_length=255)
    page_count = models.IntegerField()
    file_size = models.BigIntegerField()
    paper_size = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def size_mb(self):
        return round(self.file_size / 1024 / 1024, 2)
