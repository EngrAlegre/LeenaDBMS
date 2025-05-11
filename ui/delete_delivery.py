from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from ui.styles import *

class DeleteDeliveryScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        self.selected_delivery_id = None
        
    def set_user(self, user):
        self.user = user
        self.load_deliveries()
        
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
        
        self.widget.setStyleSheet(MAIN_BG_STYLE)
        self.widget.setObjectName("widget")
        
        # Main layout for the content
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(60, 30, 60, 30)
        
        # Title area
        self.title_layout = QHBoxLayout()
        self.title_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Title
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet(TITLE_STYLE)
        self.label.setObjectName("label")
        self.label.setText("DELETE DELIVERY")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.title_layout.addWidget(self.label)
        self.title_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.main_layout.addLayout(self.title_layout)
        
        # Subtitle
        self.subtitle_layout = QHBoxLayout()
        self.subtitle_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setStyleSheet(SUBTITLE_STYLE)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Select a delivery to delete")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.subtitle_layout.addWidget(self.label_2)
        self.subtitle_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.main_layout.addLayout(self.subtitle_layout)
        
        # Filter and search area
        self.filter_search_layout = QHBoxLayout()
        self.filter_search_layout.setContentsMargins(0, 10, 0, 10)
        self.filter_search_layout.setSpacing(10)
        
        # Filter section
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setStyleSheet(LABEL_STYLE)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("FILTER BY:")
        self.label_3.setMinimumWidth(100)
        self.label_3.setMaximumWidth(100)
        self.filter_search_layout.addWidget(self.label_3)
        
        # Filter combobox
        self.filter_combo = QtWidgets.QComboBox()
        self.filter_combo.setMinimumWidth(150)
        self.filter_combo.setMaximumWidth(250)
        self.filter_combo.setMinimumHeight(35)
        self.filter_combo.setStyleSheet(COMBOBOX_STYLE)
        self.filter_combo.setObjectName("filter_combo")
        self.filter_combo.addItem("All")
        self.filter_combo.addItem("Upcoming")
        self.filter_combo.addItem("Past")
        self.filter_search_layout.addWidget(self.filter_combo)
        
        # Add spacing between filter and search
        self.filter_search_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))
        
        # Search section
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setStyleSheet(LABEL_STYLE)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("SEARCH:")
        self.label_4.setMinimumWidth(80)
        self.label_4.setMaximumWidth(80)
        self.filter_search_layout.addWidget(self.label_4)
        
        # Search field
        self.search_field = QtWidgets.QLineEdit()
        self.search_field.setMinimumHeight(35)
        self.search_field.setStyleSheet(INPUT_STYLE)
        self.search_field.setObjectName("search_field")
        self.filter_search_layout.addWidget(self.search_field, 1)  # 1 is stretch factor
        
        self.main_layout.addLayout(self.filter_search_layout)
        
        # Add spacing before table
        self.main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Table widget for deliveries
        self.delivery_table = QtWidgets.QTableWidget()
        self.delivery_table.setMinimumHeight(300)
        self.delivery_table.setStyleSheet(TABLE_STYLE)
        self.delivery_table.setObjectName("delivery_table")
        self.delivery_table.setColumnCount(6)
        self.delivery_table.setHorizontalHeaderLabels(["ID", "Delivery Time", "Date", "Location", "Organization", "Food List"])
        
        # Make columns stretch to fill available space
        header = self.delivery_table.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        self.main_layout.addWidget(self.delivery_table, 1)  # 1 is stretch factor
        
        # Add spacing before selection box
        self.main_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Selection box with background
        self.selection_box = QtWidgets.QGroupBox()
        self.selection_box.setMinimumHeight(50)
        self.selection_box.setStyleSheet(SELECTION_BOX_STYLE)
        self.selection_box.setTitle("")
        self.selection_box.setObjectName("selection_box")
        
        # Layout for selection box
        self.selection_box_layout = QHBoxLayout(self.selection_box)
        self.selection_box_layout.setContentsMargins(10, 5, 10, 5)
        
        # Selected delivery info
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setStyleSheet(LABEL_BOLD_STYLE)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("SELECTED DELIVERY:")
        self.selection_box_layout.addWidget(self.label_5)
        
        self.selected_delivery_label = QtWidgets.QLabel()
        self.selected_delivery_label.setStyleSheet("font: 12pt \"Century Gothic\"; color: rgb(76, 107, 140)")
        self.selected_delivery_label.setObjectName("selected_delivery_label")
        self.selected_delivery_label.setText("None")
        self.selection_box_layout.addWidget(self.selected_delivery_label, 1)
        
        self.main_layout.addWidget(self.selection_box)
        
        # Add spacing before buttons
        self.main_layout.addItem(QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Buttons area
        self.buttons_layout = QHBoxLayout()
        
        # Back button (left-aligned)
        self.back_button = QtWidgets.QPushButton()
        self.back_button.setMinimumSize(QtCore.QSize(161, 41))
        self.back_button.setMaximumSize(QtCore.QSize(161, 41))
        self.back_button.setStyleSheet(SECONDARY_BUTTON_STYLE)
        self.back_button.setObjectName("back_button")
        self.back_button.setText("BACK")
        self.buttons_layout.addWidget(self.back_button)
        
        # Add spacer to push delete button to center
        self.buttons_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Delete button (center-aligned)
        self.delete_button = QtWidgets.QPushButton()
        self.delete_button.setMinimumSize(QtCore.QSize(191, 61))
        self.delete_button.setMaximumSize(QtCore.QSize(250, 61))
        self.delete_button.setStyleSheet(DELETE_BUTTON_STYLE)
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setText("DELETE")
        self.buttons_layout.addWidget(self.delete_button)
        
        # Add spacer for symmetry
        self.buttons_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        self.main_layout.addLayout(self.buttons_layout)
        
        # Connect the buttons to their functions
        self.filter_combo.currentTextChanged.connect(self.load_deliveries)
        self.search_field.textChanged.connect(self.load_deliveries)
        self.back_button.clicked.connect(self.go_back)
        self.delete_button.clicked.connect(self.delete_delivery)
        self.delivery_table.itemSelectionChanged.connect(self.on_selection_change)
        
    def load_deliveries(self):
        """Load deliveries from the database"""
        if not self.user:
            return
            
        # Get filter values
        filter_by = self.filter_combo.currentText().lower() if self.filter_combo.currentText() != "All" else None
        search_term = self.search_field.text() if self.search_field.text() else None
        
        # Get deliveries
        deliveries = self.database.get_all_deliveries(filter_by, search_term)
        
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
            organization = delivery[7]  # Organization name is at index 7
            food_list = delivery[6]  # Food list name is at index 6
                
            self.delivery_table.insertRow(row)
            self.delivery_table.setItem(row, 0, QTableWidgetItem(str(delivery_id)))
            self.delivery_table.setItem(row, 1, QTableWidgetItem(str(departure_time)))
            self.delivery_table.setItem(row, 2, QTableWidgetItem(str(date)))
            self.delivery_table.setItem(row, 3, QTableWidgetItem(str(location)))
            self.delivery_table.setItem(row, 4, QTableWidgetItem(str(organization)))
            self.delivery_table.setItem(row, 5, QTableWidgetItem(str(food_list)))
            row += 1
            
    def on_selection_change(self):
        """Handle selection changes in the table"""
        selected_rows = self.delivery_table.selectedItems()
        if selected_rows:
            row = selected_rows[0].row()
            delivery_id = self.delivery_table.item(row, 0).text()
            date = self.delivery_table.item(row, 2).text()
            location = self.delivery_table.item(row, 3).text()
            
            self.selected_delivery_id = delivery_id
            self.selected_delivery_label.setText(f"ID: {delivery_id} - {date} at {location}")
        else:
            self.selected_delivery_id = None
            self.selected_delivery_label.setText("None")
    
    def delete_delivery(self):
        """Delete the selected delivery"""
        if not self.selected_delivery_id:
            QMessageBox.warning(self.widget, "Warning", "Please select a delivery to delete")
            return
            
        # Confirm deletion
        confirm = QMessageBox.question(
            self.widget,
            "Confirm Deletion",
            f"Are you sure you want to delete the selected delivery?\nThis action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            success, error = self.database.delete_delivery(self.selected_delivery_id)
            
            if success:
                QMessageBox.information(self.widget, "Success", "Delivery deleted successfully!")
                self.selected_delivery_id = None
                self.selected_delivery_label.setText("None")
                self.load_deliveries()
            else:
                QMessageBox.critical(self.widget, "Error", f"Failed to delete delivery: {error}")
    
    def go_back(self):
        """Go back to the admin menu"""
        self.selected_delivery_id = None
        self.main_window.show_admin_menu(self.user) 