

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, calcula_imposto):
        valor = calcula_imposto. calcula(orcamento)
        print (valor)

if __name__ == '__main__':
    from impostos import ISS, ICMS
    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())