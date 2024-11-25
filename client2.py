# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QWidget
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Ui_client(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        if Form.layout() is not None:
        # Delete the existing layout
                QWidget().setLayout(Form.layout())

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QWidget(Form)
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
        self.header.setMaximumHeight(200)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
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
        self.pagename.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pagename.setObjectName("pagename")
        self.horizontalLayout.addWidget(self.pagename)
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.export_btn = QtWidgets.QPushButton(self.header)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sys client management/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_5.addWidget(self.export_btn)

        

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sys client management/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_btn = QtWidgets.QPushButton(self.header)
        self.import_btn.setIcon(icon1)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_5.addWidget(self.import_btn)
        
        self.delete_btn = QtWidgets.QPushButton(self.header)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sys client management/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        self.delete_btn.setIcon(icon2)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_5.addWidget(self.delete_btn)
        spacerItem2 = QtWidgets.QSpacerItem(468, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_btn = QtWidgets.QPushButton(self.header)
        self.add_btn.setMinimumSize(QtCore.QSize(50, 21))
        self.add_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sys client management/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon3)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_4.addWidget(self.add_btn)
        self.edit_btn = QtWidgets.QPushButton(self.header)
        self.edit_btn.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/sys client management/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon4)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_4.addWidget(self.edit_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.header)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/sys client management/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon5)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_4.addWidget(self.refresh_btn)
        spacerItem3 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchbar = QtWidgets.QLineEdit(self.header)
        self.searchbar.setMinimumSize(QtCore.QSize(160, 23))
        self.searchbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_3.addWidget(self.searchbar)

        self.searchbar.setMaximumWidth(1000)

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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/sys client management/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon6)
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
        self.verticalLayout.addWidget(self.menu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pagename.setText(_translate("Form", "CLIENT"))
        self.export_btn.setText(_translate("Form", "Export"))
        self.import_btn.setText(_translate("Form", "Import"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        self.add_btn.setText(_translate("Form", "Add"))
        self.edit_btn.setText(_translate("Form", "Edit"))
        self.refresh_btn.setText(_translate("Form", "Refresh"))
        self.searchbar.setPlaceholderText(_translate("Form", "Search..."))
        self.table_client.setSortingEnabled(False)
        item = self.table_client.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Num"))
        item = self.table_client.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.table_client.horizontalHeaderItem(2)
        item.setText(_translate("Form", "IC Number"))
        item = self.table_client.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email"))
        item = self.table_client.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Contact"))
        item = self.table_client.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Remark"))
        item = self.table_client.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Actual Num"))

import clientsysmanagenent_rc

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_client()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())