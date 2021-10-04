from acessa_cep import BuscaEndereco

cep = 86076668
cep_obj = BuscaEndereco(cep)
print(cep_obj.acessa_via_cep())





# from telefoneBr import TelefoneBr
# import re
# telefone = '43984849292'
# telefone_obj = TelefoneBr(telefone)
#          (xx) zzzzz-wwww
# padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
# texto = 'eu gosto do numero 5543984849292'
# resposta = re.findall(padrao, texto)
# print(resposta)
# print(telefone_obj)

# from datas_br import DatasBr
# cadastro = DatasBr()
# print(cadastro)

