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




class edit_dialog_fx(QDialog, Ui_edit_dialog):
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

    def setupUi(self, edit_dialog):
        super().setupUi(edit_dialog)
      
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.edit_client_info)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def ensure_connection(self):
        
        if not self.conn or not self.conn.is_connected():
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()
            print(self.conn)
        else:
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()

    def edit_client_info(self, actual_num):
         name = self.edit_name.text()
         ic_number = self.edit_ic.text()
         referral = self.edit_referral.text()
         email = self.edit_email.text()
         contact = self.edit_contact.text()
         remark = self.edit_remark.text()

         if not name or not ic_number or not referral or not email or not contact:
            QMessageBox.warning(self, "Input Error", "Please fill in all required fields!")
            return

         try:
            
            self.ensure_connection()

            # Update the client info based on the 'num' value
            query = """UPDATE client
                        SET client_name=%s, ic_number=%s, email=%s, phone=%s, remark=%s
                        WHERE client_id=%s"""
            
            values = (name, ic_number, email, contact, remark, actual_num)
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


