from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFormLayout

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
        
        # Main widget with background - fill the entire parent widget
        self.widget = QtWidgets.QWidget(Widget)
        
        # Use a layout for the parent Widget to ensure the background fills everything
        layout = QVBoxLayout(Widget)
        layout.setContentsMargins(0, 0, 0, 0)  # No margins to ensure full coverage
        layout.setSpacing(0)
        layout.addWidget(self.widget)
        
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:rgb(158, 198, 243);}")
        self.widget.setObjectName("widget")
        
        # Main layout for the widget
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(60, 40, 60, 40)
        self.main_layout.setSpacing(20)
        
        # Title area
        self.title_layout = QVBoxLayout()
        self.title_layout.setAlignment(QtCore.Qt.AlignCenter)
        
        # Title
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("font: 36pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        self.label.setText("EDIT PERSONAL INFORMATION")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_layout.addWidget(self.label)
        
        # Subtitle
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Update your account information")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_layout.addWidget(self.label_2)
        
        # Add title section to main layout
        self.main_layout.addLayout(self.title_layout)
        
        # Form layout - this centers the form horizontally
        self.form_container = QHBoxLayout()
        self.form_container.addStretch()
        
        self.form_layout = QVBoxLayout()
        self.form_layout.setSpacing(15)
        
        # Username field
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("USERNAME")
        self.form_layout.addWidget(self.label_3)
        
        self.username = QtWidgets.QLineEdit()
        self.username.setMinimumSize(QtCore.QSize(400, 41))
        self.username.setMaximumSize(QtCore.QSize(500, 41))
        self.username.setObjectName("username")
        self.form_layout.addWidget(self.username)
        
        # First Name field
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("FIRST NAME")
        self.form_layout.addWidget(self.label_4)
        
        self.firstname = QtWidgets.QLineEdit()
        self.firstname.setMinimumSize(QtCore.QSize(400, 41))
        self.firstname.setMaximumSize(QtCore.QSize(500, 41))
        self.firstname.setObjectName("firstname")
        self.form_layout.addWidget(self.firstname)
        
        # Last Name field
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LAST NAME")
        self.form_layout.addWidget(self.label_5)
        
        self.lastname = QtWidgets.QLineEdit()
        self.lastname.setMinimumSize(QtCore.QSize(400, 41))
        self.lastname.setMaximumSize(QtCore.QSize(500, 41))
        self.lastname.setObjectName("lastname")
        self.form_layout.addWidget(self.lastname)
        
        # Password field
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("PASSWORD")
        self.form_layout.addWidget(self.label_6)
        
        self.password = QtWidgets.QLineEdit()
        self.password.setMinimumSize(QtCore.QSize(400, 41))
        self.password.setMaximumSize(QtCore.QSize(500, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.form_layout.addWidget(self.password)
        
        # Confirm Password field
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("CONFIRM PASSWORD")
        self.form_layout.addWidget(self.label_7)
        
        self.confirmpassword = QtWidgets.QLineEdit()
        self.confirmpassword.setMinimumSize(QtCore.QSize(400, 41))
        self.confirmpassword.setMaximumSize(QtCore.QSize(500, 41))
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.form_layout.addWidget(self.confirmpassword)
        
        # Add spacing before button
        self.form_layout.addSpacing(20)
        
        # Update button - centered
        self.update_button_layout = QHBoxLayout()
        self.update_button_layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.update_button = QtWidgets.QPushButton()
        self.update_button.setMinimumSize(QtCore.QSize(391, 61))
        self.update_button.setMaximumSize(QtCore.QSize(500, 61))
        self.update_button.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.update_button.setObjectName("update_button")
        self.update_button.setText("UPDATE INFORMATION")
        self.update_button_layout.addWidget(self.update_button)
        
        self.form_layout.addLayout(self.update_button_layout)
        
        # Error message label - centered
        self.error_label = QtWidgets.QLabel()
        self.error_label.setStyleSheet("font: 75 italic 12pt \"Century Gothic\";color:red;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.form_layout.addWidget(self.error_label)
        
        # Add form to the container with stretching on both sides for centering
        self.form_container.addLayout(self.form_layout)
        self.form_container.addStretch()
        
        # Add form container to main layout
        self.main_layout.addLayout(self.form_container)
        
        # Add spacer to push back button to bottom
        self.main_layout.addStretch()
        
        # Back button (bottom-left)
        self.back_layout = QHBoxLayout()
        
        self.back_button = QtWidgets.QPushButton()
        self.back_button.setMinimumSize(QtCore.QSize(161, 41))
        self.back_button.setMaximumSize(QtCore.QSize(161, 41))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("BACK")
        self.back_layout.addWidget(self.back_button)
        
        # Add spacer to push back button to left
        self.back_layout.addStretch()
        
        # Add back button layout to main layout
        self.main_layout.addLayout(self.back_layout)
        
        # Connect buttons to functions
        self.update_button.clicked.connect(self.update_user_info)
        self.back_button.clicked.connect(self.go_back)
        
        # Set minimum size to ensure all content is visible
        Widget.setMinimumSize(1000, 700)
    
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