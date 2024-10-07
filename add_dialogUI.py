# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 589)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 45, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 54, -1, -1)
        self.verticalLayout_2.setSpacing(38)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMaximumSize(QtCore.QSize(139, 16777215))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.TypeDrop = QtWidgets.QComboBox(self.widget)
        self.TypeDrop.setMinimumSize(QtCore.QSize(200, 0))
        self.TypeDrop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TypeDrop.setStyleSheet("color: rgb(0, 0, 0);")
        self.TypeDrop.setObjectName("TypeDrop")
        self.TypeDrop.addItem("")
        self.TypeDrop.addItem("")
        self.horizontalLayout_8.addWidget(self.TypeDrop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem)


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.NameDrop = QtWidgets.QComboBox(self.widget)
        self.NameDrop.setMinimumSize(QtCore.QSize(350, 25))
        self.NameDrop.setMaximumSize(QtCore.QSize(350, 16777215))
        self.NameDrop.setObjectName("NameDrop")
        self.NameDrop.addItem("Select Name")
        self.horizontalLayout.addWidget(self.NameDrop)

        self.NameDrop.setVisible(True)
        self.NameDrop.setStyleSheet("color: rgb(0, 0, 0);")
        

        self.TypeDrop.setFocus()


        self.RefreshName = QtWidgets.QPushButton(self.widget)
        self.RefreshName.setMaximumSize(QtCore.QSize(97, 16777215))
        self.RefreshName.setStyleSheet("color: rgb(0, 0, 0);")
        self.RefreshName.setText("")
        icon = QtGui.QIcon("image/refresh.png")
        self.RefreshName.setIcon(icon)
        self.RefreshName.setObjectName("refresh_button")
        self.horizontalLayout.addWidget(self.RefreshName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(23)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Label_id = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Label_id.setFont(font)
        self.Label_id.setStyleSheet("color: rgb(255, 0, 0);")
        self.Label_id.setObjectName("Label_id")
        self.horizontalLayout_2.addWidget(self.Label_id)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Label_referral = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Label_referral.setFont(font)
        self.Label_referral.setStyleSheet("color: rgb(255, 0, 16);")
        self.Label_referral.setObjectName("Label_referral")
        self.horizontalLayout_3.addWidget(self.Label_referral)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dateInput = QtWidgets.QDateEdit(self.widget)
        self.dateInput.setObjectName("dateInput")
        self.horizontalLayout_5.addWidget(self.dateInput)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.deposit_input = QtWidgets.QTextEdit(self.widget)
        self.deposit_input.setMinimumSize(QtCore.QSize(0, 26))
        self.deposit_input.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.deposit_input.setFont(font)
        self.deposit_input.setObjectName("deposit_input")
        self.horizontalLayout_6.addWidget(self.deposit_input)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Add Transaction"))
        self.label.setText(_translate("Dialog", "Name :"))
        self.label_3.setText(_translate("Dialog", "Client ID :"))
        self.Label_id.setText(_translate("Dialog", "-"))
        self.label_4.setText(_translate("Dialog", "Referral Code :"))
        self.Label_referral.setText(_translate("Dialog", "-"))
        self.label_5.setText(_translate("Dialog", "Date of transaction: "))
        self.label_6.setText(_translate("Dialog", "Amount: $"))
        self.label_7.setText(_translate("Dialog", "Type of Transaction:"))
        self.TypeDrop.setItemText(0, _translate("Dialog", "Deposit"))
        self.TypeDrop.setItemText(1, _translate("Dialog", "Withdrawal"))


