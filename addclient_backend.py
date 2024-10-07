import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from sbsclientmanager import *
from edit_client import *
from addclient import *
from PyQt5 import *
import mysql.connector
import mysql

port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"




 

class add_dialog_fx(QDialog, Ui_addclient):
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

    def setupUi(self, addclient):
        super().setupUi(addclient)
      
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.add_client_info)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def add_client_info(self):

        name = self.line_name.text()
        referral = self.line_referral.text()
        ic_number = self.line_ic.text()
        email = self.line_email.text()
        contact = self.line_contact.text()
        remark = self.line_remark.text()

        if not name or not ic_number or not email or not contact:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields!")
            return
        try:
            if self.conn:
                self.cursor.execute("select max(client_id) from client")
                result = self.cursor.fetchone()
                next_num = (result[0] + 1) if result [0] else 1

                query = """insert into client (client_id, client_name, ic_number, email, phone, remark, referral_code)
                            values (%s, %s, %s, %s, %s, %s, %s)"""
                
                values = (next_num, name, ic_number, email, contact, remark, referral)
                self.cursor.execute(query, values)
                self.conn.commit()
                
                QMessageBox.information(self, "Success", "Client added successfully!")
                self.close()
                
            
            else:
                QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error adding client: {err}")
            if self.conn:
                self.conn.rollback()
        
        finally:
            if self.conn and self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
