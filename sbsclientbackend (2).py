import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from sbsclientmanager import *
from edit_client import *
from addclient import *
from PyQt5 import *
from addclient_backend import *
from editbackend import *
import mysql.connector
import mysql


port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, name, username): ##########################################
        super().__init__()
        self.setupUi(self)

#################################################
        self.login = username
        self.name_label.setText(name)
        self.username_label.setText(username)

        self.signout_btn.clicked.connect(self.sign_out)  ############# ni aku tambah sign out fx kot2 kau tk buat lagi, kalau dah delete je la

##################################################

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

        self.load_table()

        self.add_btn.clicked.connect(self.add_popup_dialog)
        self.edit_btn.clicked.connect(self.edit_popup_dialog)

        self.search_btn.clicked.connect(self.search_info)

        self.refresh_btn.clicked.connect(self.load_table)

        self.table_client.setSortingEnabled(True)

        self.delete_btn.clicked.connect(self.delete)

        self.showMaximized()


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

    def add_popup_dialog(self):
        dialog = QtWidgets.QDialog()
        ui = add_dialog_fx()
        ui.setupUi(dialog)
        dialog.exec_()


    def edit_popup_dialog(self):

        selection = self.table_client.selectedItems()

        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to edit")
            return

        selected_row = selection[0].row()
        num = self.table_client.item(selected_row, 0).text()  
        name = self.table_client.item(selected_row, 1).text()
        client_id = self.table_client.item(selected_row, 2).text()
        deposit = self.table_client.item(selected_row, 3).text()
        email = self.table_client.item(selected_row, 4).text()
        contact = self.table_client.item(selected_row, 5).text()
        remark = self.table_client.item(selected_row, 6).text()

        dialog = QtWidgets.QDialog()
        ui = edit_dialog_fx()
        ui.setupUi(dialog)

        ui.edit_name.setText(name)
        ui.edit_client_id.setText(client_id)
        ui.edit_deposit.setText(deposit)
        ui.edit_email.setText(email)
        ui.edit_contact.setText(contact)
        ui.edit_remark.setText(remark)

        if dialog.exec_() == QDialog.Accepted:
            ui.edit_client_info(num)
        
    def delete(self):
        selection = self.table_client.selectedItems()
        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to delete")
            return
        
        selected_row = selection[0].row()
        num = self.table_client.item(selected_row, 0).text()  
        
        confirm = QMessageBox.question(
        self,
        "Confirm Delete",
        f"Are you sure you want to delete the client with num {num}?",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            try:
            
                self.cursor.execute(f"DELETE FROM clientele WHERE num = {num}")
                self.conn.commit()

            
                self.cursor.execute("SELECT num FROM clientele ORDER BY num")
                nums = self.cursor.fetchall()
                for index, (num_value,) in enumerate(nums):
                    
                    self.cursor.execute(f"UPDATE clientele SET num = {index + 1} WHERE num = {num_value}")
                self.conn.commit()

                QMessageBox.information(self, "Success", "Client deleted successfully!")
                self.load_table() 

            except mysql.connector.Error as err:
                self.conn.rollback()
                QMessageBox.critical(self, "Database Error", f"Error deleting client: {err}")

    def search_info(self):
      
        condition = self.searchbar.text()

        query = f"""
        SELECT * FROM clientele 
        WHERE 
            num LIKE '%{condition}%' OR
            name LIKE '%{condition}%' OR
            client_id LIKE '%{condition}%' OR
            deposit LIKE '%{condition}%' OR
            email LIKE '%{condition}%' OR
            contact LIKE '%{condition}%' OR
            remark LIKE '%{condition}%'
        """

    

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.search_result(result)

        except mysql.connector.Error as err:
            print(err)


    def load_table(self):
        query = "select * from clientele"
        self.ensure_connection()
        
        try:
            
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            num_rows = len(data)
            num_columns = len(data[0])
            self.table_client.setRowCount(num_rows)
            self.table_client.setColumnCount(num_columns)

            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    self.table_client.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
                    self.conn.commit()

        except mysql.connector.Error as err:
            print(err)

    def search_result(self, result):
        if result:
            self.table_client.setRowCount(0)
            self.table_client.setRowCount(len(result))

            for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    self.table_client.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
        
        else:
            self.table_client.setRowCount(0)
            return

    #############################################################################################     

    def sign_out(self): ############### close app, signout
        
        self.close()
        

    def closeEvent(self, event): ##################### update function nama sama cam sebelum ni, content lain sikit, signout bila close app (signout btn or close window btn)
        try:
            query = "UPDATE staff_acc SET logged_in = 0 WHERE username = %s"
            self.cursor.execute(query, (self.login,))
            self.conn.commit()

        except mysql.connector.Error as err:
            print(f"Error logging out: {err}")

        finally:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("conn closed")
        event.accept()

##################################################################################
    
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())