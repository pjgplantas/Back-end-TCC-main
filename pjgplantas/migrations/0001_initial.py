# Generated by Django 4.0.6 on 2022-07-17 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=19)),
                ('cvv', models.IntegerField()),
                ('validade', models.DateTimeField()),
                ('nometitular', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_planta', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('nome', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=9)),
                ('senha', models.CharField(max_length=50)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Pix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('pix', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantidade_itens', models.IntegerField()),
                ('dth', models.DateTimeField()),
                ('dt_entrega', models.DateTimeField()),
                ('boleto1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.boleto')),
                ('cartao1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.cartao')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario')),
                ('pedido2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.pagamento')),
                ('pix', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.pix')),
            ],
        ),
        migrations.CreateModel(
            name='ItensCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_entrega', models.DateField()),
                ('dth', models.DateTimeField()),
                ('endereco', models.CharField(max_length=200)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.pedidocarrinho')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.planta')),
            ],
        ),
        migrations.CreateModel(
            name='Curtida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dth', models.DateTimeField()),
                ('qnt_curtida', models.IntegerField()),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.planta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=500)),
                ('dth', models.DateTimeField()),
                ('comentario1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario')),
                ('comentario2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.planta')),
            ],
        ),
        migrations.AddField(
            model_name='cartao',
            name='cartao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario'),
        ),
        migrations.AddField(
            model_name='boleto',
            name='boleto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario'),
        ),
    ]