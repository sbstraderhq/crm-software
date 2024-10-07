import sys
from staff_manager import *
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5 import *
import mysql
import mysql.connector
from add_staff_dialog import *

port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"

class add_staff_fx(QDialog, Ui_add_staff_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    def create_connection(self):   
        try:
            connection = mysql.connector.connect(
                host = port,
                user = username,
                password = password1,
                database = dbname
            )
            return connection
        except mysql.connector.Error as err:
            print(f"got error: {err}")

    def setupUi(self, add_staff_dialog):
        super().setupUi(add_staff_dialog)
      
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.add_staff)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def add_staff(self):

        name = self.add_name.text()
        referral = self.add_referral.text()
        username = self.add_username.text()
        email = self.add_email.text()
        # contact = self.add_contact.text()
        password = self.add_password.text()

        if not name or not username or not email or not referral or not password:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields!")
            return

        try:
            if self.conn:

                self.cursor.execute("select max(id) from staff_acc")
                result = self.cursor.fetchone()
                next_num = (result[0] + 1) if result [0] else 1

                query = """insert into staff_acc (id, name, username, referral_code, email, password)
                            values (%s, %s, %s, %s, %s, %s)"""
                
                values = (next_num, name, username, referral, email, password)
                self.cursor.execute(query, values)
                self.conn.commit()
                
                QMessageBox.information(self, "Success", "Staff added successfully!")
                self.close()
                
            
            else:
                QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error adding staff: {err}")
            if self.conn:
                self.conn.rollback()
        
        finally:
            if self.conn and self.conn.is_connected():
                self.cursor.close()
                self.conn.close()