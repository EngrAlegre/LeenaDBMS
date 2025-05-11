from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QGridLayout

class AdminMainMenu(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1287, 810)
        
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
        
        # Main layout for the widget - using a Grid Layout for better control
        self.main_layout = QGridLayout(self.widget)
        self.main_layout.setContentsMargins(60, 30, 60, 30)
        
        # Column stretching to maintain proportions
        # Left sidebar (column 0) gets minimum width, columns 1-3 get equal stretch
        self.main_layout.setColumnStretch(0, 1)  # Left sidebar
        self.main_layout.setColumnStretch(1, 3)  # CREATE column
        self.main_layout.setColumnStretch(2, 3)  # DELETE/EDIT column
        self.main_layout.setColumnStretch(3, 3)  # VIEW/ORG column
        
        # Row stretching to maintain proportions
        self.main_layout.setRowStretch(0, 1)  # Header row
        self.main_layout.setRowStretch(1, 2)  # First button row
        self.main_layout.setRowStretch(2, 2)  # Second button row
        self.main_layout.setRowStretch(3, 1)  # EDIT header
        self.main_layout.setRowStretch(4, 2)  # EDIT product row
        self.main_layout.setRowStretch(5, 2)  # EDIT delivery row
        self.main_layout.setRowStretch(6, 1)  # Footer row
        
        # CREATE header
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setStyleSheet("font: 24pt \"Century Gothic\";\n"
"color:rgb(0,0,0)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("CREATE")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label_2, 0, 1)
        
        # DELETE header
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setStyleSheet("font: 24pt \"Century Gothic\";\n"
"color:rgb(0,0,0)")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("DELETE")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label_5, 0, 2)
        
        # VIEW header
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setStyleSheet("font: 24pt \"Century Gothic\";\n"
"color:rgb(0,0,0)")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("VIEW")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label_7, 0, 3)
        
        # What do you want to do? label
        self.label_what = QtWidgets.QLabel()
        self.label_what.setStyleSheet("font: 16pt \"Century Gothic\";\n"
"color:rgb(71, 84, 111)")
        self.label_what.setObjectName("label_what")
        self.label_what.setText("What do you want to do?")
        self.label_what.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.main_layout.addWidget(self.label_what, 2, 0)
        
        # Logout button at bottom left
        self.logout_btn = QtWidgets.QPushButton()
        self.logout_btn.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.setText("LOGOUT")
        self.logout_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.logout_btn.setMaximumSize(QtCore.QSize(161, 41))
        self.main_layout.addWidget(self.logout_btn, 6, 0, QtCore.Qt.AlignLeft)
        
        # CREATE buttons
        self.p2 = QtWidgets.QPushButton()
        self.p2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.p2.setObjectName("p2")
        self.p2.setText("PRODUCTS")
        self.p2.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.p2, 1, 1)
        
        self.d2 = QtWidgets.QPushButton()
        self.d2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.d2.setObjectName("d2")
        self.d2.setText("DELIVERY")
        self.d2.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.d2, 2, 1)
        
        # DELETE buttons
        self.p1 = QtWidgets.QPushButton()
        self.p1.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(200, 220, 240);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid rgb(76, 107, 140)")
        self.p1.setObjectName("p1")
        self.p1.setText("PRODUCTS")
        self.p1.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.p1, 1, 2)
        
        self.d1 = QtWidgets.QPushButton()
        self.d1.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(200, 220, 240);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid rgb(76, 107, 140)")
        self.d1.setObjectName("d1")
        self.d1.setText("DELIVERY")
        self.d1.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.d1, 2, 2)
        
        # VIEW buttons
        self.p1_2 = QtWidgets.QPushButton()
        self.p1_2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.p1_2.setObjectName("p1_2")
        self.p1_2.setText("PRODUCTS")
        self.p1_2.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.p1_2, 1, 3)
        
        self.d2_2 = QtWidgets.QPushButton()
        self.d2_2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.d2_2.setObjectName("d2_2")
        self.d2_2.setText("DELIVERY")
        self.d2_2.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.d2_2, 2, 3)
        
        # EDIT section title 
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setStyleSheet("font: 24pt \"Century Gothic\";\n"
"color:rgb(0,0,0)")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("EDIT")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label_4, 3, 2)
        
        # EDIT buttons
        self.p3 = QtWidgets.QPushButton()
        self.p3.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(254, 255, 180);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.p3.setObjectName("p3")
        self.p3.setText("PRODUCTS")
        self.p3.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.p3, 4, 2)
        
        self.d3 = QtWidgets.QPushButton()
        self.d3.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(254, 255, 180);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.d3.setObjectName("d3")
        self.d3.setText("DELIVERY")
        self.d3.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.d3, 5, 2)
        
        # Organization view button
        self.o3 = QtWidgets.QPushButton()
        self.o3.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.o3.setObjectName("o3")
        self.o3.setText("ORGANIZATION")
        self.o3.setMinimumSize(QtCore.QSize(180, 100))
        self.main_layout.addWidget(self.o3, 4, 3)
        
        # Credits at bottom right
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setStyleSheet("color:rgb(154, 211, 209);")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("GRP 3; Aradanas, Delavin, Oracion, Santos Ma")
        self.main_layout.addWidget(self.label_3, 6, 3, QtCore.Qt.AlignRight)
        
        # Connect all buttons to their respective functions
        self.p2.clicked.connect(self.open_add_products)
        self.d2.clicked.connect(self.open_add_delivery)
        self.p1.clicked.connect(self.open_delete_products)
        self.d1.clicked.connect(self.open_delete_delivery)
        self.p3.clicked.connect(self.open_edit_products)
        self.d3.clicked.connect(self.open_edit_delivery)
        self.p1_2.clicked.connect(self.open_view_products)
        self.d2_2.clicked.connect(self.open_view_delivery)
        self.o3.clicked.connect(self.open_view_organization)
        self.logout_btn.clicked.connect(self.logout)
        
        # Handle window resize events
        Widget.resizeEvent = self.on_resize
        
    def on_resize(self, event):
        """Handle window resize events"""
        # This method is called when the window is resized
        # The layouts will automatically adjust the widgets
        # No need to call super as we're not a true QWidget subclass
        pass
    
    def logout(self):
        # Go back to welcome screen
        self.main_window.show_welcome_screen()
    
    def open_add_products(self):
        self.main_window.show_add_products(self.user)
    
    def open_add_delivery(self):
        self.main_window.show_add_delivery(self.user)
    
    def open_delete_products(self):
        self.main_window.show_delete_products(self.user)
    
    def open_delete_delivery(self):
        self.main_window.show_delete_delivery(self.user)
    
    def open_edit_products(self):
        self.main_window.show_edit_products(self.user)
    
    def open_edit_delivery(self):
        self.main_window.show_edit_delivery(self.user)
    
    def open_view_products(self):
        self.main_window.show_view_products(self.user)
    
    def open_view_delivery(self):
        self.main_window.show_view_delivery(self.user)
    
    def open_view_organization(self):
        self.main_window.show_view_organization(self.user) 