import mysql.connector
from analysis import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5 import *
import mysql
from PyQt5.QtCore import *


port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"

class Analysis(QWidget, Ui_analysis):
    def __init__(self, referral, admin):
        super().__init__()
        # self.ui = Ui_Staff() 
        # self.ui.setupUi(self)
        self.setupUi(self)

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

        client_id = 1
        
    def check_admin(self, admin):
        if admin == 0:
            self.is_admin = False
        else:
            self.is_admin = True

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

    def ensure_connection(self):
        
        if not self.conn or not self.conn.is_connected():
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()
            print(self.conn)
        else:
            self.conn = self.create_connection()
            self.cursor = self.conn.cursor()

    def get_client_balance(self):

        self.ensure_connection()

        query = """
        SELECT 
            d.client_id
            IFNULL(SUM(d.amount_deposit), 0) AS total_deposit,
            IFNULL(SUM(w.amount_withdraw), 0) AS total_withdrawal,
            (IFNULL(SUM(d.amount_deposit), 0) - IFNULL(SUM(w.amount_withdrawal), 0)) AS net_balance
        FROM deposit d
        LEFT JOIN withdrawal w ON d.client_id = w.client_id
        
        """



        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
         
        
        self.conn.close()

        self.balance_table(result)

    def balance_table(self, result):
        
        pass