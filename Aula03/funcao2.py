def desconto(preco = 0.0, taxa = 0.0):
    """A função desconto realiza cálculo
    de desconto recebendo o valor de preço de um produto 
    e multiplica pelo valpr da taxa e exibe o resultado em tela
    ao final"""
    vl_desc = preco * (taxa / 100)
    vl_fin = preco - vl_desc
    print(f"O valor de desconto é {vl_desc} e o valor final é {vl_fin}")

desconto(800,7)