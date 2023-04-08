from django.test import TestCase
from ..models import Pessoa

# Create your tests here.
class PessoaTestCase(TestCase):
    def setUp(self):
        Pessoa.objects.create(
            nome = "Carlos Roberto",
            idade = 37
        )

    def test_return_nome(self):
        p1 = Pessoa.objects.get(nome="Carlos Roberto")
        self.assertEquals(p1.__str__(), "Carlos Roberto")

    def test_return_idade(self):
        p1 = Pessoa.objects.get(idade=37)
        self.assertEquals(p1.__str__(), 37)
    