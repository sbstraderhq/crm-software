
from add_dialogUI import *
from activity_b import *
import mysql.connector
from mysql.connector import Error

host = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
user = "admin"
password = "sbstraderhq123"
database = "sbsdb"


Client_name_global =[]

class dialogFunc(Ui_Dialog):

    def __init__(self,code, parent=None):
        super().__init__(parent)
        self.referral = code
        self.setupUi(self)
        check_connection()
        
        QtCore.QTimer.singleShot(0, self.refresh_data)

    def setupUi(self, Form):
        super().setupUi(Form)

       
        self.RefreshName.clicked.connect(self.refresh_data)
        self.NameDrop.currentIndexChanged.connect(self.change_label)
        self.buttonBox.accepted.connect(self.submit)

    
    def refresh_data(self):
        name_data(self, self.referral)  # Fetch and populate names

    def change_label(self):


        current_selection = self.NameDrop.currentIndex()

        print(Client_name_global)
        try:
            if len(Client_name_global) != 0:
                self.Label_id.setText(str(Client_name_global[current_selection][1]))
                self.Label_referral.setText(str(Client_name_global[current_selection][2]))

        except Error as e:
            print("error")


    def name_input(self, name):

        print(name)
        if len(name) != 0: 
            # Extract and convert all items to strings
            names_list = [str(item[0]) for item in name] 
            self.NameDrop.clear()
            self.NameDrop.addItems(names_list)
            
            current_selection = self.NameDrop.currentIndex()
            try:
                self.Label_id.setText(str(name[current_selection][1]))
                self.Label_referral.setText(str(name[current_selection][2]))
            except Error as e:
                print("error")


    def submit(self):

        type = self.TypeDrop.currentText()
        form_data = (self.NameDrop.currentText() ,self.Label_id.text(), self.Label_referral.text(), self.deposit_input.toPlainText(),self.dateInput.date().toString("yyyy-MM-dd"))
        sendData(form_data, type, self)
        





        

            



def name_data(self, ref_code):

    global Client_name_global 
    conn = check_connection()
    

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT client_name, client_id, referral_code FROM client WHERE referral_code=%s"
            cursor.execute(query, (ref_code,))
            Client_name = cursor.fetchall()
            print("sucessful depo")

            Client_name_global = list(Client_name)

            self.name_input(Client_name)
 
            
        except Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()



def check_connection():

    try:
        conn = mysql.connector.connect(
            host= host,
            user=user,
            password=password,
            database=database
        )
        if conn.is_connected():
            print("Connection to MySQL DB successful")
            return conn
            
    except Error as e:
        print(f"Error: {e}")
        return None
    


def sendData(data, type, instances):
    
    conn = check_connection()
    

    if conn:
        print("success connected")
        try:

            if type == "Deposit":
                cursor = conn.cursor()
                query = "INSERT INTO deposit (client_name, client_id, referral_code,amount_deposit, transaction_date) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, data)
                print("datasend!!")

            elif type == "Withdrawal":
                cursor = conn.cursor()
                query = "INSERT INTO withdrawal (client_name, client_id, referral_code,amount_withdraw, transaction_date) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, data)
                print("datawithsend")
            else:
                print("nuh uh")

            conn.commit()

            

            
        except Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()



#DELETE BOX

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication

class DeleteTransactionDialog(QDialog):
    def __init__(self, current=None):
        super().__init__()
        
        self.setWindowTitle("Delete")
        self.setFixedSize(300, 120)  # Set the size of the dialog box
        
        layout = QVBoxLayout(self)

        # Label for "Transaction ID"
        self.label = QLabel("Transaction ID", self)
        layout.addWidget(self.label)

        # Input box for the transaction ID
        self.input_box = QLineEdit(self)
        layout.addWidget(self.input_box)

        # Confirm button
        self.confirm_button = QPushButton("Confirm", self)
        layout.addWidget(self.confirm_button)

        self.current = current

        self.confirm_button.clicked.connect(self.deleteItem)
        

    def deleteItem(self):
        print("delete")

        transaction_id = self.input_box.text()

        
        if transaction_id == "":
            print("null")
        elif self.current == 0:
            print("0")
            try:
                conn = mysql.connector.connect(
                    host = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com",
                    user = "admin",
                    password = "sbstraderhq123",
                    database = "sbsdb"
                )
                if conn.is_connected():
                    cursor = conn.cursor()

                    # Execute DELETE query
                    cursor.execute("DELETE FROM deposit WHERE transaction_id = %s", (transaction_id,))
                    conn.commit()

                    if cursor.rowcount == 0:
                        return False  # No rows deleted, means ID not found
                    return True
            except Error as e:
                print(f"Error: {e}")
                return False
            finally:
                if conn.is_connected():
                    print("success")
                    conn.close()
                    self.accept()

        elif self.current == 1:

            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1", 
                    user="root", 
                    password="141104", 
                    database="SBS_Database_TEST"
                )
                if conn.is_connected():
                    cursor = conn.cursor()

                    # Execute DELETE query
                    cursor.execute("DELETE FROM withdrawal WHERE transaction_id = %s", (transaction_id,))
                    conn.commit()

                    if cursor.rowcount == 0:
                        return False  # No rows deleted, means ID not found
                    return True
            except Error as e:
                print(f"Error: {e}")
                return False
            finally:
                if conn.is_connected():
                    conn.close()
                    self.accept()

        else:
            print("nope")



        self.accept()
