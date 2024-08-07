# lista de cidades para pesquisar 
cidades = ['Brasília', 'Taguatinga', 'Planaltina', 'Ceilândia', 'Samambaia', 'Riacho fundo', 'Candangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

# usuário pesquisa pela cidade
cidade_pesquisada = input('Cidade a ser pesquisada: ').capitalize()

# verifica se a cidade existe
try:
    # pega o indice do item da pesquisa
    indice = cidades.index(cidade_pesquisada)
    print(f'\n{cidade_pesquisada} encontrada no índice {indice}.\n')
except:
    print(f'\nNão foi possível encontrar {cidade_pesquisada}.\n')