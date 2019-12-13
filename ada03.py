from PyQt5 import QtCore, QtGui, QtWidgets
from anastruct import SystemElements

class Ui_MainWindow(object):

    ss = SystemElements()
    listax1 = []
    listax2 = []
    listay1 = []
    listay2 = []
    listappos = []
    listaprot = []
    listapint = []
    listafixo = []
    listamovel = []
    listamola = []
    listaeng = []
    listamint = []
    listampos = []
    listalint = []
    listaldir = []
    listalpos = []
    cont = contpont = contfixo = contmovel = conteng = contmola = contmom = contload = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 801)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 1000))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.x2label = QtWidgets.QLabel(self.layoutWidget)
        self.x2label.setObjectName("x2label")
        self.gridLayout.addWidget(self.x2label, 2, 0, 1, 1)
        self.y1label = QtWidgets.QLabel(self.layoutWidget)
        self.y1label.setObjectName("y1label")
        self.gridLayout.addWidget(self.y1label, 0, 1, 1, 1)
        self.x2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.x2value.setObjectName("x2value")
        self.gridLayout.addWidget(self.x2value, 3, 0, 1, 1)
        self.y1value = QtWidgets.QLineEdit(self.layoutWidget)
        self.y1value.setObjectName("y1value")
        self.gridLayout.addWidget(self.y1value, 1, 1, 1, 1)
        self.x1value = QtWidgets.QLineEdit(self.layoutWidget)
        self.x1value.setObjectName("x1value")
        self.gridLayout.addWidget(self.x1value, 1, 0, 1, 1)
        self.y2label = QtWidgets.QLabel(self.layoutWidget)
        self.y2label.setObjectName("y2label")
        self.gridLayout.addWidget(self.y2label, 2, 1, 1, 1)
        self.y2value = QtWidgets.QLineEdit(self.layoutWidget)
        self.y2value.setObjectName("y2value")
        self.gridLayout.addWidget(self.y2value, 3, 1, 1, 1)
        self.x1label = QtWidgets.QLabel(self.layoutWidget)
        self.x1label.setObjectName("x1label")
        self.gridLayout.addWidget(self.x1label, 0, 0, 1, 1)
        self.eleadd = QtWidgets.QPushButton(self.splitter)
        self.eleadd.setObjectName("eleadd")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.apoiobox = QtWidgets.QComboBox(self.layoutWidget1)
        self.apoiobox.setObjectName("apoiobox")
        self.apoiobox.addItem("")
        self.apoiobox.addItem("")
        self.apoiobox.addItem("")
        self.apoiobox.addItem("")
        self.gridLayout_2.addWidget(self.apoiobox, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 2)
        self.apoiopos = QtWidgets.QLineEdit(self.layoutWidget1)
        self.apoiopos.setObjectName("apoiopos")
        self.gridLayout_2.addWidget(self.apoiopos, 2, 0, 1, 2)
        self.apoioadd = QtWidgets.QPushButton(self.splitter)
        self.apoioadd.setObjectName("apoioadd")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pontualadd = QtWidgets.QPushButton(self.tab)
        self.pontualadd.setGeometry(QtCore.QRect(180, 170, 121, 31))
        self.pontualadd.setObjectName("pontualadd")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 90, 301, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)
        self.pontrot = QtWidgets.QLineEdit(self.layoutWidget2)
        self.pontrot.setObjectName("pontrot")
        self.gridLayout_3.addWidget(self.pontrot, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.pontpos = QtWidgets.QLineEdit(self.layoutWidget2)
        self.pontpos.setObjectName("pontpos")
        self.gridLayout_3.addWidget(self.pontpos, 1, 0, 1, 1)
        self.pontint = QtWidgets.QLineEdit(self.layoutWidget2)
        self.pontint.setObjectName("pontint")
        self.gridLayout_3.addWidget(self.pontint, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.distadd = QtWidgets.QPushButton(self.tab_2)
        self.distadd.setGeometry(QtCore.QRect(180, 170, 121, 31))
        self.distadd.setObjectName("distadd")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(90, 90, 301, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 2, 1, 1)
        self.distpos = QtWidgets.QLineEdit(self.layoutWidget3)
        self.distpos.setObjectName("distpos")
        self.gridLayout_5.addWidget(self.distpos, 1, 0, 1, 1)
        self.distint = QtWidgets.QLineEdit(self.layoutWidget3)
        self.distint.setObjectName("distint")
        self.gridLayout_5.addWidget(self.distint, 1, 1, 1, 1)
        self.distdir = QtWidgets.QLineEdit(self.layoutWidget3)
        self.distdir.setObjectName("distdir")
        self.gridLayout_5.addWidget(self.distdir, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.momadd = QtWidgets.QPushButton(self.tab_3)
        self.momadd.setGeometry(QtCore.QRect(180, 170, 121, 31))
        self.momadd.setObjectName("momadd")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(110, 90, 271, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)
        self.mompos = QtWidgets.QLineEdit(self.layoutWidget4)
        self.mompos.setObjectName("mompos")
        self.gridLayout_4.addWidget(self.mompos, 1, 0, 1, 1)
        self.momint = QtWidgets.QLineEdit(self.layoutWidget4)
        self.momint.setObjectName("momint")
        self.gridLayout_4.addWidget(self.momint, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.splitter)
        self.calcular = QtWidgets.QPushButton(self.centralwidget)
        self.calcular.setObjectName("calcular")
        self.horizontalLayout.addWidget(self.calcular)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.eleadd.clicked.connect(self.element)
        self.apoioadd.clicked.connect(self.support)
        self.pontualadd.clicked.connect(self.pointload)
        self.momadd.clicked.connect(self.moment)
        self.distadd.clicked.connect(self.load)
        self.calcular.clicked.connect(self.solve)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ada 0.3"))
        self.label_2.setText(_translate("MainWindow", "Adicionar elementos"))
        self.x2label.setText(_translate("MainWindow", "Coordenada X2"))
        self.y1label.setText(_translate("MainWindow", "Coordenada Y1"))
        self.y2label.setText(_translate("MainWindow", "Coordenada Y2"))
        self.x1label.setText(_translate("MainWindow", "Coordenada X1"))
        self.eleadd.setText(_translate("MainWindow", "Adicionar"))
        self.label.setText(_translate("MainWindow", "Adicionar apoios"))
        self.apoiobox.setItemText(0, _translate("MainWindow", "Fixo"))
        self.apoiobox.setItemText(1, _translate("MainWindow", "Móvel"))
        self.apoiobox.setItemText(2, _translate("MainWindow", "Engaste"))
        self.apoiobox.setItemText(3, _translate("MainWindow", "Mola"))
        self.label_3.setText(_translate("MainWindow", "Posição do apoio (nódulo)"))
        self.apoioadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_5.setText(_translate("MainWindow", "Adicionar cargas e momentos"))
        self.pontualadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_8.setText(_translate("MainWindow", "Rotação"))
        self.label_6.setText(_translate("MainWindow", "Posição"))
        self.label_7.setText(_translate("MainWindow", "Intensidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Carga pontual"))
        self.distadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_12.setText(_translate("MainWindow", "Posição"))
        self.label_11.setText(_translate("MainWindow", "Intensidade"))
        self.label_13.setText(_translate("MainWindow", "Direção"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Carregamento"))
        self.momadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_9.setText(_translate("MainWindow", "Posição"))
        self.label_10.setText(_translate("MainWindow", "Intensidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Momento"))
        self.calcular.setText(_translate("MainWindow", "Calcular"))

    def element(self):
        self.listax1.append(float(self.x1value.text()))
        self.listax2.append(float(self.x2value.text()))
        self.listay1.append(float(self.y1value.text()))
        self.listay2.append(float(self.y2value.text()))
        self.x1value.clear()
        self.x2value.clear()
        self.y1value.clear()
        self.y2value.clear()

    def support(self):
        apoio = str(self.apoiobox.currentText())
        pos = int(self.apoiopos.text())
        if apoio == 'Fixo':
            self.listafixo.append(pos)
        elif apoio == 'Móvel':
            self.listamovel.append(pos)
        elif apoio == 'Engaste':
            self.listaeng.append(pos)
        elif apoio == 'Mola':
            self.listamola.append(pos)
        self.apoiopos.clear()

    def pointload(self):
        self.listappos.append(int(self.pontpos.text()))
        self.listapint.append(float(self.pontint.text()))
        self.listaprot.append(float(self.pontrot.text()))
        self.pontpos.clear()
        self.pontint.clear()
        self.pontrot.clear()

    def load(self):
        self.listalpos.append(int(self.distpos.text()))
        self.listalint.append(float(self.distint.text()))
        self.listaldir.append(str(self.distdir.text()))
        self.distpos.clear()
        self.distint.clear()
        self.distdir.clear()

    def moment(self):
        self.listamint.append(float(self.momint.text()))
        self.listampos.append(int(self.mompos.text()))
        self.momint.clear()
        self.mompos.clear()

    def solve(self):
        for c in range(len(self.listax1)):
            self.ss.add_element(location=[[self.listax1[self.cont], self.listay1[self.cont]],
                                     [self.listax2[self.cont], self.listay2[self.cont]]])
            self.cont += 1

        for c in range(len(self.listafixo)):
            self.ss.add_support_hinged(node_id=self.listafixo[self.contfixo])
            self.contfixo += 1

        for c in range(len(self.listamovel)):
            self.ss.add_support_roll(node_id=self.listamovel[self.contmovel])
            self.contmovel += 1

        for c in range(len(self.listaeng)):
            self.ss.add_support_fixed(node_id=self.listafixo[self.conteng])
            self.conteng += 1

        for c in range(len(self.listamola)):
            self.ss.add_support_spring(node_id=self.listamola[self.contmola])
            self.contmola += 1

        for c in range(len(self.listapint)):
            self.ss.point_load(node_id=self.listappos[self.contpont], Fy=self.listapint[self.contpont], rotation=self.listaprot[self.contpont])
            self.contpont += 1

        for c in range(len(self.listamint)):
            self.ss.moment_load(node_id=self.listampos[self.contmom], Ty=self.listamint[self.contmom])
            self.contmom += 1

        for c in range(len(self.listalint)):
            self.ss.q_load(element_id=self.listalpos[self.contload], q=self.listalint[self.contload], direction=self.listaldir[self.contload])
            self.contload += 1

        self.ss.solve()
        self.ss.show_structure()
        self.ss.show_axial_force()
        self.ss.show_reaction_force()
        self.ss.show_bending_moment()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
