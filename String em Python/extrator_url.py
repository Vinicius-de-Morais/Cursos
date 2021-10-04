import re


class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A url está vazia')
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        verifica = padrao_url.match(self.url)

        if not verifica:
            raise ValueError('A url não é válida')

    def get_url_base(self):
        encontra_interrogacao = self.url.find('?')
        url_base = self.url[:encontra_interrogacao]
        return url_base

    def get_url_parametros(self):
        encontra_interrogacao = self.url.find('?')
        url_parametro = self.url[encontra_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_de_busca):
        busca = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = busca + len(parametro_de_busca) + 1
        posicao_e = self.get_url_parametros().find('&', indice_valor)
        if posicao_e == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:posicao_e]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url


extrator_url = ExtratorURL('https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

def calcula():
    if moeda_origem == "real" and moeda_destino == "dolar":
        valor_conversao = int(quantidade) / VALOR_DOLAR
        print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
    elif moeda_origem == "dolar" and moeda_destino == "real":
        valor_conversao = int(quantidade) * VALOR_DOLAR
        print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
    else:
        print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")

calcula()