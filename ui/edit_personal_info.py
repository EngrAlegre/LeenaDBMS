from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class EditPersonalInfoScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        self.load_user_data()
        
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1301, 811)
        
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1301, 811))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:rgb(158, 198, 243);}")
        self.widget.setObjectName("widget")
        
        # Title
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(270, 80, 851, 101))
        self.label.setStyleSheet("font: 36pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        self.label.setText("EDIT PERSONAL INFORMATION")
        
        # Subtitle
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(450, 170, 451, 41))
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:\n"
"rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Update your account information")
        
        # Username field
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 250, 121, 16))
        self.label_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("USERNAME")
        
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(430, 270, 421, 41))
        self.username.setObjectName("username")
        
        # First Name field
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(430, 330, 151, 16))
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("FIRST NAME")
        
        self.firstname = QtWidgets.QLineEdit(self.widget)
        self.firstname.setGeometry(QtCore.QRect(430, 350, 421, 41))
        self.firstname.setObjectName("firstname")
        
        # Last Name field
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(430, 410, 151, 16))
        self.label_5.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LAST NAME")
        
        self.lastname = QtWidgets.QLineEdit(self.widget)
        self.lastname.setGeometry(QtCore.QRect(430, 430, 421, 41))
        self.lastname.setObjectName("lastname")
        
        # Password field
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(430, 490, 151, 16))
        self.label_6.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("PASSWORD")
        
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(430, 510, 421, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        
        # Confirm Password field
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(430, 570, 200, 16))
        self.label_7.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("CONFIRM PASSWORD")
        
        self.confirmpassword = QtWidgets.QLineEdit(self.widget)
        self.confirmpassword.setGeometry(QtCore.QRect(430, 590, 421, 41))
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        
        # Update button
        self.update_button = QtWidgets.QPushButton(self.widget)
        self.update_button.setGeometry(QtCore.QRect(440, 660, 391, 61))
        self.update_button.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.update_button.setObjectName("update_button")
        self.update_button.setText("UPDATE INFORMATION")
        
        # Back button
        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setGeometry(QtCore.QRect(190, 730, 161, 41))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("BACK")
        
        # Error message label
        self.error_label = QtWidgets.QLabel(self.widget)
        self.error_label.setGeometry(QtCore.QRect(440, 730, 391, 31))
        self.error_label.setStyleSheet("font: 75 italic 12pt \"Century Gothic\";color:red;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        
        # Connect buttons to functions
        self.update_button.clicked.connect(self.update_user_info)
        self.back_button.clicked.connect(self.go_back)
    
    def load_user_data(self):
        """Load user data from the database into the form fields"""
        if not self.user:
            return
            
        self.username.setText(self.user[1])  # username
        self.firstname.setText(self.user[2])  # firstname
        self.lastname.setText(self.user[3])  # lastname
        self.password.setText(self.user[4])  # password
        self.confirmpassword.setText(self.user[5])  # confirm password
    
    def update_user_info(self):
        """Update user information in the database"""
        username = self.username.text()
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        password = self.password.text()
        confirm_password = self.confirmpassword.text()
        
        # Validate inputs
        if not username or not firstname or not lastname or not password or not confirm_password:
            self.error_label.setText("Please fill in all fields")
            return
            
        if password != confirm_password:
            self.error_label.setText("Passwords do not match")
            return
        
        # Update user in database
        success, error = self.database.update_user(self.user[0], username, firstname, lastname, password)
        
        if not success:
            self.error_label.setText(error)
            return
            
        # Show success message
        QMessageBox.information(self.widget, "Success", "Information updated successfully!")
        
        # Update the user object with new data
        self.user = self.database.get_user_by_id(self.user[0])
        
        # Go back to the appropriate menu
        self.go_back()
    
    def go_back(self):
        """Go back to the appropriate menu based on user type"""
        if self.user[6]:  # User is admin
            self.main_window.show_admin_menu(self.user)
        else:
            self.main_window.show_user_menu(self.user) 