#url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar'
url = ''

# Sanitiza a url
url = url.strip()

# Valida a url
if url== '':
    raise ValueError('A url está vazia')
# Separa base e parâmetros
encontra_interrogacao = url.find('?')
url_base = url[:encontra_interrogacao]
print(url_base)

# Busca valores
parametro_de_busca = 'moedaDestino'
url_parametro = url[encontra_interrogacao+1:]
busca = url_parametro.find(parametro_de_busca)

indice_valor = busca + len(parametro_de_busca) + 1
posicao_E = url_parametro.find('&', indice_valor)
if posicao_E == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:posicao_E]

print(valor)
