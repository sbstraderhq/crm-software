# sbslogin_app.py

import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from sbslogin2 import *
import yagmail



port = "sbsmanagerdb.c1gcwi06wgyq.ap-southeast-5.rds.amazonaws.com"
username = "admin"
password1 = "sbstraderhq123"
dbname = "sbsdb"


class LoginApp(QWidget):
    def __init__(self , widget, main_app):
        super().__init__()

        self.main_app = main_app
        self.widget = widget
        self.ui = LoginFunct()
        self.ui.setupUi(self.widget)

        # conn and cursor
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()
      
        self.ui.register_btn.clicked.connect(self.show_registration_page)
     
        self.ui.submit_btn.clicked.connect(self.register_staff_account)

        self.ui.signin_btn.clicked.connect(self.login_staff_account)

        self.ui.reqcode_btn.clicked.connect(self.send_email)

       

    


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

    def show_registration_page(self):
        
        self.ui.stackedWidget.setCurrentIndex(1)

    def register_staff_account(self):
       
        username = self.ui.username_line_2.text()
        name = self.ui.name_line.text()
        password = self.ui.password_line_2.text()
        email = self.ui.email_line.text()
        ref_code = self.ui.code_line_2.text()

        
        if not username or not name or not password or not email:
            QMessageBox.warning(self, 'Input Error', 'All fields must be filled!')
            return
        
        try:
            conn = self.create_connection()

            if conn:

                cursor = conn.cursor()
                sql = f"SELECT code FROM code_register WHERE email= %s "
                email_staff = self.ui.email_line.text()
                
                cursor.execute(sql, (email_staff,))
                print(email_staff)
                result = cursor.fetchall()


            

        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()

        enter_code = self.ui.code_line_3.text()
        result_code = result[0][0]
        if result_code != enter_code:
            QMessageBox.information(self, 'Failed', 'Wrong code!')
            print(result)
            return
        
        
       
        try:
           
            query = """
                INSERT INTO staff_acc (username, name, password, email, referral_code) 
                VALUES (%s, %s, %s, %s,%s)
            """
            values = (username, name, password, email, ref_code )
            self.cursor.execute(query,  values)
            self.conn.commit()

            QMessageBox.information(self, 'Success', 'Staff account registered successfully!')

            self.ui.username_line_2.clear()
            self.ui.name_line.clear()
            self.ui.password_line_2.clear()
            self.ui.email_line.clear()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f"Error: {err}")
        finally:
            self.cursor.close()
            self.conn.close()

    def login_staff_account(self):
        print("login")
        username = self.ui.username_line.text()
        password = self.ui.password_line.text()

        conn = self.create_connection()

        if conn:

            print("conn jadi")
            if not username or not password:
                QMessageBox.warning(self, 'Input Error', 'Both username and password are required!')
                return
        
            try:

                print("try jadi")
                cursor = conn.cursor()
                query = "select * from staff_acc where username = %s and password = %s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()

                if result:
                    logged_in = result[5]
                    username = result[1]
                    name = result[2]
                    referral = result[6]
                    admin = result[7]

                    # if logged_in == 1:
                    #     QMessageBox.warning(self, 'Login Error', 'This account is already logged in elsewhere.')
                    #     return
                
                    #else:
                    # update_login = "update staff_acc set logged_in = 1 where username = %s"
                    # cursor.execute(update_login, (username,))
                    # conn.commit()
                
                    self.open_main_window(name, username, referral, admin)

                else:
                    QMessageBox.warning(self, 'Login Error', 'Invalid username or password.')

            except mysql.connector.Error as err:
                QMessageBox.critical(self, 'Database error', f"Error: {err}")

            finally:
                conn.close()

    def open_main_window(self, name, username, referral, admin):
        
        
        
        self.main_window = self.main_app.update_page(name, username, referral, admin)
        

        self.conn.close()
    
    def send_email(self):
        # Gather inputs
        recipient_admin = "fareeq1411@gmail.com"
        code = generator()
        recipient_staff = self.ui.email_line.text()
        
        subject = "Your generated code for registration is:" + str(code) 

        if not recipient_staff or not subject:
            QMessageBox.warning(self, 'Input Error', 'email fields are required!')
            return

        # Define your sender email and setup yagmail
        sender_email = "izfat041394@gmail.com"   # Replace with your email
        sender_password = "ryflcdoxjzkhdlfi"      # Replace with your app-specific password

        try:

            conn = self.create_connection()

            if conn:
                cursor = conn.cursor()
                    
                query2 = "SELECT email FROM code_register"
                cursor.execute(query2)

                check_email = cursor.fetchall()

                print(check_email)

                for email_tuple in check_email:
                    email = email_tuple[0]
                    if recipient_staff == email:
                        print(email)
                        QMessageBox.information(self, 'Failed', 'You already register code')
                        return

                print("Email not found.")

        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Failed to send email: {e}")

        finally:
            cursor.close()
            conn.close()

        # Initialize yagmail
        yag = yagmail.SMTP(sender_email, sender_password)

        try:

            conn = self.create_connection()

            # Send the email
            yag.send(
                to=recipient_admin,
                subject=subject,
                contents="This is the staff email:" + str(recipient_staff)  # Customize this as needed
            )
            QMessageBox.information(self, 'Success', 'wait for the Administrator to forward you the code!')

            if conn:
                cursor = conn.cursor()
                    
                query = f"INSERT INTO code_register (email , code) VALUES (%s, %s)"
                value = (recipient_staff, code)

                cursor.execute(query, value)
                conn.commit()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Failed to send email: {e}")

        finally:
            cursor.close()
            conn.close()

        
        


   

def generator():

    import random
    random_numbers = str(random.randint(10000, 99999))
    
    return random_numbers

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LoginApp()
#     window.show()
#     sys.exit(app.exec_())

