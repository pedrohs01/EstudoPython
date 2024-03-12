# este programa exibe uma janela de PDV(Ponto de Venda).
# neste pdv estamos demostrando um caixa de uma padaria 
# vamos importa a biblioteca de sistema para executar a janela 
import sys
# importação dos elementos gráficos do pacote PyQT
from PyQt5.QtWidgets import QWidget,QApplication, QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout
# para usar imagens em nosso projetos iremos importar Qpixmap do pacote PyQT5.Gui
from PyQt5.QtGui import QPixmap


class PDV(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(5,20,1580,860)
        self.setWindowTitle("Caixa PDV - Padaria")

        # criaçaõ do layout principal que irá dividir a tela em duas colunas 
        # Onde a coluna da esqurda terá uma label e a coluna da dirieta terá outra label 
        layout_hor_principal = QHBoxLayout()
        
        # vamos criar duas labels que representarão as colunas sendo uma label col esquerda e col direita
        label_col_esquerda = QLabel()
        label_col_direita = QLabel()

        # configurar a largura e a cor de fundo da col esquerda
        label_col_esquerda.setStyleSheet("QLabel{background-color:red}")
        label_col_esquerda.setFixedWidth(790)

        # configurar a largura e a cor de fundo da col direita
        label_col_direita.setStyleSheet("QLabel{background-color:blue}")
        label_col_direita.setFixedWidth(790)

        # Vamos adicionar as duas labels a tela.
        layout_hor_principal.addWidget(label_col_esquerda)
        layout_hor_principal.addWidget(label_col_direita)

        # Adicionar o layout principal a tela 
        self.setLayout(layout_hor_principal)

        # ---------------------------------------------------------------------------------------------------------------------------------------------
        # Trabalhando com a col esquerda 
        # definir o layout vertical da col esquerda
        layout_ver_col_esquerda = QVBoxLayout()
        # criar uma label para adicionar uma imagem
        label_img = QLabel()
        label_img.setPixmap(QPixmap("logo.png"))
        # ajustar o tamanho da imagem ao tamanho da label
        label_img.setScaledContents(True) 

        # adicionar a label que está com a imagem a o layout da esquerda 
        layout_ver_col_esquerda.addWidget(label_img)
        
        label_codigo = QLabel("Código do Produto:")
        label_codigo.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_codigo)

        edit_codigo = QLineEdit()
        edit_codigo.setStyleSheet("QLineEdit{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(edit_codigo)

        label_nome = QLabel("Nome do Produto:")
        label_nome.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_nome)

        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(edit_nome)

        label_produto = QLabel("Descrição do Produto:")
        label_produto.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_produto)

        edit_produto = QLineEdit()
        edit_produto.setStyleSheet("QLineEdit{padding:10x; font-size:15pt}")
        edit_produto.setFixedHeight(120)
        layout_ver_col_esquerda.addWidget(edit_produto)

        label_quantidade = QLabel("Quantidade do Produto:")
        label_quantidade.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_quantidade)

        edit_quantidade = QLineEdit()
        edit_quantidade.setStyleSheet("QLineEdit{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(edit_quantidade)

        label_preco = QLabel("Preço Unitário do Produto:")
        label_preco.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_preco)

        edit_preco = QLineEdit()
        edit_preco.setStyleSheet("QLineEdit{padding:10px; font-size:15pt}")
        layout_ver_col_esquerda.addWidget(edit_preco)

        label_total = QLabel("Sub Total:")
        label_total.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_total)

        edit_total = QLineEdit("Tecle F3 para calcular o subtotal")
        edit_total.setStyleSheet("QLineEdit{padding:10px; font-size:15pt}")
        edit_total.setEnabled(False)
        layout_ver_col_esquerda.addWidget(edit_total)

        #-----------------------------------------------------------------------------------------------------------------------------------------------
        # vamos trabalhar com a coluna da direita 
        # criando uma tabela 
        tabela = QTableWidget()
        # Vamos definir a quatidade de linhas e colunas
        tabela.setColumnCount(5)
        tabela.setRowCount(10)
        # Definir o cabeçalho das colunas
        cabecalho = ["Código","Nome do Produto","Quatidade","Preço Unitário","Preço Total"]
        # Adicionar o cabeçalho na tabela
        tabela.setHorizontalHeaderLabels(cabecalho)

        # adicionar no layout da direita
        layout_ver_col_direita = QVBoxLayout()
        layout_ver_col_direita.addWidget(tabela)
        label_col_direita.setLayout(layout_ver_col_direita)


        label_pagar = QLabel("Total a Pagar")
        label_pagar.setStyleSheet("QLabel{font-size:30pt;color:white}")
        layout_ver_col_direita.addWidget(label_pagar)

        edit_pagar = QLineEdit("0,00")
        edit_pagar.setStyleSheet("QLineEdit{font-size:60pt; padding:10px}")
        layout_ver_col_direita.addWidget(edit_pagar)


        # vamos adicionar o layout verical da esquerda à label da coluna da esquerda
        label_col_esquerda.setLayout(layout_ver_col_esquerda)

app = QApplication(sys.argv)
janela = PDV()
janela.show()
app.exec_()        