from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFormLayout

class EditPersonalInfoScreen(object):
    def __init__(self, main_window):
        self.main_window = main_window
        self.database = main_window.database
        self.user = None
        self.organization = None
        
    def set_user(self, user):
        print(f"EditPersonalInfo - set_user called with user: {user}")
        self.user = user
        # Get the user's organization
        if not user[6]:  # If not admin
            print(f"Getting organization for user {user[0]}")
            self.organization = self.database.get_user_organization(user[0])
            print(f"Organization data: {self.organization}")
            
            # If organization is None, try to find it with a direct database query
            if self.organization is None:
                try:
                    print("Trying direct database query...")
                    self.database.cursor.execute("""
                        SELECT o.org_id, o.name, l.location_id, l.location_name
                        FROM org_info o
                        JOIN location_info l ON o.location_id = l.location_id
                        WHERE o.user_code = ?
                    """, (user[0],))
                    self.organization = self.database.cursor.fetchone()
                    print(f"Direct query result: {self.organization}")
                    
                    # If still None, create a default organization for this user
                    if self.organization is None:
                        print("Creating default organization for user")
                        org_id, _ = self.database.add_organization(
                            name="CARE Philippines",
                            user_code=user[0],
                            location_id="QC"
                        )
                        if org_id:
                            self.organization = self.database.get_user_organization(user[0])
                            print(f"Created default organization: {self.organization}")
                except Exception as e:
                    print(f"Error with direct query: {str(e)}")
                    # Create a default organization structure to prevent None errors
                    self.organization = (1, "CARE Philippines", "QC", "Quezon City")
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
        
        # Organization field (first field, only visible for regular users)
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("ORGANIZATION")
        self.form_layout.addWidget(self.label_8)
        
        self.organization_field = QtWidgets.QLineEdit()
        self.organization_field.setMinimumSize(QtCore.QSize(400, 41))
        self.organization_field.setMaximumSize(QtCore.QSize(500, 41))
        self.organization_field.setObjectName("organization_field")
        self.form_layout.addWidget(self.organization_field)
        
        # Location field
        self.label_9 = QtWidgets.QLabel()
        self.label_9.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label_9.setObjectName("label_9")
        self.label_9.setText("LOCATION")
        self.form_layout.addWidget(self.label_9)
        
        self.location_combo = QtWidgets.QComboBox()
        self.location_combo.setMinimumSize(QtCore.QSize(400, 41))
        self.location_combo.setMaximumSize(QtCore.QSize(500, 41))
        self.location_combo.setObjectName("location_combo")
        self.form_layout.addWidget(self.location_combo)
        
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
        self.update_button.setStyleSheet("""
            QPushButton {
                border-radius: 20px;
                background-color: #BBD8A3;
                color: black;
                font: 75 18pt "Century Gothic";
                border: 2px solid green;
            }
            QPushButton:hover {
                background-color: #A6C18F;
            }
        """)
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
        self.back_button.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                background-color: rgb(255, 225, 189);
                font: 75 12pt "Century Gothic";
                border: 2px solid orange;
            }
            QPushButton:hover {
                background-color: rgb(240, 200, 150);
            }
        """)
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
        
        # Hide or show organization field based on user type
        if self.user[6]:  # User is admin
            self.label_8.setVisible(False)
            self.organization_field.setVisible(False)
            self.label_9.setVisible(False)
            self.location_combo.setVisible(False)
        else:
            self.label_8.setVisible(True)
            self.organization_field.setVisible(True)
            self.label_9.setVisible(True)
            self.location_combo.setVisible(True)
            
            # Load locations into combo box
            self.location_combo.clear()
            locations = self.database.get_all_locations()
            current_location_id = "QC"  # Default location
            
            if self.organization and len(self.organization) > 2:
                current_location_id = self.organization[2]
                
            # Populate locations dropdown
            selected_index = 0
            for i, location in enumerate(locations):
                self.location_combo.addItem(location[1], location[0])
                if location[0] == current_location_id:
                    selected_index = i
            
            # Set the selected location
            self.location_combo.setCurrentIndex(selected_index)
            
            # Load organization name if available
            if self.organization:
                print(f"Setting organization field to: {self.organization[1]}")
                self.organization_field.setText(str(self.organization[1]))  # organization name
            else:
                # Set a default value to prevent UI errors
                self.organization_field.setText("CARE Philippines")
                
        self.username.setText(self.user[1])  # username
        self.firstname.setText(self.user[2])  # firstname
        self.lastname.setText(self.user[3])  # lastname
        self.password.setText(self.user[4])  # password
        self.confirmpassword.setText(self.user[5])  # confirm password
    
    def update_user_info(self):
        """Update user information in the database"""
        print("Update button clicked")
        username = self.username.text()
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        password = self.password.text()
        confirm_password = self.confirmpassword.text()
        
        print(f"Form data: username={username}, firstname={firstname}, lastname={lastname}, passwords match={password==confirm_password}")
        
        # Validate inputs
        if not username or not firstname or not lastname or not password or not confirm_password:
            self.error_label.setText("Please fill in all fields")
            print("Validation failed: Not all fields are filled")
            return
            
        if password != confirm_password:
            self.error_label.setText("Passwords do not match")
            print("Validation failed: Passwords don't match")
            return
        
        # Store user_id for later refresh
        user_id = self.user[0]
        
        # Update user in database
        try:
            success, error = self.database.update_user(user_id, username, firstname, lastname, password)
            
            if not success:
                self.error_label.setText(error)
                print(f"Database update failed: {error}")
                return
                
            print("User information updated successfully")
            
            # Update organization name if user is not admin
            if not self.user[6]:
                org_name = self.organization_field.text()
                print(f"Organization name: {org_name}")
                print(f"Current organization in DB: {self.organization}")
                
                # Get selected location ID
                location_id = self.location_combo.currentData()
                print(f"Selected location ID: {location_id}")
                
                if not location_id:
                    # Fallback to default if no location selected
                    location_id = "QC"
                
                try:
                    # First remove the old organization if it exists
                    print(f"Removing existing organization for user {user_id}")
                    self.database.cursor.execute(
                        "DELETE FROM org_info WHERE user_code = ?", 
                        (user_id,)
                    )
                    
                    # Then add the new organization
                    print(f"Adding new organization: {org_name}, user_code: {user_id}, location: {location_id}")
                    org_id, org_error = self.database.add_organization(
                        name=org_name,
                        user_code=user_id,
                        location_id=location_id
                    )
                    
                    if org_error:
                        print(f"Error adding organization: {org_error}")
                        # Don't return, just log the error, but allow the user update to proceed
                    else:
                        print(f"Organization updated successfully with ID: {org_id}")
                        
                    self.database.commit()
                except Exception as e:
                    print(f"Exception during organization update: {str(e)}")
                    # Don't stop the user update process for organization errors
            
            # Show success message
            QMessageBox.information(self.widget, "Success", "Information updated successfully!")
            
            # Update the user object with new data - with error handling
            try:
                # Force a database refresh without caching
                self.database.connection.commit()
                
                # Explicitly get updated user data
                updated_user = self.database.get_user_by_id(user_id)
                print(f"After update - retrieved user data: {updated_user}")
                
                # Only update if we got a valid user back
                if updated_user:
                    self.user = updated_user
                    
                    # Also update organization data if needed and user is not admin
                    if self.user and not self.user[6]:
                        try:
                            self.organization = self.database.get_user_organization(user_id)
                            print(f"Updated organization data: {self.organization}")
                        except Exception as org_err:
                            print(f"Error updating organization data: {str(org_err)}")
                            # Continue even if organization update fails
                else:
                    print("Warning: Could not retrieve updated user data")
            except Exception as user_err:
                print(f"Error updating user data: {str(user_err)}")
                # Continue even if we couldn't refresh the user data
            
            # Go back to the appropriate menu - with additional safety check
            self.go_back()
            
        except Exception as e:
            print(f"Unexpected error during update: {str(e)}")
            self.error_label.setText(f"Error: {str(e)}")
    
    def go_back(self):
        """Go back to the appropriate menu based on user type"""
        if not self.user:
            # Safety check - if somehow user is None, go to login screen
            self.main_window.show_login_screen()
            return
            
        if self.user[6]:  # User is admin
            self.main_window.show_admin_menu(self.user)
        else:
            self.main_window.show_user_menu(self.user) 