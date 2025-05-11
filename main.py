import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from database import Database, initialize_database
from ui.welcome import WelcomeScreen
from ui.login import LoginScreen
from ui.create_account import CreateAccountScreen
from ui.admin_menu import AdminMainMenu
from ui.user_menu import UserMainMenu
from ui.view_products import ViewProductsScreen
from ui.view_delivery import ViewDeliveryScreen
from ui.view_organization import ViewOrganizationScreen
from ui.view_delivery_user import ViewDeliveryUserScreen
from ui.edit_personal_info import EditPersonalInfoScreen
from ui.add_products import AddProductsScreen
from ui.add_delivery import AddDeliveryScreen
from ui.delete_products import DeleteProductsScreen
from ui.delete_delivery import DeleteDeliveryScreen
from ui.edit_products import EditProductsScreen
from ui.edit_delivery import EditDeliveryScreen

class DonationDriveApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize the database
        initialize_database()
        self.database = Database()
        
        # Configure the main window
        self.setWindowTitle("Donation Drive System")
        self.resize(1301, 811)
        self.setMinimumSize(800, 600)  # Set minimum window size
        
        # Create a stacked widget to manage screens
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Create all screens
        self.setup_screens()
        
        # Show the welcome screen first
        self.stacked_widget.setCurrentIndex(0)
        
    def setup_screens(self):
        """Create and add all screens to the stacked widget"""
        # Welcome Screen
        welcome_widget = QtWidgets.QWidget()
        self.welcome_screen = WelcomeScreen(self)
        self.welcome_screen.setupUi(welcome_widget)
        self.stacked_widget.addWidget(welcome_widget)
        
        # Login Screen
        login_widget = QtWidgets.QWidget()
        self.login_screen = LoginScreen(self)
        self.login_screen.setupUi(login_widget)
        self.stacked_widget.addWidget(login_widget)
        
        # Create Account Screen
        create_account_widget = QtWidgets.QWidget()
        self.create_account_screen = CreateAccountScreen(self)
        self.create_account_screen.setupUi(create_account_widget)
        self.stacked_widget.addWidget(create_account_widget)
        
        # Admin Menu Screen
        admin_menu_widget = QtWidgets.QWidget()
        self.admin_menu_screen = AdminMainMenu(self)
        self.admin_menu_screen.setupUi(admin_menu_widget)
        self.stacked_widget.addWidget(admin_menu_widget)
        
        # User Menu Screen
        user_menu_widget = QtWidgets.QWidget()
        self.user_menu_screen = UserMainMenu(self)
        self.user_menu_screen.setupUi(user_menu_widget)
        self.stacked_widget.addWidget(user_menu_widget)
        
        # Additional screens will be initialized when needed
        self.init_additional_screens()
        
    def init_additional_screens(self):
        """Initialize additional screens"""
        # View Products Screen
        view_products_widget = QtWidgets.QWidget()
        self.view_products_screen = ViewProductsScreen(self)
        self.view_products_screen.setupUi(view_products_widget)
        self.stacked_widget.addWidget(view_products_widget)
        
        # View Delivery Screen
        view_delivery_widget = QtWidgets.QWidget()
        self.view_delivery_screen = ViewDeliveryScreen(self)
        self.view_delivery_screen.setupUi(view_delivery_widget)
        self.stacked_widget.addWidget(view_delivery_widget)
        
        # View Organization Screen
        view_org_widget = QtWidgets.QWidget()
        self.view_org_screen = ViewOrganizationScreen(self)
        self.view_org_screen.setupUi(view_org_widget)
        self.stacked_widget.addWidget(view_org_widget)
        
        # View Delivery User Screen
        view_delivery_user_widget = QtWidgets.QWidget()
        self.view_delivery_user_screen = ViewDeliveryUserScreen(self)
        self.view_delivery_user_screen.setupUi(view_delivery_user_widget)
        self.stacked_widget.addWidget(view_delivery_user_widget)
        
        # Edit Personal Info Screen
        edit_personal_widget = QtWidgets.QWidget()
        self.edit_personal_screen = EditPersonalInfoScreen(self)
        self.edit_personal_screen.setupUi(edit_personal_widget)
        self.stacked_widget.addWidget(edit_personal_widget)
        
        # Add Products Screen
        add_products_widget = QtWidgets.QWidget()
        self.add_products_screen = AddProductsScreen(self)
        self.add_products_screen.setupUi(add_products_widget)
        self.stacked_widget.addWidget(add_products_widget)
        
        # Add Delivery Screen
        add_delivery_widget = QtWidgets.QWidget()
        self.add_delivery_screen = AddDeliveryScreen(self)
        self.add_delivery_screen.setupUi(add_delivery_widget)
        self.stacked_widget.addWidget(add_delivery_widget)
        
        # Delete Products Screen
        delete_products_widget = QtWidgets.QWidget()
        self.delete_products_screen = DeleteProductsScreen(self)
        self.delete_products_screen.setupUi(delete_products_widget)
        self.stacked_widget.addWidget(delete_products_widget)
        
        # Delete Delivery Screen
        delete_delivery_widget = QtWidgets.QWidget()
        self.delete_delivery_screen = DeleteDeliveryScreen(self)
        self.delete_delivery_screen.setupUi(delete_delivery_widget)
        self.stacked_widget.addWidget(delete_delivery_widget)
        
        # Edit Products Screen
        edit_products_widget = QtWidgets.QWidget()
        self.edit_products_screen = EditProductsScreen(self)
        self.edit_products_screen.setupUi(edit_products_widget)
        self.stacked_widget.addWidget(edit_products_widget)
        
        # Edit Delivery Screen
        edit_delivery_widget = QtWidgets.QWidget()
        self.edit_delivery_screen = EditDeliveryScreen(self)
        self.edit_delivery_screen.setupUi(edit_delivery_widget)
        self.stacked_widget.addWidget(edit_delivery_widget)
        
    def show_welcome_screen(self):
        self.stacked_widget.setCurrentIndex(0)
        
    def show_login_screen(self):
        self.stacked_widget.setCurrentIndex(1)
        
    def show_create_account_screen(self):
        self.stacked_widget.setCurrentIndex(2)
        
    def show_admin_menu(self, user):
        self.admin_menu_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(3)
        
    def show_user_menu(self, user):
        self.user_menu_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(4)
        
    def show_view_products(self, user):
        self.view_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(5)
        
    def show_view_delivery(self, user):
        self.view_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(6)
        
    def show_view_organization(self, user):
        self.view_org_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(7)
        
    def show_view_delivery_user(self, user):
        self.view_delivery_user_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(8)
        
    def show_edit_personal_info(self, user):
        self.edit_personal_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(9)
        
    def show_add_products(self, user):
        self.add_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(10)
        
    def show_add_delivery(self, user):
        self.add_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(11)
        
    def show_delete_products(self, user):
        self.delete_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(12)
        
    def show_delete_delivery(self, user):
        self.delete_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(13)
        
    def show_edit_products(self, user):
        self.edit_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(14)
        
    def show_edit_delivery(self, user):
        self.edit_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(15)

    def resizeEvent(self, event):
        """Handle window resize events and propagate to current screen"""
        super().resizeEvent(event)
        # The resize will automatically propagate to child widgets through layouts

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Set application-wide font
    font = QtGui.QFont("Century Gothic", 10)
    app.setFont(font)
    
    main_window = DonationDriveApp()
    main_window.show()
    sys.exit(app.exec_()) 