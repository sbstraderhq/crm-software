import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from PyQt5.QtCore import *
#from sbsclientmanager import *
from edit_client import *
from addclient import *
from PyQt5 import *
from addclient_backend import *
from editbackend import *
import mysql.connector
import mysql
from client2 import *
import pandas as pd

port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"

class MainWindow(QWidget, Ui_client):
    def __init__(self, referral, admin):
        super().__init__()
        self.setupUi(self)

        self.referral = referral
        self.admin = admin
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor() 

        self.table_client.setColumnHidden(6, True)
        self.load_table()

        print(self.import_btn)
        self.import_btn.clicked.connect(self.import_data)
        
        
        self.add_btn.clicked.connect(self.add_popup_dialog)
        self.edit_btn.clicked.connect(self.edit_popup_dialog)

        self.search_btn.clicked.connect(self.search_info)

        self.refresh_btn.clicked.connect(self.load_table)

        self.table_client.setSortingEnabled(True)

        self.delete_btn.clicked.connect(self.delete)

        self.export_btn.clicked.connect(self.export)




    def create_connection(self):   
        try:
            connection = mysql.connector.connect(
                host = port,
                user = username,
                password = password1,
                database = dbname
            )
            print("connection successful")
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

    def add_popup_dialog(self):
        referral_code = self.referral
        print("add")
        dialog = QtWidgets.QDialog()
        ui = add_dialog_fx()
        ui.setupUi(dialog)
        ui.line_referral.setText(referral_code)
        if dialog.exec_() == QDialog.Accepted:
            self.load_table()


    def edit_popup_dialog(self):
        referral = self.referral #NEED RETRIEVE REFERRAL
        selection = self.table_client.selectedItems()
        admin = self.admin

        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to edit")
            return

        if admin == 0:
            column = 6
            selected_row = selection[0].row()
            actual_num = self.table_client.item(selected_row, column).text()  
            name = self.table_client.item(selected_row, 1).text()
            ic_number = self.table_client.item(selected_row, 2).text()
            email = self.table_client.item(selected_row, 3).text()
            contact = self.table_client.item(selected_row, 4).text()
            remark = self.table_client.item(selected_row, 5).text()
        else:
            column = 7

            selected_row = selection[0].row()
            actual_num = self.table_client.item(selected_row, column).text()  
            name = self.table_client.item(selected_row, 1).text()
            ic_number = self.table_client.item(selected_row, 3).text()
            email = self.table_client.item(selected_row, 4).text()
            contact = self.table_client.item(selected_row, 5).text()
            remark = self.table_client.item(selected_row, 6).text()

        dialog = QtWidgets.QDialog()
        ui = edit_dialog_fx()
        ui.setupUi(dialog)

        ui.edit_name.setText(name)
        ui.edit_ic.setText(ic_number)
        ui.edit_email.setText(email)
        ui.edit_contact.setText(contact)
        ui.edit_remark.setText(remark)
        ui.edit_referral.setText(referral)

        if dialog.exec_() == QDialog.Accepted:
            ui.edit_client_info(actual_num)
            QMessageBox.information(self, "Success", "Client information updated successfully!")
            self.load_table()
        
    def delete(self):

        admin = self.admin
        if admin == 0:
            column = 6
        else:
            column = 7

        self.table_client.setSelectionMode(QAbstractItemView.MultiSelection)
        selection = self.table_client.selectedItems()
        self.ensure_connection()
        if not selection:
            QMessageBox.warning(self, "Selection error", "Please select a row to delete")
            return
        
        selected_rows = list(set([item.row() for item in selection]))
        names_to_delete = [self.table_client.item(row, 1).text() for row in selected_rows]

        # selected_row = selection[0].row()
        
        # name = self.table_client.item(selected_row, 1).text()
        
        confirm = QMessageBox.question(
        self,
        "Confirm Delete",
        f"Are you sure you want to delete the client: {', '.join(names_to_delete)}?", 
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No
        )
        
        if confirm == QMessageBox.Yes:
            try:
                for row in sorted(selected_rows, reverse=True):
                    num = self.table_client.item(row, column).text()  
                    self.cursor.execute(f"DELETE FROM client WHERE client_id = {num}")
                    self.conn.commit()

            
                self.cursor.execute("SELECT client_id FROM client ORDER BY client_id")
                nums = self.cursor.fetchall()
                for index, (num_value,) in enumerate(nums):
                    
                    self.cursor.execute(f"UPDATE client SET client_id = {index + 1} WHERE client_id = {num_value}")
                self.conn.commit()

                QMessageBox.information(self, "Success", "Client deleted successfully!")
                self.load_table() 

            except mysql.connector.Error as err:
                self.conn.rollback()
                QMessageBox.critical(self, "Database Error", f"Error deleting client: {err}")

    def search_info(self):
        self.ensure_connection()
      
        condition = self.searchbar.text()
        referral_code = self.referral #NEED RETRIEVE REFERRAL

        
            # access = f"SELECT admin FROM staff_acc WHERE referral_code = '{self.referral}'"
            # self.cursor.execute(access)
            # admin = self.cursor.fetchone()

        if self.admin == 0:  # If user is staff
            query = f"""
                SELECT client_name, ic_number, email, phone, remark, client_id FROM client 
                WHERE 
                    (client_name LIKE '%{condition}%' OR
                    ic_number LIKE '%{condition}%' OR
                    email LIKE '%{condition}%' OR
                    phone LIKE '%{condition}%' OR
                    remark LIKE '%{condition}%') AND
                    referral_code = '{referral_code}'
                """
        else:  # If user is admin
            query = f"""
                SELECT client_name, referral_code, ic_number, email, phone, remark, client_id FROM client 
                WHERE 
                    client_name LIKE '%{condition}%' OR
                    ic_number LIKE '%{condition}%' OR
                    email LIKE '%{condition}%' OR
                    phone LIKE '%{condition}%' OR
                    remark LIKE '%{condition}%' OR
                    referral_code LIKE '%{condition}%'
                    """
    
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.search_result(result)
            print(result)

        except mysql.connector.Error as err:
            print(err)
                
        


    # def refresh_data(self):
    #     if self.admin == 0:  # If user is staff
    #             referral_code = self.referral  # Referral code for staff
    #             query = f"SELECT client_name, ic_number, email, phone, remark, client_id FROM client WHERE referral_code = '{referral_code}'"
    #             headers = ["Num", "Name", "IC Number", "Email", "Phone", "Remark", "Actual Num"]  # Headers for staff
    #     else:  # If user is admin
    #         query = f"SELECT client_name, referral_code, ic_number, email, phone, remark, client_id FROM client"
    #         headers = ["Num", "Name", "Referral Code", "IC Number", "Email", "Phone", "Remark", "Actual Num"]  # Headers for admin

        
    #     try:
    #         self.ensure_connection()
    #         self.cursor.execute(query)
    #         data = self.cursor.fetchall()
    #         print(data)
    #         # self.table_client.clearContents()
            
    #         self.load_table(data, headers)

    #     except mysql.connector.Error as err:
    #         print(f"Error executing query: {err}")

        
            
    def load_table(self):
        self.table_client.setRowCount(0)
        self.table_client.setColumnCount(0)
        try:
            access = f"SELECT admin FROM staff_acc WHERE referral_code = '{self.referral}'"
            self.cursor.execute(access)
            admin = self.cursor.fetchone()

            if self.admin == 0:  # If user is staff
                referral_code = self.referral  # Referral code for staff
                query = f"SELECT client_name, ic_number, email, phone, remark, client_id FROM client WHERE referral_code = '{referral_code}'"
                headers = ["Num", "Name", "IC Number", "Email", "Phone", "Remark", "Actual Num"]  # Headers for staff
            else:  # If user is admin
                query = f"SELECT client_name, referral_code, ic_number, email, phone, remark, client_id FROM client"
                headers = ["Num", "Name", "Referral Code", "IC Number", "Email", "Phone", "Remark", "Actual Num"]  # Headers for admin

            
            try:
                self.ensure_connection()
                self.cursor.execute(query)
                data = self.cursor.fetchall()
                print(data)
                self.table_client.clearContents()
                self.table_client.setRowCount(0)
                # self.table_client.setColumnCount(0)

            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")

                
            if len(data) != 0:
                num_rows = len(data)
                num_columns = len(headers)  # Number of columns based on headers
                self.table_client.setRowCount(num_rows)
                self.table_client.setColumnCount(num_columns)

                # Set column headers
                self.table_client.setHorizontalHeaderLabels(headers)

                # Populate table
                for row_num, row_data in enumerate(data):
                    self.table_client.setItem(row_num, 0, QTableWidgetItem(str(row_num + 1)))  # Row numbering
                    for col_num, col_data in enumerate(row_data):
                        self.table_client.setItem(row_num, col_num + 1, QTableWidgetItem(str(col_data)))  # Populate data
                    self.conn.commit()

                if self.admin == 0:
                    self.table_client.setColumnHidden(6, True)
                    
                    self.table_client.setColumnWidth(0, 40)  # "Num" column width
                    self.table_client.setColumnWidth(1, 600)  # "Name" column width
                    self.table_client.setColumnWidth(2, 200)  # "Referral Code" column width (for admin)
                    self.table_client.setColumnWidth(3, 200)  # "IC Number" column width
                    self.table_client.setColumnWidth(4, 350)  # "Email" column width
                    self.table_client.setColumnWidth(5, 200)  # "Phone" column width
                
                else:
                    self.table_client.setColumnHidden(7, True)

                    self.table_client.setColumnWidth(0, 40)  
                    self.table_client.setColumnWidth(1, 600)  
                    self.table_client.setColumnWidth(2, 200)  
                    self.table_client.setColumnWidth(3, 200)  
                    self.table_client.setColumnWidth(4, 350)  
                    self.table_client.setColumnWidth(5, 200)  
                    self.table_client.setColumnWidth(6, 200)  

                for row in range(self.table_client.rowCount()):
                    item = self.table_client.item(row, 0)  # Get item in the "Num" column
                    if item is not None:  # Ensure item exists
                        item.setTextAlignment(Qt.AlignCenter)  # Center align the text in the first column
            else:
                self.table_client.setRowCount(0)  # No data found, clear the table
                return

        except mysql.connector.Error as err:
            print(f"Error retrieving access level: {err}")
    

       


    def search_result(self, result):
        if result:
            self.table_client.setRowCount(0)
            self.table_client.setColumnCount(0)

           

            if self.admin == 0: 
                headers = ["Num", "Name", "IC Number", "Email", "Phone", "Remark", "Actual Num"]
            else: 
                headers = ["Num", "Name", "Referral Code", "IC Number", "Email", "Phone", "Remark", "Actual Num"]   

            self.table_client.setRowCount(len(result))
            self.table_client.setColumnCount(len(headers))
            self.table_client.setHorizontalHeaderLabels(headers)

            for row_num, row_data in enumerate(result):
                self.table_client.setItem(row_num, 0, QTableWidgetItem(str(row_num + 1)))
                for col_num, col_data in enumerate(row_data):
                    self.table_client.setItem(row_num, col_num + 1, QTableWidgetItem(str(col_data)))

            if self.admin == 0:
                self.table_client.setColumnHidden(6, True)
                
                self.table_client.setColumnWidth(0, 40)  # "Num" column width
                self.table_client.setColumnWidth(1, 600)  # "Name" column width
                self.table_client.setColumnWidth(2, 200)  # "Referral Code" column width (for admin)
                self.table_client.setColumnWidth(3, 200)  # "IC Number" column width
                self.table_client.setColumnWidth(4, 350)  # "Email" column width
                self.table_client.setColumnWidth(5, 200)  # "Phone" column width
            
            else:
                self.table_client.setColumnHidden(7, True)

                self.table_client.setColumnWidth(0, 40)  
                self.table_client.setColumnWidth(1, 600)  
                self.table_client.setColumnWidth(2, 200)  
                self.table_client.setColumnWidth(3, 200)  
                self.table_client.setColumnWidth(4, 350)  
                self.table_client.setColumnWidth(5, 200)  
                self.table_client.setColumnWidth(6, 200)  

    
        
        else:
            self.table_client.setRowCount(0)
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
                file_path = f"{directory}/client.xlsx"
                self.export_to_excel( file_path)

                print(f"Selected directory: {directory}")

                

            else:
                print("No directory selected.")

        else:
            print("Operation canceled.")

    def export_to_excel(self, filename):

                    # Get the number of rows and columns in the table
            row_count = self.table_client.rowCount()
            column_count = self.table_client.columnCount()

            # Create a dictionary to hold the table data
            data = {}

            # Extract headers from the table (if available)
            headers = []
            for col in range(column_count):
                header_item = self.table_client.horizontalHeaderItem(col)
                headers.append(header_item.text() if header_item else f"Column {col+1}")

            # Extract the table data
            for col in range(column_count):
                column_data = []
                for row in range(row_count):
                    item = self.table_client.item(row, col)
                    column_data.append(item.text() if item else "")
                data[headers[col]] = column_data

            # Create a DataFrame from the dictionary
            df = pd.DataFrame(data)

            # Export the DataFrame to an Excel file
            df.to_excel(filename, index=False)

            print(f"Data exported successfully to {filename}")

    def import_data(self):

        
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            try:
                # Read the Excel file
                df = pd.read_excel(file_path)

                df.columns = df.columns.str.strip().str.lower()
                
                # Ensure the DataFrame contains all the expected columns
                expected_columns = ['name', 'ic_number', 'email', 'contact', 'remark', 'referral_code']
                if not all(col in df.columns for col in expected_columns):
                    QMessageBox.critical(self, "Error", "The Excel file is missing one or more required columns.")
                    return
                
                # Reorder the columns in the DataFrame to match the database order
                df = df[expected_columns]

                df.fillna('', inplace=True)
                df.dropna(subset=['name', 'email'], inplace=True)

                # Insert each row into the database
                for index, row in df.iterrows():
                    query = """
                        INSERT INTO client (client_name, ic_number, email, phone, remark, referral_code) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    values = (row['name'], row['ic_number'], row['email'], row['contact'], row['remark'], row['referral_code'])

                    self.cursor.execute(query, values)

                self.conn.commit()  # Commit the transaction
                QMessageBox.information(self, "Success", "Data imported successfully!")
                self.load_table()  # Refresh the table

            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")
                self.conn.rollback()

    # def closeEvent(self, event):
    #     if self.conn.is_connected():
    #         self.cursor.close()
    #         self.conn.close()
    #         print("Connection closed")  
    #     event.accept()


    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())