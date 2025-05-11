from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class ViewOrganizationScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        self.load_organizations()
        
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
        self.label.setGeometry(QtCore.QRect(350, 50, 601, 91))
        self.label.setStyleSheet("font: 36pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        self.label.setText("VIEW ORGANIZATIONS")
        
        # Subtitle
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(430, 130, 451, 41))
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:\n"
"rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("List of all registered organizations")
        
        # Search section
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(190, 190, 121, 31))
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("SEARCH:")
        
        # Search field
        self.search_field = QtWidgets.QLineEdit(self.widget)
        self.search_field.setGeometry(QtCore.QRect(320, 190, 691, 31))
        self.search_field.setObjectName("search_field")
        
        # Apply filter button
        self.apply_filter = QtWidgets.QPushButton(self.widget)
        self.apply_filter.setGeometry(QtCore.QRect(1030, 190, 161, 31))
        self.apply_filter.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.apply_filter.setObjectName("apply_filter")
        self.apply_filter.setText("SEARCH")
        
        # Table widget for organizations
        self.org_table = QtWidgets.QTableWidget(self.widget)
        self.org_table.setGeometry(QtCore.QRect(190, 250, 921, 451))
        self.org_table.setObjectName("org_table")
        self.org_table.setColumnCount(4)
        self.org_table.setHorizontalHeaderLabels(["ID", "Organization Name", "Location", "Contact Person"])
        
        # Make columns stretch to fill available space
        header = self.org_table.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        # Back button
        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setGeometry(QtCore.QRect(190, 730, 161, 41))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("BACK")
        
        # Connect the buttons to their functions
        self.apply_filter.clicked.connect(self.apply_search)
        self.back_button.clicked.connect(self.go_back)
        
    def load_organizations(self):
        """Load organizations from database into the table"""
        if not self.user:
            return
            
        # Get search term
        search_term = self.search_field.text() if self.search_field.text() else None
        
        # Get organizations
        organizations = self.database.get_all_organizations(search_term)
        
        # Clear the table
        self.org_table.setRowCount(0)
        
        # Populate the table
        row = 0
        for org in organizations:
            org_id = org[0]
            org_name = org[1]
            location = org[2]
            contact_person = org[3]
                
            self.org_table.insertRow(row)
            self.org_table.setItem(row, 0, QTableWidgetItem(str(org_id)))
            self.org_table.setItem(row, 1, QTableWidgetItem(org_name))
            self.org_table.setItem(row, 2, QTableWidgetItem(location))
            self.org_table.setItem(row, 3, QTableWidgetItem(contact_person))
            row += 1
            
    def apply_search(self):
        """Apply search filter to organizations table"""
        self.load_organizations()
    
    def go_back(self):
        """Go back to the main menu"""
        self.main_window.show_admin_menu(self.user) 