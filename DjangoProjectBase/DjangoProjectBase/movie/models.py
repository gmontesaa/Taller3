from django.db import models
import numpy as np


# Crear embedding binario
embedding_array = np.array([0.1, 0.2, 0.3])
binary_data = embedding_array.tobytes()

# Leer embedding desde binario
recovered_array = np.frombuffer(binary_data, dtype=np.float32)

def get_default_array():
    default_arr = np.random.rand(1536)
    return default_arr.tobytes()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='movie/images/', default = 'movie/images/default.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    emb = models.BinaryField(default=get_default_array())

    def __str__(self):
        return self.title