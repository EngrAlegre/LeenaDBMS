from PyQt5 import QtCore, QtGui, QtWidgets

class UserMainMenu(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(842, 595)
        
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1161, 691))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:rgb(158, 198, 243);}")
        self.widget.setObjectName("widget")
        
        # Credits label
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(1040, 770, 231, 16))
        self.label_3.setStyleSheet("color:rgb(154, 211, 209);")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("GRP 3; Aradanas, Delavin, Oracion, Santos Ma")
        
        # Main title label
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(220, 60, 441, 91))
        self.label.setStyleSheet("font: 20pt \"Century Gothic\"; color:rgb(0,0,0)\n")
        self.label.setObjectName("label")
        self.label.setText("WHAT WOULD YOU LIKE TO DO?")
        
        # Organization label
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 231, 41))
        self.label_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("ORGANIZATION")
        
        # Delivery label
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 320, 151, 41))
        self.label_5.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("DELIVERY")
        
        # Edit Personal Information button
        self.view2 = QtWidgets.QPushButton(self.widget)
        self.view2.setGeometry(QtCore.QRect(400, 200, 391, 61))
        self.view2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.view2.setObjectName("view2")
        self.view2.setText("EDIT PERSONAL INFORMATION")
        
        # View Delivery button
        self.view3 = QtWidgets.QPushButton(self.widget)
        self.view3.setGeometry(QtCore.QRect(440, 310, 281, 61))
        self.view3.setStyleSheet("border-radius: 20px;\n"
"background-color:rgbrgb(247, 207, 216);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid grey\n")
        self.view3.setObjectName("view3")
        self.view3.setText("VIEW")
        
        # Logout button
        self.logout_btn = QtWidgets.QPushButton(self.widget)
        self.logout_btn.setGeometry(QtCore.QRect(60, 520, 161, 41))
        self.logout_btn.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.setText("LOGOUT")
        
        # Connect buttons to their respective functions
        self.view2.clicked.connect(self.open_edit_personal_info)
        self.view3.clicked.connect(self.open_view_delivery)
        self.logout_btn.clicked.connect(self.logout)
    
    def logout(self):
        # Go back to welcome screen
        self.main_window.show_welcome_screen()
        
    def open_edit_personal_info(self):
        self.main_window.show_edit_personal_info(self.user)
        
    def open_view_delivery(self):
        self.main_window.show_view_delivery_user(self.user) 