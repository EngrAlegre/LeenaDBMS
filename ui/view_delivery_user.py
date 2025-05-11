from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class ViewDeliveryUserScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        
    def set_user(self, user):
        self.user = user
        self.load_deliveries()
        
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
        self.label.setGeometry(QtCore.QRect(430, 50, 441, 91))
        self.label.setStyleSheet("font: 36pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        self.label.setText("VIEW DELIVERIES")
        
        # Subtitle
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(430, 130, 451, 41))
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:\n"
"rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Deliveries assigned to your organization")
        
        # Filter section
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(190, 190, 121, 31))
        self.label_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("FILTER BY:")
        
        # Filter combobox
        self.filter_combo = QtWidgets.QComboBox(self.widget)
        self.filter_combo.setGeometry(QtCore.QRect(320, 190, 251, 31))
        self.filter_combo.setObjectName("filter_combo")
        self.filter_combo.addItem("All")
        self.filter_combo.addItem("Upcoming")
        self.filter_combo.addItem("Past")
        
        # Search section
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(610, 190, 121, 31))
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("SEARCH:")
        
        # Search field
        self.search_field = QtWidgets.QLineEdit(self.widget)
        self.search_field.setGeometry(QtCore.QRect(730, 190, 381, 31))
        self.search_field.setObjectName("search_field")
        
        # Apply filter button
        self.apply_filter = QtWidgets.QPushButton(self.widget)
        self.apply_filter.setGeometry(QtCore.QRect(950, 230, 161, 31))
        self.apply_filter.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.apply_filter.setObjectName("apply_filter")
        self.apply_filter.setText("APPLY FILTER")
        
        # Table widget for deliveries
        self.delivery_table = QtWidgets.QTableWidget(self.widget)
        self.delivery_table.setGeometry(QtCore.QRect(190, 280, 921, 421))
        self.delivery_table.setObjectName("delivery_table")
        self.delivery_table.setColumnCount(5)
        self.delivery_table.setHorizontalHeaderLabels(["ID", "Delivery Time", "Date", "Location", "Food List"])
        
        # Make columns stretch to fill available space
        header = self.delivery_table.horizontalHeader()
        for i in range(5):
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
        self.apply_filter.clicked.connect(self.apply_filters)
        self.back_button.clicked.connect(self.go_back)
        
    def load_deliveries(self):
        """Load deliveries from the database based on the user organization"""
        if not self.user:
            return
            
        # Get the organization ID for this user
        org_id = None
        orgs = self.database.get_all_organizations()
        for org in orgs:
            if org[3] == f"{self.user[2]} {self.user[3]}":  # Check if contact person matches user's name
                org_id = org[0]
                break
                
        if not org_id:
            return  # No organization found for this user
        
        # Get filter values
        filter_by = self.filter_combo.currentText().lower() if self.filter_combo.currentText() != "All" else None
        search_term = self.search_field.text() if self.search_field.text() else None
        
        # Get deliveries for this organization
        deliveries = self.database.get_deliveries_by_org(org_id, filter_by)
        
        # Clear the table
        self.delivery_table.setRowCount(0)
        
        # Populate the table
        row = 0
        for delivery in deliveries:
            # The database structure is incorrect - date and foodList_id are swapped:
            # delivery[0] = delivery_id
            # delivery[1] = departure_time
            # delivery[2] = date (currently None)
            # delivery[3] = foodList_id (actually contains the date)
            # delivery[4] = location_id
            # delivery[5] = org_id
            # delivery[6] = food_list_name
            # delivery[7] = org_name
            # delivery[8] = location_name
            
            delivery_id = delivery[0]
            departure_time = delivery[1] if delivery[1] else "N/A"
            
            # Handle the swapped date and foodList_id fields
            date = delivery[3] if isinstance(delivery[3], str) and "-" in delivery[3] else "None"  # Date is in foodList_id field
            food_list_id = delivery[2] if isinstance(delivery[2], int) else (int(delivery[2]) if delivery[2] and delivery[2].isdigit() else None)
            
            location = delivery[8]  # Location name is at index 8
            food_list = delivery[6]  # Food list name is at index 6
            
            # If search term is specified, filter results
            if search_term and search_term.lower() not in str(food_list).lower() and search_term.lower() not in str(location).lower():
                continue
                
            self.delivery_table.insertRow(row)
            self.delivery_table.setItem(row, 0, QTableWidgetItem(str(delivery_id)))
            self.delivery_table.setItem(row, 1, QTableWidgetItem(str(departure_time)))
            self.delivery_table.setItem(row, 2, QTableWidgetItem(str(date)))
            self.delivery_table.setItem(row, 3, QTableWidgetItem(str(location)))
            self.delivery_table.setItem(row, 4, QTableWidgetItem(str(food_list)))
            row += 1
            
    def apply_filters(self):
        """Apply filters to the deliveries table"""
        self.load_deliveries()
    
    def go_back(self):
        """Go back to the main menu"""
        self.main_window.show_user_menu(self.user) 