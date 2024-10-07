import sys
from staff_manager import *
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5 import *
import mysql
import mysql.connector
from edit_staff_dialog import *

port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"

class edit_staff_fx(QDialog, Ui_edit_staff_dialog):
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

    def setupUi(self, edit_staff_dialog):
        super().setupUi(edit_staff_dialog)
      
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.edit_staff)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def ensure_connection(self):
        
        if not self.conn or not self.conn.is_connected():
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()
            print(self.conn)
        else:
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()

    def edit_staff(self, num):
         
        name = self.edit_name.text()
        referral = self.edit_referral.text()
        username = self.edit_username.text()
        email = self.edit_email.text()
        # contact = self.edit_contact.text()
        password = self.edit_password.text()

        if not name or not username or not referral or not email or not password:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields!")
            return

        try:
            
            self.ensure_connection()

            query = """UPDATE staff_acc
                        SET name=%s, username=%s, referral_code=%s, email=%s, password=%s
                        WHERE id=%s"""
            
            values = (name, username, referral, email, password, num)
            self.cursor.execute(query, values)
            self.conn.commit()

            

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error updating client: {err}")
            if self.conn:
                self.conn.rollback()

        #  finally:
        #     if self.conn and self.conn.is_connected():
        #         self.cursor.close()
        #         self.conn.close()
