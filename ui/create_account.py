from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class CreateAccountScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1301, 811)
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1301, 811))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:rgb(158, 198, 243);}")
        self.widget.setObjectName("widget")
        
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(320, 60, 741, 171))
        self.label.setStyleSheet("font: 48pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(500, 170, 451, 61))
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:\n"
"rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        
        # Username field
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 240, 121, 16))
        self.label_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(430, 260, 421, 41))
        self.username.setObjectName("username")
        
        # First Name field
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(430, 310, 151, 16))
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        
        self.firstname = QtWidgets.QLineEdit(self.widget)
        self.firstname.setGeometry(QtCore.QRect(430, 330, 421, 41))
        self.firstname.setObjectName("firstname")
        
        # Last Name field
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(430, 380, 151, 16))
        self.label_5.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_5.setObjectName("label_5")
        
        self.lastname = QtWidgets.QLineEdit(self.widget)
        self.lastname.setGeometry(QtCore.QRect(430, 400, 421, 41))
        self.lastname.setObjectName("lastname")
        
        # Password field
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(430, 450, 151, 16))
        self.label_6.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_6.setObjectName("label_6")
        
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(430, 470, 421, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        
        # Confirm Password field
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(430, 520, 200, 16))
        self.label_7.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_7.setObjectName("label_7")
        
        self.confirmpassword = QtWidgets.QLineEdit(self.widget)
        self.confirmpassword.setGeometry(QtCore.QRect(430, 540, 421, 41))
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        
        # User Type radio buttons
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(430, 590, 151, 16))
        self.label_8.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_8.setObjectName("label_8")
        
        self.user_type_group = QtWidgets.QButtonGroup(Widget)
        
        self.admin_radio = QtWidgets.QRadioButton(self.widget)
        self.admin_radio.setGeometry(QtCore.QRect(430, 620, 100, 30))
        self.admin_radio.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.admin_radio.setObjectName("admin_radio")
        
        self.user_radio = QtWidgets.QRadioButton(self.widget)
        self.user_radio.setGeometry(QtCore.QRect(550, 620, 100, 30))
        self.user_radio.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.user_radio.setObjectName("user_radio")
        self.user_radio.setChecked(True)  # Default selection
        
        self.user_type_group.addButton(self.admin_radio)
        self.user_type_group.addButton(self.user_radio)
        
        # Create Account button
        self.create_button = QtWidgets.QPushButton(self.widget)
        self.create_button.setGeometry(QtCore.QRect(440, 680, 391, 61))
        self.create_button.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.create_button.setObjectName("create_button")
        
        # Back button
        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setGeometry(QtCore.QRect(190, 730, 161, 41))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.back_button.setObjectName("back_button")
        
        # Error message label
        self.error_label = QtWidgets.QLabel(self.widget)
        self.error_label.setGeometry(QtCore.QRect(430, 750, 421, 31))
        self.error_label.setStyleSheet("font: 75 italic 12pt \"Century Gothic\";color:red;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        
        # Connect the create button to create account function
        self.create_button.clicked.connect(self.create_account)
        self.back_button.clicked.connect(self.go_back)
        
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Create Account"))
        self.label.setText(_translate("Widget", "CREATE ACCOUNT"))
        self.label_2.setText(_translate("Widget", "Please fill in the details"))
        self.label_3.setText(_translate("Widget", "USERNAME"))
        self.label_4.setText(_translate("Widget", "FIRST NAME"))
        self.label_5.setText(_translate("Widget", "LAST NAME"))
        self.label_6.setText(_translate("Widget", "PASSWORD"))
        self.label_7.setText(_translate("Widget", "CONFIRM PASSWORD"))
        self.label_8.setText(_translate("Widget", "USER TYPE"))
        self.admin_radio.setText(_translate("Widget", "Admin"))
        self.user_radio.setText(_translate("Widget", "User"))
        self.create_button.setText(_translate("Widget", "CREATE ACCOUNT"))
        self.back_button.setText(_translate("Widget", "BACK"))
    
    def go_back(self):
        # Go back to welcome screen
        self.main_window.show_welcome_screen()
        
    def create_account(self):
        username = self.username.text()
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        password = self.password.text()
        confirm_password = self.confirmpassword.text()
        
        # Check if admin radio button is selected
        user_type = 1 if self.admin_radio.isChecked() else 0
        
        # Validate inputs
        if not username or not firstname or not lastname or not password or not confirm_password:
            self.error_label.setText("Please fill in all fields")
            return
            
        if password != confirm_password:
            self.error_label.setText("Passwords do not match")
            return
            
        # Create account in database
        user_code, error = self.database.create_account(username, firstname, lastname, password, confirm_password, user_type)
        
        if error:
            self.error_label.setText(error)
            return
            
        # Show success message
        QMessageBox.information(self.widget, "Success", "Account created successfully!")
        
        # Clear the form
        self.username.clear()
        self.firstname.clear()
        self.lastname.clear()
        self.password.clear()
        self.confirmpassword.clear()
        self.user_radio.setChecked(True)
        self.error_label.setText("")
        
        # Go back to login screen
        self.main_window.show_login_screen() 