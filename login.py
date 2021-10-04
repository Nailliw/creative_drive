from PyQt5 import uic, QtWidgets
import requests, json


def login():
    login_screen.error_message.setText("")
    username = login_screen.login_email.toPlainText()
    password = login_screen.login_password.text()

    if username == "will" and password == "1234":
        login_screen.close()
        home_screen.show()
    else:
        login_screen.error_message.setText("Dados de login incorretos.")


def logout():
    home_screen.close()
    login_screen.show()


def register():
    login_screen.close()
    register_screen.show()


def send_new_register():
    email = register_screen.email.toPlainText()
    name = register_screen.name.toPlainText()
    password = register_screen.password.text()
    confirmPassword = register_screen.confirm_password.text()

    if password == confirmPassword:
        try:
            register_screen.error_message.setText("Usuário cadastrado com sucesso!")

            register_screen.close()
            login_screen.show()

        except:
            register_screen.error_message.setText("Erro ao inserir dados.")


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
