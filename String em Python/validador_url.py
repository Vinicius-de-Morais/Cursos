import re
url = 'https://www.bytebank.com/cambio'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
verifica = padrao_url.match(url)

if not verifica:
    raise ValueError('A url não é válida')
print('A url é valida')
