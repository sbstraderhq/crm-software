
from activity import *
from dialog import *
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox, QFileDialog, QHeaderView, QWidget
import pandas as pd
from sbsclientbackend import *
import subprocess
from staff_manager_backend import *
from analysis_backend import *



import mysql.connector
from mysql.connector import Error

host = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
user = "admin"
password = "sbstraderhq123"
database = "sbsdb"


class UiFunction(Ui_Form):
    
    staff_name = None
    staff_username = None
    staff_referral = None

    def setupUi(self, Form , name , username, referral, admin):
        super().setupUi(Form)
        from main import MainApp
        self.ui_form = MainWindow(referral, admin)

        
        
        print(referral)
        self.staff_name = name
        self.staff_username = username
        self.staff_referral = referral
        self.admin = admin

        self.stackedWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.withdrawal_button.clicked.connect(self.wd_button)
        self.deposit_button.clicked.connect(self.dep_button)
        self.refresh_button.clicked.connect(self.ref_button)
        self.add_button.clicked.connect(self.add)
        self.ref_button()
        self.export_button.clicked.connect(self.export)
        self.delete_button.clicked.connect(self.delete)
        self.client_page.clicked.connect(self.change_Client)
        self.activity_page.clicked.connect(self.Change_activity)
        self.signout_button.clicked.connect(self.signout)
        self.import_button.clicked.connect(self.import_dir)
        self.staff_button.clicked.connect(self.change_staff)

        self.searchbar.returnPressed.connect(self.search_table)

        self.main_app = MainApp()

        self.name_label.setText(str(self.staff_name))
        self.username_label.setText(str(self.staff_username))
        self.referral_label.setText(str(self.staff_referral))

        self.analysis_btn.clicked.connect(self.change_analysis)
        
        self.staff_ui = StaffManager()

        self.analysis_ui = Analysis(referral, admin)

        self.check_admin()
    
    def check_admin(self):
        if self.admin == 0:
            self.is_admin = False
            self.staff_button.setVisible(False)
        else:
            self.is_admin = True
            self.staff_button.setVisible(True)



    def Change_activity(self):
        self.stackedWidget_page.setCurrentWidget(self.page)

    def change_Client(self):


        self.ui_form.setupUi(self.client_widget)
        self.stackedWidget_page.setCurrentWidget(self.page_2)

        self.ui_form.conn
        self.ui_form.cursor
        self.ui_form.load_table()

        # self.ui_form.table_client.setColumnHidden(6, True)

        self.ui_form.table_client.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.ui_form.searchbar.returnPressed.connect(self.ui_form.search_info)
       
        self.ui_form.add_btn.clicked.connect(self.ui_form.add_popup_dialog)
        self.ui_form.edit_btn.clicked.connect(self.ui_form.edit_popup_dialog)

        self.ui_form.import_btn.clicked.connect(self.ui_form.import_data)

        self.ui_form.search_btn.clicked.connect(self.ui_form.search_info)

        self.ui_form.refresh_btn.clicked.connect( self.ui_form.load_table)

        self.ui_form.table_client.setSortingEnabled(True)

        self.ui_form.delete_btn.clicked.connect(self.ui_form.delete)

        self.ui_form.export_btn.clicked.connect(self.ui_form.export)

    def change_staff(self):
        
        self.staff_ui.setupUi(self.staff_widget)
        self.stackedWidget_page.setCurrentWidget(self.staff_page)

        self.staff_ui.table_staff.setColumnHidden(6, True)
        self.staff_ui.searchbar.returnPressed.connect(self.staff_ui.search)

        self.conn = self.staff_ui.create_connection()
        self.cursor = self.staff_ui.conn.cursor()

        self.staff_ui.export_btn.clicked.connect(self.staff_ui.export)
        self.staff_ui.refresh_btn.clicked.connect(self.staff_ui.load_table)
        self.staff_ui.add_btn.clicked.connect(self.staff_ui.open_addstaff)
        self.staff_ui.edit_btn.clicked.connect(self.staff_ui.open_editstaff)
        self.staff_ui.delete_btn.clicked.connect(self.staff_ui.delete_stafF)
        self.staff_ui.search_btn.clicked.connect(self.staff_ui.search)
        self.staff_ui.table_staff.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)


        self.staff_ui.load_table()

        
        # self.staff_ui.table_staff.resizeColumnsToContents()

    def change_analysis(self):

        self.analysis_ui.setupUi(self.analysis_widget)
        self.stackedWidget_page.setCurrentWidget(self.analysis_page)

        self.conn = self.analysis_ui.create_connection()
        self.cursor = self.analysis_ui.conn.cursor()
        

        
    def test(self):
        print("test called")


    def delete(self):
        from dialog import DeleteTransactionDialog
        thedialog = DeleteTransactionDialog(current=self.stackedWidget.currentIndex())
        thedialog.setFixedSize(thedialog.size())
        
        result = thedialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            self.ref_button()

        else:
            print("not call refresh")
        
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
            
                nametable = None
                table_widget = None

                if self.stackedWidget.currentWidget() == self.page_3:
                   
                    nametable = "deposit"
                    # Here you can call the export_to_excel function and pass the directory path
                    file_path = f"{directory}/{nametable}.xlsx"
                    export_to_excel(self.table_deposit, file_path)
            
        
                elif self.stackedWidget.currentWidget() == self.page_4:
 
                    nametable = "withdrawal"
                    # Here you can call the export_to_excel function and pass the directory path
                    file_path = f"{directory}/{nametable}.xlsx"
                    export_to_excel(self.table_withdrawal, file_path)

      

                print(f"Selected directory: {directory}")

                

            else:
                print("No directory selected.")

        else:
            print("Operation canceled.")

    def wd_button(self):
        
        self.stackedWidget.setCurrentWidget(self.page_4)
        self.table_withdrawal.sortItems(-1)
        self.table_withdrawal.clearContents()
        ref_code = self.referral_label.text()

        wd_func(self.table_withdrawal , ref_code, self.admin)

    def dep_button(self):

        self.stackedWidget.setCurrentWidget(self.page_3)
        self.table_deposit.sortItems(-1)
        self.table_deposit.clearContents()
        ref_code = self.referral_label.text()
        dep_func(self.table_deposit, ref_code, self.admin)

    def ref_button(self):
        page = self.stackedWidget.currentWidget()
        if page == self.page_3:
            pagename = "deposit"
            self.table_deposit.sortItems(-1)
            self.table_deposit.clearContents()
        else:
            pagename = "withdrawal"
            self.table_withdrawal.sortItems(-1)
            self.table_withdrawal.clearContents()

        
        ref_func(pagename, self, self.staff_referral, self.admin)

    #####################################################################################################

    def search_table(self):
        page = self.stackedWidget.currentWidget()
        if page == self.page_3:
            pagename = "deposit"
            db = 'deposit'
            amount = 'amount_deposit'
            self.table_deposit.sortItems(-1)
            self.table_deposit.clearContents()
        else:
            pagename = "withdrawal"
            db = 'withdrawal'
            amount = 'amount_withdraw'
            self.table_withdrawal.sortItems(-1)
            self.table_withdrawal.clearContents()

        if pagename == "deposit":
            
            self.search_fetch(self.table_deposit, self.staff_referral, self.admin, db, amount)

        elif pagename == "withdrawal":
            
            self.search_fetch(self.table_withdrawal, self.staff_referral, self.admin, db, amount)

        else:
            print("hmm")
        

    def search_fetch(self, table, referral, admin, db, amount):
        condition = self.searchbar.text()
        referral = self.staff_referral
        admin = self.admin
        

        if admin == 0:
            query = f"""
            SELECT * FROM {db} 
            WHERE 
                (transaction_id LIKE '%{condition}%' OR
                client_id LIKE '%{condition}%' OR
                client_name LIKE '%{condition}%' OR
                referral_code LIKE '%{condition}%' OR
                {amount} LIKE '%{condition}%' OR
                transaction_date LIKE '%{condition}%') AND
                referral_code = '{referral}'
            """

        else:
            query = f"""
            SELECT * FROM {db} 
            WHERE 
                transaction_id LIKE '%{condition}%' OR
                client_id LIKE '%{condition}%' OR
                client_name LIKE '%{condition}%' OR
                referral_code LIKE '%{condition}%' OR
                {amount} LIKE '%{condition}%' OR
                transaction_date LIKE '%{condition}%'
            """

        conn = check_connection()
    

        results = []

        if conn:
            try:
                cursor = conn.cursor()
                
                cursor.execute(query)
                results = cursor.fetchall()
                
            except Error as e:
                print(f"Error: {e}")

            finally:
                conn.close()

        table.setRowCount(0)
        table.setSortingEnabled(False)

    
        # Populate the table widget

        table.setRowCount(len(results))
        for row_idx, row in enumerate(results):
        # row contains (client_id, client_name, referral_code)
            transaction_id, client_id, client_name, referral_code, Depo, Date = row

            
            date_item = QTableWidgetItem(str(Date))
            date_item.setData(0, QDate.fromString(str(Date), 'yyyy-MM-dd')) 

            trans_id = QtWidgets.QTableWidgetItem()
            trans_id.setData(QtCore.Qt.DisplayRole, int(transaction_id))
            
        # Populate each column based on the index
            table.setItem(row_idx, 0, trans_id)  # ID column
            table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(client_name)))      # Name column
            table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(client_id)))
            table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(referral_code))
            table.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(date_item))
            table.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(str(Depo)))

        table.setSortingEnabled(True)

        







    def add(self):
        referral_code = self.referral_label.text()
        from dialog import dialogFunc
        thedialog = QtWidgets.QDialog()
        ui = dialogFunc(referral_code)
        ui.setupUi(thedialog)
        thedialog.setFixedSize(thedialog.size())
        
        result = thedialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            self.ref_button()

        else:
            print("not call refresh")

    def closeapp(self):
        self.close()

    def closeEvent(self, event):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Sign Out")
        msg_box.setText("Are you sure you want to sign out?")
        
        # Add Yes and No buttons
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)  # Default is No

        # Execute the message box and check the user's choice
        choice = msg_box.exec_()

        if choice == QMessageBox.Yes:
            if self.conn.is_connected():
                    self.cursor.close()
                    self.conn.close()
                    print("conn closed")

        event.accept()


    def signout(self):
        # Create a QMessageBox to ask the user if they want to sign out
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Sign Out")
        msg_box.setText("Are you sure you want to sign out?")
        
        # Add Yes and No buttons
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)  # Default is No

        # Execute the message box and check the user's choice
        choice = msg_box.exec_()

        if choice == QMessageBox.Yes:

            conn = check_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    query = "UPDATE staff_acc SET logged_in = 0 WHERE username = %s"
                    cursor.execute(query, (self.staff_username,))
                    conn.commit()

                except mysql.connector.Error as err:
                    print(f"Error logging out: {err}")

                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
                        
                        print("conn closed")
                    QtWidgets.QApplication.quit()
            # if getattr(sys, 'frozen', False):
            #     # If the application is running as a .exe
            #     executable_path = sys.executable
            #     QtWidgets.QApplication.quit()
            #     # os.startfile(executable_path)
            #     subprocess.Popen(r'Client Manager.exe')  # Restart the executable
            # else:
            #     # If the application is running as a script
            #     QtWidgets.QApplication.quit()
            #     python = sys.executable
            #     os.execl(python, python, *sys.argv)

            
        else:
            # If user clicks No, do nothing
            print("Cancelled sign out.")
            
            
    def import_todb(self, file_path):
        try:
            # Step 1: Read the Excel file
            df = pd.read_excel(file_path)

            connection = check_connection()
            if connection.is_connected():
                cursor = connection.cursor()

                # Step 3: Insert data into the table (assuming table has columns matching Excel file structure)
                for index, row in df.iterrows():
                    # Modify the query and column names as per your table structure
                    query = """
                        INSERT INTO deposit (client_name, referral_code, amount_deposit, transaction_date)
                        VALUES (%s, %s, %s,%s)
                    """
                    values = (row['client_name'], row['referral_code'], row['amount_deposit'],  row['transaction_date'])  # Adjust as per your column names
                    cursor.execute(query, values)

                connection.commit()
                print("Data inserted successfully.")

        except Error as e:
            print(f"Error: {e}")
            self.show_message("Error", f"Database error: {e}")
        except KeyError as e:
            print(f"Column error: {e}")
            self.show_message("Error", f"Missing column: {e}")
        except Exception as e:
            print(f"Error: {e}")
            self.show_message("Error", f"An error occurred: {e}")
            

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning if "Error" in title else QMessageBox.Information)
        msg_box.exec_()

    def import_dir(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Choose Directory")
        msg_box.setText("Please choose a directory to import the Excel file.")
    
        # Add custom buttons
        save_button = msg_box.addButton("Choose Directory", QMessageBox.ActionRole)
        cancel_button = msg_box.addButton(QMessageBox.Cancel)

        # Show the message box and wait for user input
        msg_box.exec_()

    

            # Check which button was clicked
        if msg_box.clickedButton() == save_button:
            # Open the QFileDialog to select a directory
            directory, _ = QFileDialog.getOpenFileName(None, "Select File", "", "All Files (*)")

            if directory:

                # Here you can call the export_to_excel function and pass the directory path
                
                self.import_todb( directory)
        
        
                print(f"Selected directory: {directory}")

                

            else:
                print("No directory selected.")

        else:
            print("Operation canceled.")





        


        


def wd_func(table_widget, ref_code, admin):

    #tomorrow task : 
    #checkin connection to databases (func 1)
    #retrieve data from db
    #arrange data into table


    if admin == 0:
        query = f"SELECT * FROM withdrawal WHERE referral_code= '{ref_code}'"
    else:
        query = "SELECT * FROM withdrawal"


    conn = check_connection()
    

    results = []

    if conn:
        try:
            cursor = conn.cursor()
            
            cursor.execute(query)
            results = cursor.fetchall()
            print("sucessful depo")
            
        except Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    table_widget.setRowCount(0)
    table_widget.setSortingEnabled(False)

 
    # Populate the table widget

    table_widget.setRowCount(len(results))
    for row_idx, row in enumerate(results):
    # row contains (client_id, client_name, referral_code)
        transaction_id, client_id, client_name, referral_code, Depo, Date = row

        
        date_item = QTableWidgetItem(str(Date))
        date_item.setData(0, QDate.fromString(str(Date), 'yyyy-MM-dd')) 

        trans_id = QtWidgets.QTableWidgetItem()
        trans_id.setData(QtCore.Qt.DisplayRole, int(transaction_id))
        
    # Populate each column based on the index
        table_widget.setItem(row_idx, 0, trans_id)  # ID column
        table_widget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(client_name)))      # Name column
        table_widget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(client_id)))
        table_widget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(referral_code))
        table_widget.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(date_item))
        table_widget.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(str(Depo)))

    table_widget.setSortingEnabled(True)


def dep_func(table_widget, ref_code, admin):
    conn = check_connection()

    if admin == 0:
        query = f"SELECT * FROM deposit WHERE referral_code= '{ref_code}'"
    else:
        query = "SELECT * FROM deposit"

    results = []

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            print(ref_code)
            
            
        except Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    

    # Populate the table widget
    table_widget.setRowCount(len(results))
    for row_idx, row in enumerate(results):
    # row contains (client_id, client_name, referral_code)
        transaction_id, client_id, client_name, referral_code, Depo, Date = row

        date_item = QTableWidgetItem(str(Date))
        date_item.setData(0, QDate.fromString(str(Date), 'yyyy-MM-dd')) 

        trans_id = QtWidgets.QTableWidgetItem()
        trans_id.setData(QtCore.Qt.DisplayRole, int(transaction_id))

    # Populate each column based on the index
        table_widget.setItem(row_idx, 0, trans_id)  # ID column
        table_widget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(str(client_name)))      # Name column
        table_widget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(str(client_id)))
        table_widget.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(referral_code))
        table_widget.setItem(row_idx, 4, QtWidgets.QTableWidgetItem(date_item))
        table_widget.setItem(row_idx, 5, QtWidgets.QTableWidgetItem(str(Depo)))
        
    table_widget.setSortingEnabled(True)


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


def ref_func(pagename, self , referral, admin):

    conn = check_connection()
    
    if pagename == "deposit":
       
        
        dep_func(self.table_deposit, referral, admin)

    elif pagename == "withdrawal":
        
        wd_func(self.table_withdrawal,referral, admin)

    else:
        print("hmm")
    

def export_to_excel(table_widget, filename):


    # Get the number of rows and columns in the table
    row_count = table_widget.rowCount()
    column_count = table_widget.columnCount()

    # Create a dictionary to hold the table data
    data = {}

    # Extract headers from the table (if available)
    headers = []
    for col in range(column_count):
        header_item = table_widget.horizontalHeaderItem(col)
        headers.append(header_item.text() if header_item else f"Column {col+1}")

    # Extract the table data
    for col in range(column_count):
        column_data = []
        for row in range(row_count):
            item = table_widget.item(row, col)
            column_data.append(item.text() if item else "")
        data[headers[col]] = column_data

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Export the DataFrame to an Excel file
    df.to_excel(filename, index=False)

    print(f"Data exported successfully to {filename}")




