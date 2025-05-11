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
        
        # Apply initial resizing
        Widget.resizeEvent = self.handle_resize_event
        
    def handle_resize_event(self, event):
        """Handle resize events for this widget"""
        # Call parent resizeEvent
        QtWidgets.QWidget.resizeEvent(self.widget.parent(), event)
        
        # Resize main widget to fill the entire parent
        if self.widget.parent():
            parent_width = self.widget.parent().width()
            parent_height = self.widget.parent().height()
            
            # Resize the main widget to fill the window
            self.widget.setGeometry(0, 0, parent_width, parent_height)
            
            # Center the title labels
            center_x = int(parent_width / 2)
            self.label.setGeometry(QtCore.QRect(int(center_x - 370), 60, 741, 171))
            self.label_2.setGeometry(QtCore.QRect(int(center_x - 225), 170, 451, 61))
            
            # Form width remains fixed, but centered
            form_width = 421
            form_x = int(center_x - form_width / 2)
            
            # Username field
            self.label_3.setGeometry(QtCore.QRect(form_x, 240, 121, 16))
            self.username.setGeometry(QtCore.QRect(form_x, 260, form_width, 41))
            
            # First Name field
            self.label_4.setGeometry(QtCore.QRect(form_x, 310, 151, 16))
            self.firstname.setGeometry(QtCore.QRect(form_x, 330, form_width, 41))
            
            # Last Name field
            self.label_5.setGeometry(QtCore.QRect(form_x, 380, 151, 16))
            self.lastname.setGeometry(QtCore.QRect(form_x, 400, form_width, 41))
            
            # Password field
            self.label_6.setGeometry(QtCore.QRect(form_x, 450, 151, 16))
            self.password.setGeometry(QtCore.QRect(form_x, 470, form_width, 41))
            
            # Confirm Password field
            self.label_7.setGeometry(QtCore.QRect(form_x, 520, 200, 16))
            self.confirmpassword.setGeometry(QtCore.QRect(form_x, 540, form_width, 41))
            
            # User Type radio buttons
            self.label_8.setGeometry(QtCore.QRect(form_x, 590, 151, 16))
            self.admin_radio.setGeometry(QtCore.QRect(form_x, 620, 100, 30))
            self.user_radio.setGeometry(QtCore.QRect(form_x + 120, 620, 100, 30))
            
            # Create Account button
            button_width = 391
            self.create_button.setGeometry(QtCore.QRect(int(center_x - button_width/2), 680, button_width, 61))
            
            # Calculate margin for left side
            margin_x = max(50, int((parent_width - 1100) / 2))
            
            # Back button - keep it on the left side with proper margin
            back_button_y = parent_height - 80  # Fixed distance from bottom
            self.back_button.setGeometry(QtCore.QRect(margin_x, back_button_y, 161, 41))
            
            # Error message label - center under create button
            self.error_label.setGeometry(QtCore.QRect(int(center_x - form_width/2), 750, form_width, 31))
        
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