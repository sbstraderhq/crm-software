import sys
from staff_manager import *
from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5 import *
import mysql
import mysql.connector
from add_staff_backend import add_staff_fx
from edit_staff_backend import edit_staff_fx
from PyQt5.QtCore import *
import pandas as pd


port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"


class StaffManager(QWidget, Ui_Staff):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Staff() 
        # self.ui.setupUi(self)
        self.setupUi(self)

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

        # self.ui.refresh_btn.clicked.connect(self.load_table)
        # self.ui.add_btn.clicked.connect(self.open_addstaff)
        # self.ui.edit_btn.clicked.connect(self.open_editstaff)
        # self.ui.delete_btn.clicked.connect(self.delete_stafF)
        # self.ui.search_btn.clicked.connect(self.search)

        self.load_table()

        
        # self.ui.table_staff.resizeColumnsToContents()

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

    def open_addstaff(self):

        dialog = QtWidgets.QDialog()
        ui = add_staff_fx()
        ui.setupUi(dialog)
        if dialog.exec_() == QDialog.Accepted:
            self.load_table()


    def open_editstaff(self):

        selection = self.table_staff.selectedItems()

        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to edit")
            return


        selected_row = selection[0].row()
        num = self.table_staff.item(selected_row, 0).text()  
        name = self.table_staff.item(selected_row, 1).text()
        username = self.table_staff.item(selected_row, 2).text()
        referral = self.table_staff.item(selected_row, 3).text()
        email = self.table_staff.item(selected_row, 4).text()
        # contact = self.table_staff.item(selected_row, 5).text()
        password = self.table_staff.item(selected_row, 5).text()
        

        dialog = QtWidgets.QDialog()
        ui = edit_staff_fx()
        ui.setupUi(dialog)

        ui.edit_num.setText(num)
        ui.edit_name.setText(name)
        ui.edit_username.setText(username)
        ui.edit_email.setText(email)
        # ui.edit_contact.setText(contact)
        ui.edit_password.setText(password)
        ui.edit_referral.setText(referral)

        if dialog.exec_() == QDialog.Accepted:
            ui.edit_staff(num)
            QMessageBox.information(self, "Success", "staff information updated successfully!")
            self.load_table()

    def delete_stafF(self):

        selection = self.table_staff.selectedItems()
        self.ensure_connection()

        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to delete")
            return
        
        selected_row = selection[0].row()
        name = self.table_staff.item(selected_row, 1).text()
        num = self.table_staff.item(selected_row, 0).text()
        
        confirm = QMessageBox.question(
        self,
        "Confirm Delete",
        f"Are you sure you want to delete the staff: {name}?",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            try:
            
                self.cursor.execute(f"DELETE FROM staff_acc WHERE id = {num}")
                self.conn.commit()

            
                self.cursor.execute("SELECT id FROM staff_acc ORDER BY id")
                nums = self.cursor.fetchall()
                for index, (num_value,) in enumerate(nums):
                    
                    self.cursor.execute(f"UPDATE staff_acc SET id = {index + 1} WHERE id = {num_value}")
                self.conn.commit()

                QMessageBox.information(self, "Success", "Staff deleted successfully!")
                self.load_table() 

            except mysql.connector.Error as err:
                self.conn.rollback()
                QMessageBox.critical(self, "Database Error", f"Error deleting staff: {err}")

    def load_table(self):

        query = f"select name, username, referral_code, email, password, logged_in from staff_acc;"
        self.table_staff.setRowCount(0)
        self.ensure_connection()
        
        try:
            
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            print(data)

            if len(data) != 0:
                num_rows = len(data)
                num_columns = len(data[0]) + 1
                self.table_staff.setRowCount(num_rows)
                self.table_staff.setColumnCount(num_columns)

                for row_num, row_data in enumerate(data):
                    self.table_staff.setItem(row_num, 0, QTableWidgetItem(str(row_num + 1)))
                    for col_num, col_data in enumerate(row_data):
                        self.table_staff.setItem(row_num, col_num + 1, QTableWidgetItem(str(col_data)))
                        self.conn.commit()
                
                self.table_staff.setColumnWidth(0, 40)
                self.table_staff.setColumnWidth(1, 600)
                self.table_staff.setColumnWidth(2, 150)
                self.table_staff.setColumnWidth(3, 150)
                self.table_staff.setColumnWidth(4, 300)

                for row in range(self.table_staff.rowCount()):
                    item = self.table_staff.item(row, 0)  # Get item in the first column
                    if item is not None:  # Check if the item exists
                        item.setTextAlignment(Qt.AlignCenter)  # Center align the text

            else:
                self.table_staff.setRowCount(0)

        except mysql.connector.Error as err:
            print(err)
    
    def search(self):
        self.ensure_connection()
      
        condition = self.searchbar.text()

        query = f"""
        SELECT id, name, username, referral_code, email, password FROM staff_acc 
        WHERE 
            id LIKE '%{condition}%' OR
            name LIKE '%{condition}%' OR
            username LIKE '%{condition}%' OR
            referral_code LIKE '%{condition}%' OR
            email LIKE '%{condition}%' OR
            password LIKE '%{condition}'
        """

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.search_result(result)

        except mysql.connector.Error as err:
            print(err)

    def search_result(self, result):
        if result:
            self.table_staff.setRowCount(0)
            self.table_staff.setRowCount(len(result))

            for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    self.table_staff.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

        else:
            self.table_staff.setRowCount(0)
            return
        
    def export(self):
            
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Choose Directory")
        msg_box.setText("Please choose a directory to save the Excel file.")
    
        # Add custom buttons
        save_button = msg_box.addButton("Choose Directory", QMessageBox.ActionRole)
        cancel_button = msg_box.addButton(QMessageBox.Cancel)

        # Show the message box and wait for user input
        msg_box.exec_()

            # Check which button was clicked
        if msg_box.clickedButton() == save_button:
            # Open the QFileDialog to select a directory
            options = QFileDialog.Options()
            directory = QFileDialog.getExistingDirectory(
                None, 
                "Select Directory", 
                "", 
                options=options
            )
            
            if directory:
            
                # Here you can call the export_to_excel function and pass the directory path
                file_path = f"{directory}/staff.xlsx"
                self.export_to_excel( file_path)

                print(f"Selected directory: {directory}")

                

            else:
                print("No directory selected.")

        else:
            print("Operation canceled.")

    def export_to_excel(self, filename):

                    # Get the number of rows and columns in the table
            row_count = self.table_staff.rowCount()
            column_count = self.table_staff.columnCount()

            # Create a dictionary to hold the table data
            data = {}

            # Extract headers from the table (if available)
            headers = []
            for col in range(column_count):
                header_item = self.table_staff.horizontalHeaderItem(col)
                headers.append(header_item.text() if header_item else f"Column {col+1}")

            # Extract the table data
            for col in range(column_count):
                column_data = []
                for row in range(row_count):
                    item = self.table_staff.item(row, col)
                    column_data.append(item.text() if item else "")
                data[headers[col]] = column_data

            # Create a DataFrame from the dictionary
            df = pd.DataFrame(data)

            # Export the DataFrame to an Excel file
            df.to_excel(filename, index=False)

            print(f"Data exported successfully to {filename}")


    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = StaffManager()
#     window.show()
#     sys.exit(app.exec_())