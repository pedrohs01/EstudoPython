def criaArquivo(nome="",ext="",cont="")->str:
    """A função criaArquivo recebe o nome do arquivo
    a extensãp e por fim algo para inserir no arquivo,
    é criar este arquivo no diretório local"""
    f = open(nome+"."+ext,"a")
    f.write(cont)
    f.close()
    return "Arquivo criado com sucesso"

print(criaArquivo("Nike","csv","texto;mensagem;ola"))