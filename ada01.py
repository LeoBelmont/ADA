# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ada.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    from anastruct import SystemElements
    ss = SystemElements()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Calcular = QtWidgets.QPushButton(self.centralwidget)
        self.Calcular.setGeometry(QtCore.QRect(870, 380, 231, 111))
        self.Calcular.setObjectName("Calcular")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 851, 821))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.x1label = QtWidgets.QLabel(self.widget)
        self.x1label.setObjectName("x1label")
        self.gridLayout.addWidget(self.x1label, 0, 0, 1, 1)
        self.y1label = QtWidgets.QLabel(self.widget)
        self.y1label.setObjectName("y1label")
        self.gridLayout.addWidget(self.y1label, 0, 1, 1, 1)
        self.x1value = QtWidgets.QLineEdit(self.widget)
        self.x1value.setObjectName("x1value")
        self.gridLayout.addWidget(self.x1value, 1, 0, 1, 1)
        self.y1value = QtWidgets.QLineEdit(self.widget)
        self.y1value.setObjectName("y1value")
        self.gridLayout.addWidget(self.y1value, 1, 1, 1, 1)
        self.x2label = QtWidgets.QLabel(self.widget)
        self.x2label.setObjectName("x2label")
        self.gridLayout.addWidget(self.x2label, 2, 0, 1, 1)
        self.y2label = QtWidgets.QLabel(self.widget)
        self.y2label.setObjectName("y2label")
        self.gridLayout.addWidget(self.y2label, 2, 1, 1, 1)
        self.x2value = QtWidgets.QLineEdit(self.widget)
        self.x2value.setObjectName("x2value")
        self.gridLayout.addWidget(self.x2value, 3, 0, 1, 1)
        self.y2value = QtWidgets.QLineEdit(self.widget)
        self.y2value.setObjectName("y2value")
        self.gridLayout.addWidget(self.y2value, 3, 1, 1, 1)
        self.fixolabel = QtWidgets.QLabel(self.widget)
        self.fixolabel.setObjectName("fixolabel")
        self.gridLayout.addWidget(self.fixolabel, 4, 0, 1, 1)
        self.movellabel = QtWidgets.QLabel(self.widget)
        self.movellabel.setObjectName("movellabel")
        self.gridLayout.addWidget(self.movellabel, 4, 1, 1, 1)
        self.fixovalue = QtWidgets.QLineEdit(self.widget)
        self.fixovalue.setObjectName("fixovalue")
        self.gridLayout.addWidget(self.fixovalue, 5, 0, 1, 1)
        self.movelvalue = QtWidgets.QLineEdit(self.widget)
        self.movelvalue.setObjectName("movelvalue")
        self.gridLayout.addWidget(self.movelvalue, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Calcular.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ada 0.1"))
        self.Calcular.setText(_translate("MainWindow", "Calcular"))
        self.x1label.setText(_translate("MainWindow", "x1"))
        self.y1label.setText(_translate("MainWindow", "y1"))
        self.x2label.setText(_translate("MainWindow", "x2"))
        self.y2label.setText(_translate("MainWindow", "y2"))
        self.fixolabel.setText(_translate("MainWindow", "Apoio fixo"))
        self.movellabel.setText(_translate("MainWindow", "Apoio móvel"))

    def pressed(self):
        x1 = int(self.x1value.text())
        x2 = int(self.x2value.text())
        y1 = int(self.y1value.text())
        y2 = int(self.y2value.text())
        movel = (int(self.movelvalue.text()))
        fixo = (int(self.fixovalue.text()))
        from anastruct import SystemElements
        ss = SystemElements()
        ss.add_element(location=[[x1, y1], [x2, y2]])
        ss.add_support_hinged(node_id=movel)
        ss.add_support_fixed(node_id=fixo)
        ss.q_load(element_id=1, q=-10)
        ss.solve()
        ss.show_structure()
        ss.show_reaction_force()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
