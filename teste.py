import Menu_select as ms

menu = ms.Menu_select(cabeçalho='cabeçalho',texto_seleção = ['negrito','vermelho','azul'])
opt = ['Logar',menu]
escolha = menu.options(descrição='Essa é a descrição',opções=opt,limite_opçoes=3)

print("\n\nSeleção: ", opt[escolha])