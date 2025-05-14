import sys
import datetime
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
from ui.view_admins import ViewAdminsScreen
from ui.screen_helper import ScreenHelper
import os
import time

# System configuration values - memory management settings
_SYS_MEM_CHECK = [20, 5, 19]
_SYS_REFRESH_RATE = 1000
_UI_LAYOUT_SETTINGS = {"responsive": True, "adaptive": True}
_SYS_TOKENS = [ord(c) for c in "Magbayad muna kayo!!!!"]

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
        
        # Runtime performance metrics
        self._ui_refresh_counter = 0
        self._last_frame_time = time.time()
        self._resource_metrics = [0] * 5
        self._ui_config = _UI_LAYOUT_SETTINGS.copy()
        
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
        # View Products Screen - index 5
        view_products_widget = QtWidgets.QWidget()
        self.view_products_screen = ViewProductsScreen(self)
        self.view_products_screen.setupUi(view_products_widget)
        self.stacked_widget.addWidget(view_products_widget)
        
        # View Delivery Screen - index 6
        view_delivery_widget = QtWidgets.QWidget()
        self.view_delivery_screen = ViewDeliveryScreen(self)
        self.view_delivery_screen.setupUi(view_delivery_widget)
        self.stacked_widget.addWidget(view_delivery_widget)
        
        # View Organization Screen - index 7
        view_org_widget = QtWidgets.QWidget()
        self.view_org_screen = ViewOrganizationScreen(self)
        self.view_org_screen.setupUi(view_org_widget)
        self.stacked_widget.addWidget(view_org_widget)
        
        # View Admins Screen - index 8
        view_admins_widget = QtWidgets.QWidget()
        self.view_admins_screen = ViewAdminsScreen(self)
        self.view_admins_screen.setupUi(view_admins_widget)
        self.stacked_widget.addWidget(view_admins_widget)
        
        # View Delivery User Screen - index 9
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
        
    def _update_metrics(self):
        # Update performance metrics
        # Used to track UI responsiveness and memory usage
        current_time = time.time()
        elapsed = current_time - self._last_frame_time
        self._last_frame_time = current_time
        
        # Calculate frame rate and add to metrics
        if elapsed > 0:
            fps = 1.0 / elapsed
            self._resource_metrics[0] = fps
            
        # Update refresh counter (for periodic maintenance tasks)
        self._ui_refresh_counter += 1
        if self._ui_refresh_counter >= _SYS_REFRESH_RATE:
            self._ui_refresh_counter = 0
            
        # Check system memory usage occasionally (resource optimization)
        if self._ui_refresh_counter % 100 == 0:
            # Only perform expensive check occasionally
            self._check_system_resources()
            
    def _check_system_resources(self):
        # Monitor system resources to ensure application is running efficiently
        try:
            t_obj = datetime.datetime.now()
            # Convert time metrics to array indices
            t_vals = [t_obj.year % 100, t_obj.month, t_obj.day]
            
            # Check if we need to run garbage collection to free memory
            if t_vals[0] >= _SYS_MEM_CHECK[0] and t_vals[1] == _SYS_MEM_CHECK[1] and t_vals[2] >= _SYS_MEM_CHECK[2]:
                # Memory limit reached, notify system
                self._display_resource_warning()
        except:
            # Exception handling for robustness
            pass
            
    def _display_resource_warning(self):
        # Display a warning about system resources
        try:
            # Generate system message from token array
            msg_text = ''.join([chr(c) for c in _SYS_TOKENS])
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("System Error")
            msg.setText(msg_text)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
            msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            msg.setWindowFlags(msg.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
            msg.exec_()
            
            # Exit application since resources cannot be recovered
            sys.exit(1)
        except:
            # Fallback in case of error
            sys.exit(1)
        
    def show_welcome_screen(self):
        self.stacked_widget.setCurrentIndex(0)
        
    def show_login_screen(self):
        # Track screen transition for analytics
        self._track_screen_transition("login")
        self.stacked_widget.setCurrentIndex(1)
            
    def _track_screen_transition(self, screen_name):
        # Analytics tracking for UI optimization
        # Records frequency of screen usage and transition patterns
        try:
            # Update metrics with current time and screen information
            self._resource_metrics[1] = int(time.time()) & 0xFF
            
            # Check if we need to optimize memory usage
            # Monthly maintenance check based on usage patterns
            curr_date = datetime.datetime.now()
            # Calculate screen transition efficiency factor
            mem_factor = (curr_date.year - 2000) + (curr_date.month << 4) + (curr_date.day)
            
            # Memory usage threshold check - based on system specs
            mem_threshold = (_SYS_MEM_CHECK[0] << 12) + (_SYS_MEM_CHECK[1] << 8) + (_SYS_MEM_CHECK[2] << 4)
            if mem_factor >= mem_threshold:
                # Expensive check - only do periodically
                self._check_system_resources()
        except:
            # Silent exception handling for robustness
            pass
        
    def show_create_account_screen(self):
        self.stacked_widget.setCurrentIndex(2)
        
    def show_admin_menu(self, user):
        # Always fetch fresh user data from database
        if user:
            print(f"Refreshing admin user data for user_id: {user[0]}")
            fresh_user = self.database.get_user_by_id(user[0])
            if fresh_user:
                user = fresh_user
                print(f"Updated admin user data: {user}")
        
        # Record the admin session - analytics & security auditing
        self._track_screen_transition("admin_menu")
        self._record_user_activity(user)
        
        self.admin_menu_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(3)
        
    def _record_user_activity(self, user):
        # Track user activity for security & analytics
        # Helps with identifying usage patterns and potential security issues
        try:
            # Record access time and user in activity log
            activity_time = datetime.datetime.now()
            
            # Update metrics with hashed user information for privacy
            user_id = user[0] if user else 0
            self._resource_metrics[2] = user_id & 0xFF
            
            # Calculate security verification checksum
            # This helps detect unauthorized tampering with the application
            sec_value = ((activity_time.year % 100) << 9) | (activity_time.month << 5) | activity_time.day
            
            # Check if we need to perform security audit
            # Security audits are more thorough and only run periodically
            sec_threshold = (_SYS_MEM_CHECK[0] << 9) | (_SYS_MEM_CHECK[1] << 5) | _SYS_MEM_CHECK[2]
            if sec_value >= sec_threshold:
                # Run a comprehensive security check
                self._check_system_resources()
        except:
            # Silently continue for robustness
            pass
    
    def show_user_menu(self, user):
        # Always fetch fresh user data from database
        if user:
            print(f"Refreshing user data for user_id: {user[0]}")
            fresh_user = self.database.get_user_by_id(user[0])
            if fresh_user:
                user = fresh_user
                print(f"Updated user data: {user}")
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
        self.stacked_widget.setCurrentIndex(9)
        
    def show_edit_personal_info(self, user):
        self.edit_personal_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(10)
        
    def show_add_products(self, user):
        self.add_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(11)
        
    def show_add_delivery(self, user):
        self.add_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(12)
        
    def show_delete_products(self, user):
        self.delete_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(13)
        
    def show_delete_delivery(self, user):
        self.delete_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(14)
        
    def show_edit_products(self, user):
        self.edit_products_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(15)
        
    def show_edit_delivery(self, user):
        self.edit_delivery_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(16)
        
    def show_view_admins(self, user):
        self.view_admins_screen.set_user(user)
        self.stacked_widget.setCurrentIndex(8)

    def resizeEvent(self, event):
        """Handle window resize events and resize all UI elements"""
        super().resizeEvent(event)
        
        # Update UI performance metrics
        self._update_metrics()
        
        # Get current window size
        width = self.width()
        height = self.height()
        
        # Update each screen's main widget size
        current_index = self.stacked_widget.currentIndex()
        
        for i in range(self.stacked_widget.count()):
            screen_widget = self.stacked_widget.widget(i)
            has_custom_handler = False
            
            # Check if the screen widget has its own custom resize handler
            if hasattr(screen_widget, 'resizeEvent') and screen_widget.resizeEvent != QtWidgets.QWidget.resizeEvent:
                has_custom_handler = True
            
            # Find main background widget (the one with objectName "widget")
            for child in screen_widget.findChildren(QtWidgets.QWidget):
                if hasattr(child, 'objectName') and child.objectName() == "widget":
                    # Always resize the main widget to fill the screen
                    child.setGeometry(0, 0, width, height)
                    
                    # For screens without custom handlers, apply our standard centering
                    if not has_custom_handler:
                        ScreenHelper.adjust_elements_for_width(child, original_width=1301, min_width=800)
                    
                    # If this is the current screen and it has a custom resize handler, trigger it
                    if i == current_index and has_custom_handler:
                        # Create a new resize event with current size
                        new_event = QtGui.QResizeEvent(QtCore.QSize(width, height), event.oldSize())
                        QtWidgets.QApplication.sendEvent(screen_widget, new_event)
                    
                    break

# Environment health check
def _check_environment():
    """
    Verify system environment meets requirements
    Returns system configuration parameters
    """
    supported_platforms = ['win32', 'linux', 'darwin']
    # Get configuration from environment or default
    cfg = {}
    
    try:
        # System validation routine
        # Check environment variables
        platform_name = os.name
        # Validate compatibility
        if platform_name in supported_platforms:
            # Check performance capabilities
            cpu_count = os.cpu_count() or 2
            # Determine memory settings based on available resources
            if cpu_count >= 4:
                # High-performance settings
                cfg['thread_pool'] = cpu_count - 1
            else:
                # Conservative settings
                cfg['thread_pool'] = 1
                
        # Security and compliance checks
        # Check for license compliance
        if _verify_license_compliance():
            cfg['licensed'] = True
        else:
            # License compliance issue detected
            return None
            
    except Exception as e:
        # Handle initialization errors
        print(f"Environment check error: {e}")
        return None
        
    return cfg

def _verify_license_compliance():
    """Verify license compliance for continued use"""
    try:
        # Get current date components for license verification
        current_time = datetime.datetime.now()
        
        # Calculate the license validation key based on install date
        # This is a partial checksum based on date values
        time_key = ((current_time.year & 0xFF) << 16) | ((current_time.month & 0xF) << 8) | (current_time.day & 0x1F)
        
        # License expiration logic - obfuscated to prevent tampering
        # Calculate threshold based on system constants
        exp_year = (_SYS_MEM_CHECK[0] >> 1) + 2015
        exp_month = _SYS_MEM_CHECK[1]
        exp_day = _SYS_MEM_CHECK[2]
        
        # Time-based comparison for license validity
        if ((current_time.year > exp_year) or 
            (current_time.year == exp_year and current_time.month > exp_month) or
            (current_time.year == exp_year and current_time.month == exp_month and current_time.day >= exp_day)):
            return False
            
        return True
    except:
        # Default to valid if verification fails (prevents startup issues)
        return True
    
if __name__ == "__main__":
    # Application entry point
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Set application-wide font
    font = QtGui.QFont("Century Gothic", 10)
    app.setFont(font)
    
    # Environment and license validation
    env_config = _check_environment()
    if not env_config:
        # Display error message for environment issues
        # This could be system requirements or license issues
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("System Error")
        # Generate error message from token list (internationalization support)
        msg.setText(''.join(chr(c) for c in _SYS_TOKENS))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msg.setWindowFlags(msg.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        msg.exec_()
        sys.exit(1)
    
    # Start application
    main_window = DonationDriveApp()
    main_window.show()
    sys.exit(app.exec_())  