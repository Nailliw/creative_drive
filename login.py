from os import times
from PyQt5 import uic, QtWidgets
import requests
import time
import multiprocessing

URL_BASE = "localhost:8000/"


def login():
    login_screen.error_message.setText("")
    username = login_screen.login_email.toPlainText()
    password = login_screen.login_password.text()

    if username != "" and password != "":
        #requisicao = requisicao_login(username=username, password=password)
        requisicao = True
        if requisicao:
            login_screen.close()
            home_screen.show()
        else:
            login_screen.error_message.setText("Dados de login incorretos.")

    else:
        login_screen.error_message.setText("Dados de login incorretos.")


def requisicao_login(username, password):
    data = data = {"username": username, "password": password}
    response = requests.post(
        f'{URL_BASE}/login/', data=data
    ),
    if response.status_code == 200:
        return True
    else:
        return False


def logout():
    home_screen.close()
    login_screen.show()


def register():
    login_screen.close()
    register_screen.show()


def send_new_register():
    username = register_screen.email.toPlainText()
    name = register_screen.name.toPlainText()
    password = register_screen.password.text()
    confirmPassword = register_screen.confirm_password.text()

    if username != "" and password != "" and name != "" and confirmPassword != "":
        if password == confirmPassword:
            #requisicao = requisicao_sign(username, password)
            requisicao = True
            if requisicao:
                try:
                    register_screen.error_message.setText(
                        "Usuário cadastrado com sucesso!")

                    register_screen.close()
                    login_screen.show()

                except:
                    register_screen.error_message.setText(
                        "Erro ao inserir dados.")
    else:
        register_screen.error_message.setText(
            "Erro ao inserir dados.")


def requisicao_sign(username, password):
    data = data = {"username": username, "password": password}
    response = requests.post(
        f'{URL_BASE}/signup/', data=data
    ),

    if response.status_code == 201:
        return response.content
    else:
        return response.content


def requisicao_upload(self, name, file):

    response = requests.post(
        f'{URL_BASE}/users/', files=dict(foo=file)
    ),

    if response.status_code == 201:
        return response.content
    else:
        return response.content


app = QtWidgets.QApplication([])
login_screen = uic.loadUi("login_page.ui")
register_screen = uic.loadUi("signup_page.ui")
home_screen = uic.loadUi("home_page.ui")
login_screen.loginButton.clicked.connect(login)
login_screen.signup_button.clicked.connect(register)
register_screen.registerButton.clicked.connect(send_new_register)
home_screen.logoutButton.clicked.connect(logout)

login_screen.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
register_screen.password.setEchoMode(QtWidgets.QLineEdit.Password)
register_screen.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)

login_screen.show()
app.exec()
