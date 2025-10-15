from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.nome}"
    
class Livro(models.Model):
    isbn = models.CharField( max_length=13, unique=True)
    titulo = models.CharField(max_length=20)
    data_publicacao = models.DateField()
    preco = models.DecimalField( max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titulo}"
    
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nome}"
    
class Publica(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("livro", "autor")

    def __str__(self):
        return f"{self.autor.nome} - {self.livro.titulo}"