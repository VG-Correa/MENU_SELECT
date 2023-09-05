import Menu_select as ms

menu = ms.Menu_select(cabeçalho='cabeçalho',texto_seleção = ['negrito','vermelho','azul'])
opt = ['Logar','Cadastrar','Sair']
escolha = menu.options(descrição='Essa é a descrição',opções=opt)

print("\n\nSeleção: ", opt[escolha])