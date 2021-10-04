import re  # Regular Expression -- RegEx


endereco = 'Nunciata Euvira Roncarati, 252, Itapoa, Londrina, PR, 86080668'

# 5 digitos + hifem (opcional) + 3 digitos

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
