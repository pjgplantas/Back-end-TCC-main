
from django.db import models

class TipoUsuario (models.Model):
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.desc

class Usuario (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=9)
    senha = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Planta (models.Model):
    tipo_planta = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    nome = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.nome

class Pagamento (models.Model):
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.descricao

class Boleto (models.Model):
    nome = models.CharField(max_length=150)
    boleto = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Cartao (models.Model):
    numero = models.CharField(max_length=19)
    cvv = models.IntegerField()
    validade = models.DateTimeField()
    nometitular = models.CharField(max_length=100)
    cartao = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Pix (models.Model):
    banco = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.EmailField
    pix = models.ForeignKey(Usuario, on_delete=models.PROTECT
    )

class PedidoCarrinho (models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade_itens = models.IntegerField()
    dth = models.DateTimeField()
    dt_entrega = models.DateTimeField()
    boleto1 = models.ForeignKey(Boleto, on_delete=models.PROTECT, blank=True, null=True)
    cartao1 = models.ForeignKey(Cartao, on_delete=models.PROTECT, blank=True, null=True)
    pix = models.ForeignKey(Pix, on_delete=models.PROTECT, blank=True, null=True)
    pedido = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pedido2 = models.ForeignKey(Pagamento, on_delete=models.PROTECT)


class ItensCarrinho (models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT,)
    pedido = models.ForeignKey(PedidoCarrinho, on_delete=models.PROTECT)
    dt_entrega = models.DateField()
    dth = models.DateTimeField()
    endereco = models.CharField(max_length=200)

class Comentario (models.Model):
    texto = models.TextField(max_length=500)
    dth = models.DateTimeField()
    comentario1 = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    comentario2 = models.ForeignKey(Planta, on_delete=models.PROTECT)

class Midia (models.Model):
    local = models.ImageField()
    titulo = models.CharField(max_length=150)
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)