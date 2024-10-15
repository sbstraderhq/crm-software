# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analysis(object):
    def setupUi(self, analysis):
        analysis.setObjectName("analysis")
        analysis.resize(637, 502)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(analysis)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(analysis)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header = QtWidgets.QWidget(self.widget)
        self.header.setStyleSheet("QWidget{\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"    \n"
"    background-color: rgb(226, 226, 226);\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.title_label = QtWidgets.QLabel(self.header)
        self.title_label.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_4.addWidget(self.title_label)
        spacerItem1 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.balance_btn = QtWidgets.QPushButton(self.header)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sys client management/balance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.balance_btn.setIcon(icon)
        self.balance_btn.setObjectName("balance_btn")
        self.horizontalLayout.addWidget(self.balance_btn)
        self.delete_btn = QtWidgets.QPushButton(self.header)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sys client management/trending.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        spacerItem2 = QtWidgets.QSpacerItem(438, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_btn = QtWidgets.QPushButton(self.header)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sys client management/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon2)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.edit_btn = QtWidgets.QPushButton(self.header)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sys client management/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon3)
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_3.addWidget(self.edit_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.header)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/sys client management/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon4)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_3.addWidget(self.refresh_btn)
        spacerItem3 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchbar = QtWidgets.QLineEdit(self.header)
        self.searchbar.setMinimumSize(QtCore.QSize(160, 21))
        self.searchbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchbar.setClearButtonEnabled(False)
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_2.addWidget(self.searchbar)
        self.search_btn = QtWidgets.QPushButton(self.header)
        self.search_btn.setMinimumSize(QtCore.QSize(22, 22))
        self.search_btn.setStyleSheet("border-radius: 10px;")
        self.search_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/sys client management/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon5)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_2.addWidget(self.search_btn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.header)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.balance_page = QtWidgets.QWidget()
        self.balance_page.setObjectName("balance_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.balance_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.balance_table = QtWidgets.QTableWidget(self.balance_page)
        self.balance_table.setStyleSheet("QHeaderView::section{\n"
"    background-color: rgb(195, 195, 195);;\n"
"}\n"
"QTableWidget::Item{ \n"
"    color:black;    \n"
"}\n"
"")
        self.balance_table.setObjectName("balance_table")
        self.balance_table.setColumnCount(7)
        self.balance_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.balance_table.setHorizontalHeaderItem(6, item)
        self.balance_table.horizontalHeader().setSortIndicatorShown(False)
        self.balance_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.balance_table)
        self.stackedWidget.addWidget(self.balance_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.widget)

        self.retranslateUi(analysis)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(analysis)

    def retranslateUi(self, analysis):
        _translate = QtCore.QCoreApplication.translate
        analysis.setWindowTitle(_translate("analysis", "Analysis"))
        self.title_label.setText(_translate("analysis", "ANALYSIS"))
        self.balance_btn.setText(_translate("analysis", "Balance"))
        self.delete_btn.setText(_translate("analysis", "Trends"))
        self.add_btn.setText(_translate("analysis", "Add"))
        self.edit_btn.setText(_translate("analysis", "Edit"))
        self.refresh_btn.setText(_translate("analysis", "Refresh"))
        self.searchbar.setPlaceholderText(_translate("analysis", "Search..."))
        item = self.balance_table.horizontalHeaderItem(0)
        item.setText(_translate("analysis", "Num"))
        item = self.balance_table.horizontalHeaderItem(1)
        item.setText(_translate("analysis", "Client ID"))
        item = self.balance_table.horizontalHeaderItem(2)
        item.setText(_translate("analysis", "Name"))
        item = self.balance_table.horizontalHeaderItem(3)
        item.setText(_translate("analysis", "Referral Code"))
        item = self.balance_table.horizontalHeaderItem(4)
        item.setText(_translate("analysis", "Total Deposit"))
        item = self.balance_table.horizontalHeaderItem(5)
        item.setText(_translate("analysis", "Total Withdrawal"))
        item = self.balance_table.horizontalHeaderItem(6)
        item.setText(_translate("analysis", "Balance"))
import clientsysmanagenent_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    analysis = QtWidgets.QWidget()
    ui = Ui_analysis()
    ui.setupUi(analysis)
    analysis.show()
    sys.exit(app.exec_())