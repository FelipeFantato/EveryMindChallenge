from dataclasses import replace


listaUsuarios = open("listaUsuarios.txt", "a")
listaSenhas = open("listaSenhas.txt", "a")

def escreverEmTXT(nomeArquivo, conteudoNovo):
    lista = open(str(nomeArquivo), "r")
    conteudo = lista.readlines()
    conteudo.append(str(conteudoNovo) + "\n")
    lista = open(str(nomeArquivo), "w")
    lista.writelines(conteudo)
    lista.close()

def verificarSenha(usuario):
    senha = input("insira a sua Senha:")
    lista = open("listaSenhas.txt", "r")
    linhas = lista.readlines()
    senhaInterna = str(senha + usuario)
        
    for linha in linhas:
        linha = linha.replace("\n", "")
        
        if linha == senhaInterna:
            print("Boas vindas de volta a Oliveira Trade, " + usuario)
            return
        
        
        
    else:
        print("Senha inválida!")
        verificarSenha(usuario)
        
def criarSenha(usuario):
    senhaNova = input("Insira a sua senha: ")
    senhaNova2 = input("Insira novamente a sua senha: ")
    
    if senhaNova == senhaNova2:
        
        escreverEmTXT("listaSenhas.txt", senhaNova + usuario)        
        print("sua conta foi criada! Realize o Login...")
        login()
    else:
        print("senhas não identicas, escreva novamente")
        criarSenha(usuario)
        
def cadastro():
    print("Usuario novo!")
    usuarioNovo = input("Insira o seu nome de usuário: ")
    listaUsuarios = open("listaUsuarios.txt", "r")
    
    for linha in listaUsuarios.readlines():
        if linha == usuarioNovo:
            listaUsuarios.close()
            print("Usuário ja cadastro, tente realizar o login novamente")
            login()
    else:
        escreverEmTXT("listaUsuarios.txt",usuarioNovo)
        
    
    criarSenha(usuarioNovo)
    
    
def verificarUsuario(usuario):
    listaUsuarios = open("listaUsuarios.txt", "r")
    
    if usuario == "":
        cadastro()
    for linha in listaUsuarios.readlines():
        linha = linha.replace("\n", "")


        if linha == usuario:
            listaUsuarios.close()
            verificarSenha(usuario)
            break         
    else:
        print("Usuário Inválido")
        login()           





def login():
    usuario = input("insira o nome de Usuário, Caso seja usuário novo, aperte enter: ")
    verificarUsuario(usuario)                                         

print("Olá! Realize seu login:")
print(".......................")


login()