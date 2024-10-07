# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activity.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import os
import sys
from PyQt5.QtWidgets import QPushButton, QSizePolicy

class Ui_Form(object):
    def setupUi(self, Form):

        if getattr(sys, 'frozen', False):

            base_path = sys._MEIPASS
        else:

            base_path = os.path.dirname(os.path.abspath(__file__))

        self.refresh_path = os.path.join(base_path, 'image', 'refresh.png')
        Form.setObjectName("Form")
        Form.resize(850, 666)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color: rgb(182, 216, 255);")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        self.label_6 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name_label = QtWidgets.QLabel(self.widget_2)
        self.name_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_label.setObjectName("name_label")
        self.verticalLayout_3.addWidget(self.name_label)
        self.username_label = QtWidgets.QLabel(self.widget_2)
        self.username_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.username_label.setObjectName("username_label")
        self.verticalLayout_3.addWidget(self.username_label)

        self.referral_label = QtWidgets.QLabel(self.widget_2)
        self.referral_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.referral_label.setObjectName("referral_label")
        self.verticalLayout_3.addWidget(self.referral_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 100)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.activity_page = QtWidgets.QPushButton(self.widget_2)
        self.activity_page.setMinimumSize(QtCore.QSize(0, 50))
        self.activity_page.setMaximumHeight(85)
        self.activity_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.activity_page.setAutoFillBackground(False)
        self.activity_page.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    background-color: rgba(255, 255, 255, 161);\n"
"border: solid;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    \n"
"\n"
"\n"
"")
        self.activity_page.setObjectName("activity_page")
        self.verticalLayout.addWidget(self.activity_page)
        self.analysis_page = QtWidgets.QPushButton(self.widget_2)
        self.analysis_page.setMinimumSize(QtCore.QSize(0, 50))
        self.analysis_page.setMaximumHeight(85)
        self.analysis_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.analysis_page.setAutoFillBackground(False)
        self.analysis_page.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    background-color: rgba(255, 255, 255, 161);\n"
"border: solid;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    \n"
"\n"
"\n"
"\n"
"\n"
"")
        self.analysis_page.setObjectName("analysis_page")
        self.verticalLayout.addWidget(self.analysis_page)
        self.client_page = QtWidgets.QPushButton(self.widget_2)
        self.client_page.setMinimumSize(QtCore.QSize(0, 50))
        self.client_page.setMaximumHeight(85)
        self.client_page.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.client_page.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    background-color: rgba(255, 255, 255, 161);\n"
"border: solid;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    \n"
"\n"
"\n"
"")
        self.client_page.setObjectName("client_page")
        self.verticalLayout.addWidget(self.client_page)

        ######################################## button ##########################################
        self.staff_button = QtWidgets.QPushButton(self.widget_2)
        self.staff_button.setMinimumSize(QtCore.QSize(0, 50))
        self.staff_button.setMaximumHeight(85)
        self.staff_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.staff_button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    background-color: rgba(255, 255, 255, 161);\n"
"border: solid;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    \n"
"\n"
"\n"
"")
        self.staff_button.setObjectName("staff_button")
        self.verticalLayout.addWidget(self.staff_button)
        #########################################################################################



        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.signout_button = QtWidgets.QPushButton(self.widget_2)
        self.signout_button.setMinimumSize(QtCore.QSize(0, 50))
        self.signout_button.setMaximumHeight(85)
        self.signout_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.signout_button.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    background-color: rgba(255, 255, 255, 161);\n"
"border: solid;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"    \n"
"\n"
"\n"
"")
        self.signout_button.setObjectName("signout_button")
        self.verticalLayout_4.addWidget(self.signout_button)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setStyleSheet("color: rgba(55, 55, 55, 224);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setStyleSheet("color: rgba(0, 0, 0, 186);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        #self.horizontalLayout_5.addWidget(self.widget_2)

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        
        self.stackedWidget_page = QtWidgets.QStackedWidget(Form)
        self.stackedWidget_page.setObjectName("stackedWidget_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        # spacerItem2 = QtWidgets.QSpacerItem(20, 494, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout_8.addItem(spacerItem2)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.export_button = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy)
        self.export_button.setMinimumSize(QtCore.QSize(120, 40))
        self.export_button.setMaximumSize(QtCore.QSize(120, 40))
        self.export_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgba(166, 255, 142, 186);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.export_button.setObjectName("export_button")
        self.horizontalLayout_6.addWidget(self.export_button)
        self.import_button = QtWidgets.QPushButton(self.widget)
        self.import_button.setMinimumSize(QtCore.QSize(120, 40))
        self.import_button.setMaximumSize(QtCore.QSize(120, 40))
        self.import_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgba(166, 255, 142, 186);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_6.addWidget(self.import_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        


        self.searchbar = QtWidgets.QLineEdit(self.widget)
        self.searchbar.setMinimumSize(QtCore.QSize(160, 30))
        self.searchbar.setStyleSheet("border:1px solid black;\n"
"   background-color: rgb(230, 230, 230);\n"
"")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_6.addWidget(self.searchbar)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_button = QtWidgets.QPushButton(self.widget)
        self.add_button.setMinimumSize(QtCore.QSize(120, 40))
        self.add_button.setMaximumSize(QtCore.QSize(120, 40))
        self.add_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgba(255, 114, 95, 207);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_3.addWidget(self.add_button)

        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setMinimumSize(QtCore.QSize(120, 40))
        self.delete_button.setMaximumSize(QtCore.QSize(120, 40))
        self.delete_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    \n"
"    background-color: rgba(255, 114, 95, 207);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_3.addWidget(self.delete_button)

        spacerItem4 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.refresh_button = QtWidgets.QPushButton(self.widget)
        self.refresh_button.setMinimumSize(QtCore.QSize(120, 40))
        self.refresh_button.setMaximumSize(QtCore.QSize(120, 40))
        self.refresh_button.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"    color: rgb(0,0,0);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    color: rgb(0,0,0);\n"
"    \n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon(self.refresh_path)
        self.refresh_button.setIcon(icon)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout_2.addWidget(self.refresh_button)
        
        self.deposit_button = QtWidgets.QPushButton(self.widget)
        self.deposit_button.setMinimumSize(QtCore.QSize(120, 40))
        self.deposit_button.setMaximumSize(QtCore.QSize(120, 40))
        self.deposit_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"\n"
"    background-color: rgba(173, 173, 173, 145);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.deposit_button.setObjectName("deposit_button")
        self.horizontalLayout_2.addWidget(self.deposit_button)
        self.withdrawal_button = QtWidgets.QPushButton(self.widget)
        self.withdrawal_button.setMinimumSize(QtCore.QSize(120, 40))
        self.withdrawal_button.setMaximumSize(QtCore.QSize(120, 40))
        self.withdrawal_button.setStyleSheet("QPushButton{\n"
"\n"
"    border: 1px solid black;\n"
"    \n"
"    background-color: rgba(173, 173, 173, 145);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(188, 255, 195, 196);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    \n"
"    background-color: rgba(255, 176, 169, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.withdrawal_button.setObjectName("withdrawal_button")
        self.horizontalLayout_2.addWidget(self.withdrawal_button)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        

        
        

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.table_deposit = QtWidgets.QTableWidget(self.page_3)
        self.table_deposit.setStyleSheet("color: rgb(0, 0, 0);")
        self.table_deposit.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_deposit.setObjectName("table_deposit")
        self.table_deposit.setWordWrap(True)
       

        self.table_deposit.setColumnCount(6)
        self.table_deposit.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_deposit.setItem(0, 5, item)
        # Set the width of a specific column
        self.table_deposit.setColumnWidth(0, 159)
        self.table_deposit.setColumnWidth(1, 300)
        self.table_deposit.setColumnWidth(2, 150)
        self.table_deposit.setColumnWidth(3, 150)
        self.table_deposit.setColumnWidth(4, 200)
        self.table_deposit.setColumnWidth(5, 150)
        

        self.table_deposit.horizontalHeader().setCascadingSectionResizes(False)
        
        self.table_deposit.horizontalHeader().setMinimumSectionSize(19)
        self.table_deposit.horizontalHeader().setSortIndicatorShown(False)
        self.table_deposit.horizontalHeader().setStretchLastSection(True)
        self.table_deposit.verticalHeader().setCascadingSectionResizes(False)
        self.table_deposit.setSortingEnabled(True)
        self.verticalLayout_9.addWidget(self.table_deposit)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.table_withdrawal = QtWidgets.QTableWidget(self.page_4)
        self.table_withdrawal.setStyleSheet("color: rgb(0, 0, 0);")
        self.table_withdrawal.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_withdrawal.setObjectName("table_withdrawal")
        self.table_withdrawal.setColumnCount(6)
        self.table_withdrawal.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_withdrawal.setHorizontalHeaderItem(5, item)

        self.table_withdrawal.horizontalHeader().setStretchLastSection(True)
        
        self.table_withdrawal.setColumnWidth(0, 159)
        self.table_withdrawal.setColumnWidth(1, 300)
        self.table_withdrawal.setColumnWidth(2, 150)
        self.table_withdrawal.setColumnWidth(3, 150)
        self.table_withdrawal.setColumnWidth(4, 200)
        self.table_withdrawal.setColumnWidth(5, 150)
        self.table_withdrawal.setSortingEnabled(True)
        self.verticalLayout_10.addWidget(self.table_withdrawal)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.widget)

  
        self.verticalLayout_7.addWidget(self.widget)
        

        self.stackedWidget_page.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.client_widget = QWidget(self.page_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_7")
        self.stackedWidget_page.addWidget(self.page_2)
        self.verticalLayout_11.addWidget(self.client_widget)

        self.horizontalLayout_5.addWidget(self.widget_2)
        self.horizontalLayout_5.addWidget(self.stackedWidget_page)


        ############################################################ pertukaran #################################################
        self.staff_page = QtWidgets.QWidget()
        self.staff_page.setObjectName("staff_page")
        self.staff_widget = QWidget(self.staff_page)
        self.staff_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.staff_page)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_7")
        self.stackedWidget_page.addWidget(self.staff_page)
        self.verticalLayout_12.addWidget(self.staff_widget)

        #############################################################################################################################


        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Name:"))
        self.label_5.setText(_translate("Form", "Referral Code:"))
        self.name_label.setText(_translate("Form", "Text"))
        self.username_label.setText(_translate("Form", "Text"))
        self.activity_page.setText(_translate("Form", "Activity"))
        self.analysis_page.setText(_translate("Form", "Analysis"))
        self.client_page.setText(_translate("Form", "Client"))
        self.staff_button.setText(_translate("Form", "Staff"))
        self.signout_button.setText(_translate("Form", "Sign out"))
        self.label_2.setText(_translate("Form", "connection:"))
        self.label_3.setText(_translate("Form", "label load"))
        self.label.setText(_translate("Form", "Activity Dashboard"))
        self.export_button.setText(_translate("Form", "Export"))
        self.refresh_button.setText(_translate("Form", " Refresh"))
        self.add_button.setText(_translate("Form", "Add"))
        self.deposit_button.setText(_translate("Form", "Deposit"))
        self.withdrawal_button.setText(_translate("Form", "Withdrawal"))
        item = self.table_deposit.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Transaction ID"))
        item = self.table_deposit.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.table_deposit.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Client ID "))
        item = self.table_deposit.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Referral Code:"))
        item = self.table_deposit.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date"))
        item = self.table_deposit.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Amt. Deposit"))
        __sortingEnabled = self.table_deposit.isSortingEnabled()
        self.table_deposit.setSortingEnabled(False)
        self.table_deposit.setSortingEnabled(__sortingEnabled)
        item = self.table_withdrawal.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Transaction ID"))
        item = self.table_withdrawal.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.table_withdrawal.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Client ID"))
        item = self.table_withdrawal.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Referral Code"))
        item = self.table_withdrawal.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date"))
        item = self.table_withdrawal.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Amt. Withdraw"))
        self.delete_button.setText(_translate("Form", "Delete"))
        self.label_6.setText(_translate("Form", "Username:"))
        self.referral_label.setText(_translate("Form", "Text"))
        self.import_button.setText(_translate("Form", "Import"))

        self.searchbar.setPlaceholderText(_translate("Form", "Search..."))
