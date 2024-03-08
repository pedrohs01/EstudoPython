import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

class JanelaControles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de cliente")
        self.setGeometry(15, 20, 500, 600)

        # Criar um layout para organizar os componentes
        layout = QVBoxLayout()

        # Label para o titulo da janela 
        label_titulo = QLabel("Gerenciar os clientes")
        label_titulo.setStyleSheet("QLabel{font-size:20pt;color:#fe09c4;font-weight:bold}")

        # Criar elemesntos de texto para pedir ao usuário entrar
        # com dados do clientes. Criaremos as labels(rótulo)
        label_nome = QLabel("Nome do cliente:")
        label_nome.setStyleSheet("QLabel{font-size:20pt;color:#fe09c4;font-weight:bold}")
        label_email = QLabel("E-Mail:")
        label_email.setStyleSheet("QLabel{font-size:20pt;color:#fe09c4;font-weight:bold}")
        label_telefone = QLabel("Telefone:")
        label_telefone.setStyleSheet("QLabel{font-size:20pt;color:#fe09c4;font-weight:bold}")

        # Criar elementos para que o usuário possam escrever o que 
        # as labels estão pedindo
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{padding:10px; border-radius:10px;}")
        edit_email = QLineEdit()
        edit_email.setStyleSheet("QLineEdit{padding:10px; border-radius:10px;}")
        edit_telefone = QLineEdit()
        edit_telefone.setStyleSheet("QLineEdit{padding:10px; border-radius:10px;}")

        # Criar um controle de botão para realizar um possivel cadastro
        botao_cadastro = QPushButton("Cadastrar")

        # Adicionar titulo
        layout.addWidget(label_titulo)

        #Adicionar os controles de label e edit ao layout
        layout.addWidget(label_nome)
        layout.addWidget(edit_nome)

        layout.addWidget(label_email)
        layout.addWidget(edit_email)

        layout.addWidget(label_telefone)
        layout.addWidget(edit_telefone)

        layout.addWidget(botao_cadastro)

        # adicionar o layout na janela 
        self.setLayout(layout)
    
app = QApplication(sys.argv)
tela = JanelaControles()
tela.show()
app.exec_()
