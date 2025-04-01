import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Verifica que los embeddings se almacenaron correctamente en la base de datos."

    def handle(self, *args, **kwargs):
        self.stdout.write("🔍 Verificando embeddings en la base de datos...\n")

        for movie in Movie.objects.all():
            if movie.emb:
                embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
                self.stdout.write(f"🎬 {movie.title} → Embedding: {embedding_vector[:5]}")
            else:
                self.stdout.write(f"⚠ {movie.title} no tiene embedding almacenado.")

        self.stdout.write("\n✅ Verificación completada.")
