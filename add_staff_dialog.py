# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_staff_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_staff_dialog(object):
    def setupUi(self, add_staff_dialog):
        add_staff_dialog.setObjectName("add_staff_dialog")
        add_staff_dialog.resize(700, 160)
        add_staff_dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(add_staff_dialog)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(add_staff_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.add_name = QtWidgets.QLineEdit(add_staff_dialog)
        self.add_name.setObjectName("add_name")
        self.horizontalLayout_4.addWidget(self.add_name)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.username_label = QtWidgets.QLabel(add_staff_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy)
        self.username_label.setMinimumSize(QtCore.QSize(80, 0))
        self.username_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout_2.addWidget(self.username_label)
        self.add_username = QtWidgets.QLineEdit(add_staff_dialog)
        self.add_username.setMinimumSize(QtCore.QSize(250, 0))
        self.add_username.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.add_username.setObjectName("add_username")
        self.horizontalLayout_2.addWidget(self.add_username)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.password_label = QtWidgets.QLabel(add_staff_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        self.password_label.setMinimumSize(QtCore.QSize(80, 0))
        self.password_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_6.addWidget(self.password_label)
        self.add_password = QtWidgets.QLineEdit(add_staff_dialog)
        self.add_password.setMinimumSize(QtCore.QSize(250, 0))
        self.add_password.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.add_password.setObjectName("add_password")
        self.horizontalLayout_6.addWidget(self.add_password)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.referral_label = QtWidgets.QLabel(add_staff_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referral_label.sizePolicy().hasHeightForWidth())
        self.referral_label.setSizePolicy(sizePolicy)
        self.referral_label.setMinimumSize(QtCore.QSize(80, 30))
        self.referral_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.referral_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.referral_label.setWordWrap(True)
        self.referral_label.setObjectName("referral_label")
        self.horizontalLayout.addWidget(self.referral_label)
        self.add_referral = QtWidgets.QLineEdit(add_staff_dialog)
        self.add_referral.setMinimumSize(QtCore.QSize(250, 0))
        self.add_referral.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.add_referral.setStyleSheet("")
        self.add_referral.setReadOnly(False)
        self.add_referral.setObjectName("add_referral")
        self.horizontalLayout.addWidget(self.add_referral)
        self.horizontalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.email_label = QtWidgets.QLabel(add_staff_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy)
        self.email_label.setMinimumSize(QtCore.QSize(80, 0))
        self.email_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.email_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout_5.addWidget(self.email_label)
        self.add_email = QtWidgets.QLineEdit(add_staff_dialog)
        self.add_email.setMinimumSize(QtCore.QSize(250, 0))
        self.add_email.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.add_email.setObjectName("add_email")
        self.horizontalLayout_5.addWidget(self.add_email)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_staff_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_7.addWidget(self.buttonBox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.retranslateUi(add_staff_dialog)
        self.buttonBox.accepted.connect(add_staff_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(add_staff_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(add_staff_dialog)

    def retranslateUi(self, add_staff_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_staff_dialog.setWindowTitle(_translate("add_staff_dialog", "Add Staff"))
        self.label_2.setText(_translate("add_staff_dialog", "Name:"))
        self.username_label.setText(_translate("add_staff_dialog", "Username:"))
        self.password_label.setText(_translate("add_staff_dialog", "Password:"))
        self.referral_label.setText(_translate("add_staff_dialog", "Referral code:"))
        self.email_label.setText(_translate("add_staff_dialog", "Email:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     add_staff_dialog = QtWidgets.QDialog()
#     ui = Ui_add_staff_dialog()
#     ui.setupUi(add_staff_dialog)
#     add_staff_dialog.show()
#     sys.exit(app.exec_())