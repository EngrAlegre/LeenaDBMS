from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy

class DeleteProductsScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        self.selected_product_id = None
        
    def set_user(self, user):
        self.user = user
        self.load_products()
        
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
        
        # Main layout for the content
        self.main_layout = QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(60, 30, 60, 30)
        
        # Title area
        self.title_layout = QHBoxLayout()
        self.title_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Title
        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("font: 36pt \"Century Gothic\"; color:rgb(76, 107, 140)")
        self.label.setObjectName("label")
        self.label.setText("DELETE PRODUCT")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.title_layout.addWidget(self.label)
        self.title_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.main_layout.addLayout(self.title_layout)
        
        # Subtitle
        self.subtitle_layout = QHBoxLayout()
        self.subtitle_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setStyleSheet("font: 16pt \"Century Gothic\";color:\n"
"rgb(71, 84, 111)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Select a product to delete")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.subtitle_layout.addWidget(self.label_2)
        self.subtitle_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.main_layout.addLayout(self.subtitle_layout)
        
        # Search area
        self.search_layout = QHBoxLayout()
        
        # Search label
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("SEARCH:")
        self.label_4.setMinimumWidth(80)
        self.search_layout.addWidget(self.label_4)
        
        # Search field
        self.search_field = QtWidgets.QLineEdit()
        self.search_field.setMinimumHeight(31)
        self.search_field.setObjectName("search_field")
        self.search_layout.addWidget(self.search_field, 1)  # 1 is stretch factor
        
        # Apply filter button
        self.apply_filter = QtWidgets.QPushButton()
        self.apply_filter.setMinimumSize(QtCore.QSize(120, 31))
        self.apply_filter.setMaximumSize(QtCore.QSize(161, 31))
        self.apply_filter.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(187, 216, 163);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid green")
        self.apply_filter.setObjectName("apply_filter")
        self.apply_filter.setText("SEARCH")
        self.search_layout.addWidget(self.apply_filter)
        
        self.main_layout.addLayout(self.search_layout)
        
        # Table widget for products
        self.product_table = QtWidgets.QTableWidget()
        self.product_table.setMinimumHeight(300)
        self.product_table.setObjectName("product_table")
        self.product_table.setColumnCount(4)
        self.product_table.setHorizontalHeaderLabels(["ID", "Product Name", "Perishable", "Quantity"])
        
        # Make columns stretch to fill available space
        header = self.product_table.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        self.main_layout.addWidget(self.product_table, 1)  # 1 is stretch factor
        
        # Selection area
        self.selection_layout = QHBoxLayout()
        
        # Selection box with background
        self.selection_box = QtWidgets.QGroupBox()
        self.selection_box.setMinimumHeight(50)
        self.selection_box.setStyleSheet("QGroupBox{\n"
"background-color: rgb(200, 220, 240);\n"
"border: 2px solid rgb(76, 107, 140);\n"
"border-radius: 10px;\n"
"}")
        self.selection_box.setTitle("")
        self.selection_box.setObjectName("selection_box")
        
        # Layout for selection box
        self.selection_box_layout = QHBoxLayout(self.selection_box)
        self.selection_box_layout.setContentsMargins(10, 5, 10, 5)
        
        # Selected product info
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("SELECTED PRODUCT:")
        self.selection_box_layout.addWidget(self.label_3)
        
        self.selected_product_label = QtWidgets.QLabel()
        self.selected_product_label.setStyleSheet("font: 12pt \"Century Gothic\"; color: rgb(76, 107, 140)")
        self.selected_product_label.setObjectName("selected_product_label")
        self.selected_product_label.setText("None")
        self.selection_box_layout.addWidget(self.selected_product_label, 1)  # 1 is stretch factor
        
        self.selection_layout.addWidget(self.selection_box)
        self.main_layout.addLayout(self.selection_layout)
        
        # Buttons area
        self.buttons_layout = QHBoxLayout()
        
        # Back button (left-aligned)
        self.back_button = QtWidgets.QPushButton()
        self.back_button.setMinimumSize(QtCore.QSize(161, 41))
        self.back_button.setMaximumSize(QtCore.QSize(161, 41))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 225, 189);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid orange")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("BACK")
        self.buttons_layout.addWidget(self.back_button)
        
        # Spacer to push delete button to center
        self.buttons_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Delete button (center-aligned)
        self.delete_button = QtWidgets.QPushButton()
        self.delete_button.setMinimumSize(QtCore.QSize(191, 61))
        self.delete_button.setMaximumSize(QtCore.QSize(250, 61))
        self.delete_button.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(255, 100, 100);\n"
"font: 75 18pt \"Century Gothic\";\n"
"border: 2px solid rgb(200, 50, 50)")
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setText("DELETE")
        self.buttons_layout.addWidget(self.delete_button)
        
        # Spacer for symmetry
        self.buttons_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        self.main_layout.addLayout(self.buttons_layout)
        
        # Connect the buttons to their functions
        self.apply_filter.clicked.connect(self.apply_search)
        self.back_button.clicked.connect(self.go_back)
        self.delete_button.clicked.connect(self.delete_product)
        self.product_table.itemSelectionChanged.connect(self.on_selection_change)
        
        # Handle window resize events
        Widget.resizeEvent = self.on_resize
        
    def load_products(self):
        """Load products from database into the table"""
        if not self.user:
            return
            
        # Get products
        products = self.database.get_all_products()
        
        # Clear the table
        self.product_table.setRowCount(0)
        
        # Get search term
        search_term = self.search_field.text().lower() if self.search_field.text() else None
        
        # Populate the table
        row = 0
        for product in products:
            product_id = product[0]
            product_name = product[1]
            perishable = "Yes" if product[2] else "No"
            quantity = product[3]
            
            # If search term is specified, filter results
            if search_term and search_term not in product_name.lower():
                continue
                
            self.product_table.insertRow(row)
            self.product_table.setItem(row, 0, QTableWidgetItem(str(product_id)))
            self.product_table.setItem(row, 1, QTableWidgetItem(product_name))
            self.product_table.setItem(row, 2, QTableWidgetItem(perishable))
            self.product_table.setItem(row, 3, QTableWidgetItem(str(quantity)))
            row += 1
            
    def apply_search(self):
        """Apply search filter to products table"""
        self.load_products()
    
    def on_selection_change(self):
        """Handle selection changes in the table"""
        selected_rows = self.product_table.selectedItems()
        if selected_rows:
            row = selected_rows[0].row()
            product_id = self.product_table.item(row, 0).text()
            product_name = self.product_table.item(row, 1).text()
            
            self.selected_product_id = product_id
            self.selected_product_label.setText(f"ID: {product_id} - {product_name}")
        else:
            self.selected_product_id = None
            self.selected_product_label.setText("None")
    
    def delete_product(self):
        """Delete the selected product"""
        if not self.selected_product_id:
            QMessageBox.warning(self.widget, "Warning", "Please select a product to delete")
            return
            
        # Confirm deletion
        confirm = QMessageBox.question(
            self.widget,
            "Confirm Deletion",
            f"Are you sure you want to delete the selected product?\nThis action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            success, error = self.database.delete_product(self.selected_product_id)
            
            if success:
                QMessageBox.information(self.widget, "Success", "Product deleted successfully!")
                self.selected_product_id = None
                self.selected_product_label.setText("None")
                self.load_products()
            else:
                QMessageBox.critical(self.widget, "Error", f"Failed to delete product: {error}")
    
    def go_back(self):
        """Go back to the admin menu"""
        self.selected_product_id = None
        self.main_window.show_admin_menu(self.user)
    
    def on_resize(self, event):
        """Handle window resize events"""
        # This method is called when the window is resized
        # The layouts will automatically adjust the widgets
        # No need to call super as we're not a true QWidget subclass
        pass 