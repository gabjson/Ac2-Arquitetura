import abc
from unittest import TestCase, main

class Calculadora(object):
    def calcular(self, num1, num2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if (operacao == None):
            return 0
        else:
            result = operacao.executar(num1, num2)
            return result

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, num1, num2):
        pass

class Soma(Operacao):
    def executar(self, num1, num2):
        result = num1 + num2
        return result

class Subtracao(Operacao):
    def executar(self, num1, num2):
        result = num1 - num2
        return result

class Multiplicacao(Operacao):
    def executar(self, num1, num2):
        result = num1 * num2
        return result

class Divisao(Operacao):
    def executar(self, num1, num2):
        result = num1 / num2
        return result

class Testes(TestCase):
    def test_multiplicacao(self):
        calc = Calculadora()
        result = calc.calcular(10,50, 'multiplicacao')
        self.assertEqual(result, 500)

    def test_divisao(self):
        calc = Calculadora()
        result = calc.calcular(100,10, 'divisao')
        self.assertEqual(result, 10)

    def test_soma(self):
        calc = Calculadora()
        result = calc.calcular(10,10, 'soma')
        self.assertEqual(result, 20)

    def test_subtracao(self):
        calc = Calculadora()
        result = calc.calcular(10,10, 'subtracao')
        self.assertEqual(result, 0)
    
if _name_ == '_main_':
    main()