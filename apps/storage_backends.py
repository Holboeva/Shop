# apps/storage_backends.py
from django.core.files.storage import FileSystemStorage
import os

class StaticStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        location = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/images')  # Specify the location inside static/images
        base_url = '/static/images/'  # URL to access the uploaded images
        super().__init__(location, base_url)
