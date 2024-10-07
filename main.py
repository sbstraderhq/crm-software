from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from sbslogin2 import *
from PyQt5.QtGui import *

from update import *
from activity_b import *
import os
from sbslogin_backend import *
    

class MainApp(QMainWindow):

    staff_name = None
    staff_username = None 
    staff_referral = None

    def __init__(self):
        super(MainApp, self).__init__()
        
        print("called")
        self.setWindowIcon(QIcon('icon.ico'))  # Make sure 'icon.ico' is in the same folder as your script
        
        # Set the app's window title
        self.setWindowTitle('CRM')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        

        self.central_layout = QVBoxLayout(central_widget)
        self.central_layout.setContentsMargins(0,0,0,0)

        self.stacked_widget_main = QtWidgets.QStackedWidget()
        self.central_layout.addWidget(self.stacked_widget_main)

        self.login_widget = QWidget()
        self.ui_form = LoginApp(self.login_widget, self)


        self.update_widget = QWidget()

        self.activity_widget = QWidget()


        self.stacked_widget_main.addWidget(self.login_widget)
        self.stacked_widget_main.addWidget(self.update_widget)
        self.stacked_widget_main.addWidget(self.activity_widget)

        
        self.stacked_widget_main.setStyleSheet("background-color: rgb(0,0,0)")
        self.central_layout.setStretch(0, 1)
        self.loginpage()


    def loginpage(self):


        self.stacked_widget_main.setCurrentWidget(self.login_widget)
        self.ui_form.ui.signin_btn.clicked.connect(self.ui_form.login_staff_account)


    def mainpage(self):
        print("called")
        self.staff_name = None
        self.staff_username = None
        self.staff_referral = None

        # self.stacked_widget_main.setCurrentWidget(self.login_widget)
        self.loginpage()

        self.ui_form.ui.username_line.clear()
        self.ui_form.ui.password_line.clear()


    def update_page(self, name , username, referral, admin):
        print("update")
        self.staff_name = name
        self.staff_username = username
        self.staff_referral = referral
        self.admin = admin
        self.updateClass = Ui_update(self)
        self.updateClass.setupUi(self.update_widget)
        self.stacked_widget_main.setCurrentWidget(self.update_widget)

        
    def activity_page(self):
        

        print(self.staff_referral)
        self.activityClass = UiFunction()
        self.activityClass.setupUi(self.activity_widget, self.staff_name , self.staff_username, self.staff_referral, self.admin)
        # self.activityClass.staff_name = self.staff_name
        # self.activityClass.staff_username = self.staff_username
        self.stacked_widget_main.setCurrentWidget(self.activity_widget)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp() 
    main_app.show()
    sys.exit(app.exec_())
