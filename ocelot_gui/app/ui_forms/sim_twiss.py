# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/ui_forms/sim_twiss.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Twiss(object):
    def setupUi(self, Form_Twiss):
        Form_Twiss.setObjectName("Form_Twiss")
        Form_Twiss.resize(1200, 750)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Twiss.sizePolicy().hasHeightForWidth())
        Form_Twiss.setSizePolicy(sizePolicy)
        Form_Twiss.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        )
        self.gridLayout = QtWidgets.QGridLayout(Form_Twiss)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Form_Twiss)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plus_button = QtWidgets.QPushButton(self.groupBox)
        self.plus_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.plus_button.setObjectName("plus_button")
        self.horizontalLayout_4.addWidget(self.plus_button)
        self.edit_delta = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_delta.sizePolicy().hasHeightForWidth())
        self.edit_delta.setSizePolicy(sizePolicy)
        self.edit_delta.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_delta.setDecimals(3)
        self.edit_delta.setMinimum(-9999999999.0)
        self.edit_delta.setMaximum(9999999999.99)
        self.edit_delta.setSingleStep(0.1)
        self.edit_delta.setProperty("value", 1.0)
        self.edit_delta.setObjectName("edit_delta")
        self.horizontalLayout_4.addWidget(self.edit_delta)
        self.minus_button = QtWidgets.QPushButton(self.groupBox)
        self.minus_button.setMaximumSize(QtCore.QSize(60, 16777215))
        self.minus_button.setObjectName("minus_button")
        self.horizontalLayout_4.addWidget(self.minus_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.scroll = QtWidgets.QScrollArea(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll.sizePolicy().hasHeightForWidth())
        self.scroll.setSizePolicy(sizePolicy)
        self.scroll.setMinimumSize(QtCore.QSize(300, 0))
        self.scroll.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 284, 534))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 281, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.widgetArea = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.widgetArea.setContentsMargins(0, 0, 0, 2)
        self.widgetArea.setSpacing(0)
        self.widgetArea.setObjectName("widgetArea")
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scroll)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.edit_tws_step = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.edit_tws_step.sizePolicy().hasHeightForWidth()
        )
        self.edit_tws_step.setSizePolicy(sizePolicy)
        self.edit_tws_step.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit_tws_step.setDecimals(6)
        self.edit_tws_step.setMaximum(9999999999.0)
        self.edit_tws_step.setSingleStep(0.1)
        self.edit_tws_step.setObjectName("edit_tws_step")
        self.horizontalLayout_6.addWidget(self.edit_tws_step)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.calc_params = QtWidgets.QPushButton(Form_Twiss)
        self.calc_params.setObjectName("calc_params")
        self.verticalLayout_5.addWidget(self.calc_params)
        self.calc_matching = QtWidgets.QPushButton(Form_Twiss)
        self.calc_matching.setObjectName("calc_matching")
        self.verticalLayout_5.addWidget(self.calc_matching)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn1 = QtWidgets.QPushButton(Form_Twiss)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout_5.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(Form_Twiss)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_5.addWidget(self.btn2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(Form_Twiss)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.tws_plot_widget = QtWidgets.QWidget(Form_Twiss)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tws_plot_widget.sizePolicy().hasHeightForWidth()
        )
        self.tws_plot_widget.setSizePolicy(sizePolicy)
        self.tws_plot_widget.setMinimumSize(QtCore.QSize(850, 700))
        self.tws_plot_widget.setObjectName("tws_plot_widget")
        self.verticalLayout_6.addWidget(self.tws_plot_widget)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.retranslateUi(Form_Twiss)
        QtCore.QMetaObject.connectSlotsByName(Form_Twiss)

    def retranslateUi(self, Form_Twiss):
        _translate = QtCore.QCoreApplication.translate
        Form_Twiss.setWindowTitle(_translate("Form_Twiss", "Form"))
        self.groupBox.setTitle(_translate("Form_Twiss", "Tuning elements list"))
        self.plus_button.setText(_translate("Form_Twiss", "+"))
        self.minus_button.setText(_translate("Form_Twiss", "-"))
        self.label_3.setText(_translate("Form_Twiss", "Twiss function step, m"))
        self.calc_params.setText(_translate("Form_Twiss", "Calculate Main Parameters"))
        self.calc_matching.setText(_translate("Form_Twiss", "Matching"))
        self.btn1.setText(_translate("Form_Twiss", "Update"))
        self.btn2.setText(_translate("Form_Twiss", "Reset"))
        self.label.setText(_translate("Form_Twiss", "Twiss functions"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form_Twiss = QtWidgets.QWidget()
    ui = Ui_Form_Twiss()
    ui.setupUi(Form_Twiss)
    Form_Twiss.show()
    sys.exit(app.exec_())
