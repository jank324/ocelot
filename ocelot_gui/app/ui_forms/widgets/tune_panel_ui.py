# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/ui_forms/widgets/tune_panel_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_TunePanel(object):
    def setupUi(self, Form_TunePanel):
        Form_TunePanel.setObjectName("Form_TunePanel")
        Form_TunePanel.resize(285, 70)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_TunePanel.sizePolicy().hasHeightForWidth())
        Form_TunePanel.setSizePolicy(sizePolicy)
        Form_TunePanel.setMinimumSize(QtCore.QSize(285, 70))
        Form_TunePanel.setMaximumSize(QtCore.QSize(285, 70))
        Form_TunePanel.setAutoFillBackground(False)
        Form_TunePanel.setStyleSheet(
            ".QWidget {background-color: rgb(238, 238, 236); border-top: 2px solid rgb(255, 255, 255);}"
        )
        Form_TunePanel.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        )
        self.layoutWidget = QtWidgets.QWidget(Form_TunePanel)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 288, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 6, 5, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(
            5, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.check = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check.sizePolicy().hasHeightForWidth())
        self.check.setSizePolicy(sizePolicy)
        self.check.setMinimumSize(QtCore.QSize(115, 23))
        self.check.setMaximumSize(QtCore.QSize(115, 23))
        self.check.setAutoFillBackground(False)
        self.check.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.check.setText("")
        self.check.setObjectName("check")
        self.horizontalLayout_6.addWidget(self.check)
        self.label_f = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_f.sizePolicy().hasHeightForWidth())
        self.label_f.setSizePolicy(sizePolicy)
        self.label_f.setMinimumSize(QtCore.QSize(43, 23))
        self.label_f.setMaximumSize(QtCore.QSize(43, 23))
        self.label_f.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_f.setObjectName("label_f")
        self.horizontalLayout_6.addWidget(self.label_f)
        self.factor = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.factor.setMinimumSize(QtCore.QSize(65, 0))
        self.factor.setMaximumSize(QtCore.QSize(65, 16777215))
        self.factor.setDecimals(3)
        self.factor.setMinimum(-99999999.0)
        self.factor.setMaximum(99999999.0)
        self.factor.setSingleStep(0.01)
        self.factor.setProperty("value", 0.01)
        self.factor.setObjectName("factor")
        self.horizontalLayout_6.addWidget(self.factor)
        spacerItem1 = QtWidgets.QSpacerItem(
            15, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem1)
        self.xbutton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xbutton.sizePolicy().hasHeightForWidth())
        self.xbutton.setSizePolicy(sizePolicy)
        self.xbutton.setMinimumSize(QtCore.QSize(23, 23))
        self.xbutton.setMaximumSize(QtCore.QSize(23, 23))
        self.xbutton.setObjectName("xbutton")
        self.horizontalLayout_6.addWidget(self.xbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            5, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.label_c = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c.sizePolicy().hasHeightForWidth())
        self.label_c.setSizePolicy(sizePolicy)
        self.label_c.setMinimumSize(QtCore.QSize(40, 23))
        self.label_c.setMaximumSize(QtCore.QSize(40, 23))
        self.label_c.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_c.setObjectName("label_c")
        self.horizontalLayout.addWidget(self.label_c)
        self.curval = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curval.sizePolicy().hasHeightForWidth())
        self.curval.setSizePolicy(sizePolicy)
        self.curval.setMinimumSize(QtCore.QSize(88, 23))
        self.curval.setMaximumSize(QtCore.QSize(88, 23))
        self.curval.setDecimals(6)
        self.curval.setMinimum(-9999.0)
        self.curval.setMaximum(9999.0)
        self.curval.setSingleStep(0.01)
        self.curval.setObjectName("curval")
        self.horizontalLayout.addWidget(self.curval)
        spacerItem3 = QtWidgets.QSpacerItem(
            11, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.label_o = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_o.sizePolicy().hasHeightForWidth())
        self.label_o.setSizePolicy(sizePolicy)
        self.label_o.setMinimumSize(QtCore.QSize(63, 23))
        self.label_o.setMaximumSize(QtCore.QSize(63, 23))
        self.label_o.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.label_o.setObjectName("label_o")
        self.horizontalLayout.addWidget(self.label_o)
        self.oldval = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldval.sizePolicy().hasHeightForWidth())
        self.oldval.setSizePolicy(sizePolicy)
        self.oldval.setMinimumSize(QtCore.QSize(73, 23))
        self.oldval.setMaximumSize(QtCore.QSize(73, 23))
        self.oldval.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.oldval.setReadOnly(True)
        self.oldval.setObjectName("oldval")
        self.horizontalLayout.addWidget(self.oldval)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form_TunePanel)
        QtCore.QMetaObject.connectSlotsByName(Form_TunePanel)

    def retranslateUi(self, Form_TunePanel):
        _translate = QtCore.QCoreApplication.translate
        Form_TunePanel.setWindowTitle(_translate("Form_TunePanel", "Form"))
        self.label_f.setText(_translate("Form_TunePanel", "factor:"))
        self.xbutton.setText(_translate("Form_TunePanel", "x"))
        self.label_c.setText(_translate("Form_TunePanel", "value:"))
        self.label_o.setText(_translate("Form_TunePanel", "old value:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form_TunePanel = QtWidgets.QWidget()
    ui = Ui_Form_TunePanel()
    ui.setupUi(Form_TunePanel)
    Form_TunePanel.show()
    sys.exit(app.exec_())
