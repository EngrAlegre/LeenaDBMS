from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QGridLayout

class UserMainMenu(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        # Print user info for debugging
        print(f"UserMenu - set_user called with user: {user}")
        
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1300, 800)
        
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
        
        # Main layout for the widget - using a vertical box layout for simpler centering
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(60, 60, 60, 60)
        self.main_layout.setSpacing(30)
        
        # Title in the center at top
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("font: 30pt \"Century Gothic\"; color:rgb(0,0,0)")
        self.label.setObjectName("label")
        self.label.setText("WHAT WOULD YOU LIKE TO DO?")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label)
        
        # Add spacing after title
        self.main_layout.addSpacing(40)
        
        # Center container for menu options
        self.center_container = QVBoxLayout()
        self.center_container.setSpacing(30)
        self.center_container.setAlignment(QtCore.Qt.AlignCenter)
        
        # Grid layout for better alignment of labels and buttons
        self.menu_grid = QtWidgets.QGridLayout()
        self.menu_grid.setHorizontalSpacing(40)
        self.menu_grid.setVerticalSpacing(30)
        
        # Organization row
        # Organization label
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("ORGANIZATION")
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_4.setMinimumWidth(250)
        self.menu_grid.addWidget(self.label_4, 0, 0)
        
        # Edit Personal Information button
        self.view2 = QtWidgets.QPushButton()
        self.view2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.view2.setObjectName("view2")
        self.view2.setText("EDIT PERSONAL INFORMATION")
        self.view2.setMinimumSize(QtCore.QSize(400, 61))
        self.view2.setMaximumSize(QtCore.QSize(600, 61))
        self.menu_grid.addWidget(self.view2, 0, 1)
        
        # Delivery row
        # Delivery label
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("DELIVERY")
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_5.setMinimumWidth(250)
        self.menu_grid.addWidget(self.label_5, 1, 0)
        
        # View Delivery button
        self.view3 = QtWidgets.QPushButton()
        self.view3.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(200, 220, 240);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid rgb(76, 107, 140)")
        self.view3.setObjectName("view3")
        self.view3.setText("VIEW")
        self.view3.setMinimumSize(QtCore.QSize(281, 61))
        self.view3.setMaximumSize(QtCore.QSize(400, 61))
        self.menu_grid.addWidget(self.view3, 1, 1)
        
        # Center the grid in the window
        self.center_grid_container = QHBoxLayout()
        self.center_grid_container.addStretch(1)
        self.center_grid_container.addLayout(self.menu_grid)
        self.center_grid_container.addStretch(1)
        
        # Add the centered grid to the center container
        self.center_container.addLayout(self.center_grid_container)
        
        # Add center container to main layout
        self.main_layout.addLayout(self.center_container)
        
        # Add spacer to push logout to bottom
        self.main_layout.addStretch()
        
        # Create bottom row for logout button
        self.bottom_layout = QHBoxLayout()
        
        # Logout button
        self.logout_btn = QtWidgets.QPushButton()
        self.logout_btn.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.setText("LOGOUT")
        self.logout_btn.setMinimumSize(QtCore.QSize(161, 41))
        self.logout_btn.setMaximumSize(QtCore.QSize(161, 41))
        self.bottom_layout.addWidget(self.logout_btn)
        
        # Add stretch to push logout to left
        self.bottom_layout.addStretch()
        
        # Add bottom row to main layout
        self.main_layout.addLayout(self.bottom_layout)
        
        # Connect buttons to their respective functions
        self.view2.clicked.connect(self.open_edit_personal_info)
        self.view3.clicked.connect(self.open_view_delivery)
        self.logout_btn.clicked.connect(self.logout)
        
        # Set minimum size to ensure all content is visible
        Widget.setMinimumSize(1000, 600)

    def logout(self):
        # Go back to welcome screen
        self.main_window.show_welcome_screen()
        
    def open_edit_personal_info(self):
        # Store the current user_id for fetching fresh data when returning
        if self.user:
            self.user_id = self.user[0]
            print(f"Storing user_id {self.user_id} before edit screen")
        self.main_window.show_edit_personal_info(self.user)
        
    def open_view_delivery(self):
        self.main_window.show_view_delivery_user(self.user) 