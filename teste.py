import Menu_select as ms

menu = ms.Menu_seleção(cabeçalho='cabeçalho',texto_seleção = ['negrito','vermelho','verde'])
opt = ['Logar','Cadastrar','Sair']
escolha = menu.options(descrição='Essa é a descrição',opções=opt)

print("\n\nSeleção: ", opt[escolha])