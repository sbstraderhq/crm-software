# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sbs client manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(200, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setStyleSheet("background-color: rgb(182, 216, 255);")
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.staff_account = QtWidgets.QHBoxLayout()
        self.staff_account.setContentsMargins(-1, 5, -1, -1)
        self.staff_account.setObjectName("staff_account")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.staff_account.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name_label = QtWidgets.QLabel(self.sidebar)
        self.name_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.name_label.setObjectName("name_label")
        self.verticalLayout_3.addWidget(self.name_label)
        self.username_label = QtWidgets.QLabel(self.sidebar)
        self.username_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.username_label.setObjectName("username_label")
        self.verticalLayout_3.addWidget(self.username_label)
        self.staff_account.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.staff_account)
        spacerItem = QtWidgets.QSpacerItem(179, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.activity_btn = QtWidgets.QPushButton(self.sidebar)
        self.activity_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.activity_btn.setAutoFillBackground(False)
        self.activity_btn.setStyleSheet("QPushButton{\n"
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
        self.activity_btn.setObjectName("activity_btn")
        self.verticalLayout.addWidget(self.activity_btn)
        self.analysis_btn = QtWidgets.QPushButton(self.sidebar)
        self.analysis_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.analysis_btn.setAutoFillBackground(False)
        self.analysis_btn.setStyleSheet("QPushButton{\n"
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
        self.analysis_btn.setObjectName("analysis_btn")
        self.verticalLayout.addWidget(self.analysis_btn)
        self.client_btn = QtWidgets.QPushButton(self.sidebar)
        self.client_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.client_btn.setStyleSheet("QPushButton{\n"
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
        self.client_btn.setObjectName("client_btn")
        self.verticalLayout.addWidget(self.client_btn)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.signout_btn = QtWidgets.QPushButton(self.sidebar)
        self.signout_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.signout_btn.setStyleSheet("QPushButton{\n"
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
        self.signout_btn.setObjectName("signout_btn")
        self.verticalLayout_4.addWidget(self.signout_btn)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addWidget(self.sidebar)
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setStyleSheet("background-color:white;\n"
"\n"
"QTableWidget{}\n"
"\n"
"")
        self.menu.setObjectName("menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.header = QtWidgets.QWidget(self.menu)
        self.header.setStyleSheet("QWidget{\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    background-color: rgb(213, 213, 213);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"    background-color: rgb(166, 166, 166);\n"
"}\n"
"")
        self.header.setObjectName("header")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pagename = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(24)
        self.pagename.setFont(font)
        self.pagename.setStyleSheet("border-radius:10px;\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"text-align:hcenter;\n"
"")
        self.pagename.setAlignment(QtCore.Qt.AlignCenter)
        self.pagename.setObjectName("pagename")
        self.horizontalLayout.addWidget(self.pagename)
        spacerItem3 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.export_btn = QtWidgets.QPushButton(self.header)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sys client management/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_5.addWidget(self.export_btn)
        self.delete_btn = QtWidgets.QPushButton(self.header)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sys client management/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_5.addWidget(self.delete_btn)
        spacerItem4 = QtWidgets.QSpacerItem(468, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_btn = QtWidgets.QPushButton(self.header)
        self.add_btn.setMinimumSize(QtCore.QSize(50, 21))
        self.add_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sys client management/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon2)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_4.addWidget(self.add_btn)
        self.edit_btn = QtWidgets.QPushButton(self.header)
        self.edit_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sys client management/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon3)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_4.addWidget(self.edit_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.header)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/sys client management/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon4)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_4.addWidget(self.refresh_btn)
        spacerItem5 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchbar = QtWidgets.QLineEdit(self.header)
        self.searchbar.setMinimumSize(QtCore.QSize(160, 23))
        self.searchbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_3.addWidget(self.searchbar)
        self.search_btn = QtWidgets.QPushButton(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(23, 23))
        self.search_btn.setMaximumSize(QtCore.QSize(21, 21))
        self.search_btn.setStyleSheet("border-radius:9px;")
        self.search_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/sys client management/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon5)
        self.search_btn.setIconSize(QtCore.QSize(16, 16))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.header)
        self.table_client = QtWidgets.QTableWidget(self.menu)
        self.table_client.setStyleSheet("QHeaderView::section{\n"
"    background-color: rgb(195, 195, 195);;\n"
"}\n"
"QTableWidget::Item{ \n"
"    color:black;    \n"
"}\n"
"")
        self.table_client.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_client.setObjectName("table_client")
        self.table_client.setColumnCount(7)
        self.table_client.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(6, item)
        self.table_client.horizontalHeader().setVisible(True)
        self.table_client.horizontalHeader().setCascadingSectionResizes(False)
        self.table_client.horizontalHeader().setStretchLastSection(True)
        self.table_client.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.table_client)
        self.horizontalLayout_2.addWidget(self.menu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Manager"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.name_label.setText(_translate("MainWindow", "Text"))
        self.username_label.setText(_translate("MainWindow", "Text"))
        self.activity_btn.setText(_translate("MainWindow", "Activity"))
        self.analysis_btn.setText(_translate("MainWindow", "Analysis"))
        self.client_btn.setText(_translate("MainWindow", "Client"))
        self.signout_btn.setText(_translate("MainWindow", "Sign out"))
        self.pagename.setText(_translate("MainWindow", "CLIENT"))
        self.export_btn.setText(_translate("MainWindow", "Export"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.table_client.setSortingEnabled(False)
        item = self.table_client.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Num"))
        item = self.table_client.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_client.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IC Number"))
        item = self.table_client.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_client.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.table_client.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Remark"))
        item = self.table_client.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Actual Num"))
import clientsysmanagenent_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
