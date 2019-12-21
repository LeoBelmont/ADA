from PyQt5 import QtCore, QtGui, QtWidgets
from anastruct import SystemElements

class Ui_MainWindow(object):

    ss = SystemElements()

    listavx1 = []
    listavy1 = []
    listavx2 = []
    listavy2 = []
    listavei = []
    listavea = []
    listavg = []
    listavmp = []
    listavmola = []
    listatx1 = []
    listaty1 = []
    listatx2 = []
    listaty2 = []
    listatea = []
    listamdir = []
    listamang = []
    listappos = []
    listaprot = []
    listapyint = []
    listapxint = []
    listafixo = []
    listamovel = []
    listamolapos = []
    listamolatra = []
    listamolares = []
    listamolactrl = []
    listaeng = []
    listamint = []
    listampos = []
    listalint = []
    listaldir = []
    listalpos = []
    listanid = []
    listanx = []
    listany = []
    cont = contpont = contfixo = contmovel = conteng = contmola = contmom = contload = contt = contn = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1280))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.splitter_15 = QtWidgets.QSplitter(self.tab)
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName("splitter_15")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.label_33 = QtWidgets.QLabel(self.splitter_12)
        self.label_33.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_12)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.vigacx2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigacx2.setMinimumSize(QtCore.QSize(0, 25))
        self.vigacx2.setObjectName("vigacx2")
        self.gridLayout.addWidget(self.vigacx2, 1, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        self.label_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 0, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.vigaei = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigaei.setMinimumSize(QtCore.QSize(0, 25))
        self.vigaei.setObjectName("vigaei")
        self.gridLayout.addWidget(self.vigaei, 1, 5, 1, 1)
        self.vigag = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigag.setMinimumSize(QtCore.QSize(0, 25))
        self.vigag.setObjectName("vigag")
        self.gridLayout.addWidget(self.vigag, 1, 6, 1, 1)
        self.vigamp = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigamp.setMinimumSize(QtCore.QSize(0, 25))
        self.vigamp.setObjectName("vigamp")
        self.gridLayout.addWidget(self.vigamp, 1, 7, 1, 1)
        self.vigacx1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigacx1.setMinimumSize(QtCore.QSize(0, 25))
        self.vigacx1.setObjectName("vigacx1")
        self.gridLayout.addWidget(self.vigacx1, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget)
        self.label_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 0, 2, 1, 1)
        self.vigacy2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigacy2.setMinimumSize(QtCore.QSize(0, 25))
        self.vigacy2.setObjectName("vigacy2")
        self.gridLayout.addWidget(self.vigacy2, 1, 3, 1, 1)
        self.vigaea = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigaea.setMinimumSize(QtCore.QSize(0, 25))
        self.vigaea.setObjectName("vigaea")
        self.gridLayout.addWidget(self.vigaea, 1, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        self.label_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 0, 8, 1, 1)
        self.vigamola = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigamola.setMinimumSize(QtCore.QSize(0, 25))
        self.vigamola.setObjectName("vigamola")
        self.gridLayout.addWidget(self.vigamola, 1, 8, 1, 1)
        self.vigacy1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.vigacy1.setMinimumSize(QtCore.QSize(0, 25))
        self.vigacy1.setObjectName("vigacy1")
        self.gridLayout.addWidget(self.vigacy1, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        self.label_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 0, 6, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget)
        self.label_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 0, 3, 1, 1)
        self.vigaadd = QtWidgets.QPushButton(self.splitter_12)
        self.vigaadd.setObjectName("vigaadd")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_13.setMinimumSize(QtCore.QSize(0, 25))
        self.splitter_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")
        self.label_34 = QtWidgets.QLabel(self.splitter_13)
        self.label_34.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_13)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.trusscx2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.trusscx2.setMinimumSize(QtCore.QSize(0, 25))
        self.trusscx2.setObjectName("trusscx2")
        self.gridLayout_5.addWidget(self.trusscx2, 1, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 0, 4, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 0, 0, 1, 1)
        self.trusscx1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.trusscx1.setMinimumSize(QtCore.QSize(0, 25))
        self.trusscx1.setObjectName("trusscx1")
        self.gridLayout_5.addWidget(self.trusscx1, 1, 0, 1, 1)
        self.trussea = QtWidgets.QLineEdit(self.layoutWidget1)
        self.trussea.setMinimumSize(QtCore.QSize(0, 25))
        self.trussea.setObjectName("trussea")
        self.gridLayout_5.addWidget(self.trussea, 1, 4, 1, 1)
        self.trusscy1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.trusscy1.setMinimumSize(QtCore.QSize(0, 25))
        self.trusscy1.setObjectName("trusscy1")
        self.gridLayout_5.addWidget(self.trusscy1, 1, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_5.addWidget(self.label_41, 0, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_5.addWidget(self.label_44, 0, 2, 1, 1)
        self.trusscy2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.trusscy2.setMinimumSize(QtCore.QSize(0, 25))
        self.trusscy2.setObjectName("trusscy2")
        self.gridLayout_5.addWidget(self.trusscy2, 1, 3, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_5.addWidget(self.label_45, 0, 3, 1, 1)
        self.trussadd = QtWidgets.QPushButton(self.splitter_13)
        self.trussadd.setObjectName("trussadd")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")
        self.label_37 = QtWidgets.QLabel(self.splitter_14)
        self.label_37.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_14)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_38 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 0, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_11.addWidget(self.label_39, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 0, 2, 1, 1)
        self.nodpv = QtWidgets.QLineEdit(self.layoutWidget2)
        self.nodpv.setMinimumSize(QtCore.QSize(0, 25))
        self.nodpv.setObjectName("nodpv")
        self.gridLayout_11.addWidget(self.nodpv, 1, 0, 1, 1)
        self.noduv = QtWidgets.QLineEdit(self.layoutWidget2)
        self.noduv.setMinimumSize(QtCore.QSize(0, 25))
        self.noduv.setObjectName("noduv")
        self.gridLayout_11.addWidget(self.noduv, 1, 1, 1, 1)
        self.nodpos = QtWidgets.QLineEdit(self.layoutWidget2)
        self.nodpos.setMinimumSize(QtCore.QSize(0, 25))
        self.nodpos.setObjectName("nodpos")
        self.gridLayout_11.addWidget(self.nodpos, 1, 2, 1, 1)
        self.nodadd = QtWidgets.QPushButton(self.splitter_14)
        self.nodadd.setObjectName("nodadd")
        self.gridLayout_12.addWidget(self.splitter_15, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.splitter_6 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter = QtWidgets.QSplitter(self.splitter_6)
        self.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setMinimumSize(QtCore.QSize(0, 80))
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)
        self.fixopos = QtWidgets.QLineEdit(self.layoutWidget3)
        self.fixopos.setMinimumSize(QtCore.QSize(0, 25))
        self.fixopos.setObjectName("fixopos")
        self.gridLayout_6.addWidget(self.fixopos, 2, 0, 1, 1)
        self.fixoadd = QtWidgets.QPushButton(self.splitter)
        self.fixoadd.setObjectName("fixoadd")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 80))
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_13.addWidget(self.label_12, 0, 0, 1, 1)
        self.engpos = QtWidgets.QLineEdit(self.layoutWidget4)
        self.engpos.setMinimumSize(QtCore.QSize(0, 25))
        self.engpos.setObjectName("engpos")
        self.gridLayout_13.addWidget(self.engpos, 1, 0, 1, 1)
        self.engadd = QtWidgets.QPushButton(self.splitter_2)
        self.engadd.setObjectName("engadd")
        self.gridLayout_14.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        self.label_6.setMinimumSize(QtCore.QSize(0, 80))
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget5 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 2, 1, 1)
        self.movelpos = QtWidgets.QLineEdit(self.layoutWidget5)
        self.movelpos.setMinimumSize(QtCore.QSize(0, 25))
        self.movelpos.setObjectName("movelpos")
        self.gridLayout_2.addWidget(self.movelpos, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.movelang = QtWidgets.QLineEdit(self.layoutWidget5)
        self.movelang.setMinimumSize(QtCore.QSize(0, 25))
        self.movelang.setObjectName("movelang")
        self.gridLayout_2.addWidget(self.movelang, 1, 2, 1, 1)
        self.moveldir = QtWidgets.QLineEdit(self.layoutWidget5)
        self.moveldir.setMinimumSize(QtCore.QSize(0, 25))
        self.moveldir.setObjectName("moveldir")
        self.gridLayout_2.addWidget(self.moveldir, 1, 1, 1, 1)
        self.moveladd = QtWidgets.QPushButton(self.splitter_3)
        self.moveladd.setObjectName("moveladd")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_8 = QtWidgets.QLabel(self.splitter_4)
        self.label_8.setMinimumSize(QtCore.QSize(0, 80))
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.molapos = QtWidgets.QLineEdit(self.layoutWidget6)
        self.molapos.setMinimumSize(QtCore.QSize(0, 25))
        self.molapos.setObjectName("molapos")
        self.gridLayout_3.addWidget(self.molapos, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.molares = QtWidgets.QLineEdit(self.layoutWidget6)
        self.molares.setMinimumSize(QtCore.QSize(0, 25))
        self.molares.setObjectName("molares")
        self.gridLayout_3.addWidget(self.molares, 1, 2, 1, 1)
        self.molactrl = QtWidgets.QLineEdit(self.layoutWidget6)
        self.molactrl.setMinimumSize(QtCore.QSize(0, 25))
        self.molactrl.setObjectName("molactrl")
        self.gridLayout_3.addWidget(self.molactrl, 1, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.molatra = QtWidgets.QLineEdit(self.layoutWidget6)
        self.molatra.setMinimumSize(QtCore.QSize(0, 25))
        self.molatra.setObjectName("molatra")
        self.gridLayout_3.addWidget(self.molatra, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)
        self.molaadd = QtWidgets.QPushButton(self.splitter_4)
        self.molaadd.setObjectName("molaadd")
        self.gridLayout_14.addWidget(self.splitter_5, 0, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.splitter_9 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.label_25 = QtWidgets.QLabel(self.splitter_9)
        self.label_25.setMinimumSize(QtCore.QSize(0, 80))
        self.label_25.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.layoutWidget7 = QtWidgets.QWidget(self.splitter_9)
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 1)
        self.pontyint = QtWidgets.QLineEdit(self.layoutWidget7)
        self.pontyint.setMinimumSize(QtCore.QSize(0, 25))
        self.pontyint.setObjectName("pontyint")
        self.gridLayout_7.addWidget(self.pontyint, 1, 1, 1, 1)
        self.pontadd = QtWidgets.QPushButton(self.layoutWidget7)
        self.pontadd.setMinimumSize(QtCore.QSize(0, 30))
        self.pontadd.setObjectName("pontadd")
        self.gridLayout_7.addWidget(self.pontadd, 2, 0, 1, 4)
        self.pontxint = QtWidgets.QLineEdit(self.layoutWidget7)
        self.pontxint.setMinimumSize(QtCore.QSize(0, 25))
        self.pontxint.setObjectName("pontxint")
        self.gridLayout_7.addWidget(self.pontxint, 1, 2, 1, 1)
        self.pontpos = QtWidgets.QLineEdit(self.layoutWidget7)
        self.pontpos.setMinimumSize(QtCore.QSize(0, 25))
        self.pontpos.setObjectName("pontpos")
        self.gridLayout_7.addWidget(self.pontpos, 1, 0, 1, 1)
        self.pontrot = QtWidgets.QLineEdit(self.layoutWidget7)
        self.pontrot.setMinimumSize(QtCore.QSize(0, 25))
        self.pontrot.setObjectName("pontrot")
        self.gridLayout_7.addWidget(self.pontrot, 1, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 0, 1, 1, 1)
        self.gridLayout_16.addWidget(self.splitter_9, 0, 0, 1, 1)
        self.splitter_10 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.label_26 = QtWidgets.QLabel(self.splitter_10)
        self.label_26.setMinimumSize(QtCore.QSize(0, 80))
        self.label_26.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.layoutWidget8 = QtWidgets.QWidget(self.splitter_10)
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget8)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.distint = QtWidgets.QLineEdit(self.layoutWidget8)
        self.distint.setMinimumSize(QtCore.QSize(0, 25))
        self.distint.setObjectName("distint")
        self.gridLayout_9.addWidget(self.distint, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 0, 2, 1, 1)
        self.distadd = QtWidgets.QPushButton(self.layoutWidget8)
        self.distadd.setMinimumSize(QtCore.QSize(0, 30))
        self.distadd.setObjectName("distadd")
        self.gridLayout_9.addWidget(self.distadd, 2, 0, 1, 3)
        self.distpos = QtWidgets.QLineEdit(self.layoutWidget8)
        self.distpos.setMinimumSize(QtCore.QSize(0, 25))
        self.distpos.setObjectName("distpos")
        self.gridLayout_9.addWidget(self.distpos, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_9.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_9.addWidget(self.label_28, 0, 1, 1, 1)
        self.distdir = QtWidgets.QLineEdit(self.layoutWidget8)
        self.distdir.setMinimumSize(QtCore.QSize(0, 25))
        self.distdir.setObjectName("distdir")
        self.gridLayout_9.addWidget(self.distdir, 1, 2, 1, 1)
        self.gridLayout_16.addWidget(self.splitter_10, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.momadd = QtWidgets.QPushButton(self.tab_3)
        self.momadd.setMinimumSize(QtCore.QSize(0, 30))
        self.momadd.setObjectName("momadd")
        self.gridLayout_10.addWidget(self.momadd, 2, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 0, 1, 1, 1)
        self.momint = QtWidgets.QLineEdit(self.tab_3)
        self.momint.setMinimumSize(QtCore.QSize(0, 25))
        self.momint.setObjectName("momint")
        self.gridLayout_8.addWidget(self.momint, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 0, 0, 1, 1)
        self.mompos = QtWidgets.QLineEdit(self.tab_3)
        self.mompos.setMinimumSize(QtCore.QSize(0, 25))
        self.mompos.setObjectName("mompos")
        self.gridLayout_8.addWidget(self.mompos, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setMinimumSize(QtCore.QSize(0, 80))
        self.label_22.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_10.addWidget(self.label_22, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_10, 2, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.splitter_7 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.visualizar = QtWidgets.QPushButton(self.splitter_7)
        self.visualizar.setMinimumSize(QtCore.QSize(0, 40))
        self.visualizar.setObjectName("visualizar")
        self.calcular = QtWidgets.QPushButton(self.splitter_7)
        self.calcular.setMinimumSize(QtCore.QSize(0, 40))
        self.calcular.setObjectName("calcular")
        self.gridLayout_4.addWidget(self.splitter_7, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ajuda = QtWidgets.QAction(MainWindow)
        self.ajuda.setObjectName("ajuda")
        self.resetar = QtWidgets.QAction(MainWindow)
        self.resetar.setObjectName("resetar")
        self.menuOp_es.addAction(self.ajuda)
        self.menuOp_es.addAction(self.resetar)
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.calcular)
        MainWindow.setTabOrder(self.calcular, self.molaadd)
        MainWindow.setTabOrder(self.molaadd, self.molapos)
        MainWindow.setTabOrder(self.molapos, self.molatra)
        MainWindow.setTabOrder(self.molatra, self.molares)
        MainWindow.setTabOrder(self.molares, self.molactrl)
        MainWindow.setTabOrder(self.molactrl, self.moveladd)
        MainWindow.setTabOrder(self.moveladd, self.movelpos)
        MainWindow.setTabOrder(self.movelpos, self.moveldir)
        MainWindow.setTabOrder(self.moveldir, self.movelang)
        MainWindow.setTabOrder(self.movelang, self.engadd)
        MainWindow.setTabOrder(self.engadd, self.engpos)
        MainWindow.setTabOrder(self.engpos, self.fixoadd)
        MainWindow.setTabOrder(self.fixoadd, self.fixopos)
        MainWindow.setTabOrder(self.fixopos, self.mompos)
        MainWindow.setTabOrder(self.mompos, self.momint)
        MainWindow.setTabOrder(self.momint, self.distpos)
        MainWindow.setTabOrder(self.distpos, self.distint)
        MainWindow.setTabOrder(self.distint, self.distdir)
        MainWindow.setTabOrder(self.distdir, self.pontpos)
        MainWindow.setTabOrder(self.pontpos, self.pontyint)
        MainWindow.setTabOrder(self.pontyint, self.pontxint)
        MainWindow.setTabOrder(self.pontxint, self.pontrot)
        MainWindow.setTabOrder(self.pontrot, self.vigaadd)
        MainWindow.setTabOrder(self.vigaadd, self.vigacx1)
        MainWindow.setTabOrder(self.vigacx1, self.vigacy1)
        MainWindow.setTabOrder(self.vigacy1, self.vigaea)
        MainWindow.setTabOrder(self.vigaea, self.vigaei)
        MainWindow.setTabOrder(self.vigaei, self.vigag)
        MainWindow.setTabOrder(self.vigag, self.vigamp)
        MainWindow.setTabOrder(self.vigamp, self.vigamola)
        MainWindow.setTabOrder(self.vigamola, self.trusscx1)
        MainWindow.setTabOrder(self.trusscx1, self.trussea)
        MainWindow.setTabOrder(self.trussea, self.trussadd)
        MainWindow.setTabOrder(self.trussadd, self.nodpv)
        MainWindow.setTabOrder(self.nodpv, self.noduv)
        MainWindow.setTabOrder(self.noduv, self.nodpos)
        MainWindow.setTabOrder(self.nodpos, self.nodadd)
        MainWindow.setTabOrder(self.nodadd, self.trusscy1)
        MainWindow.setTabOrder(self.trusscy1, self.pontadd)
        MainWindow.setTabOrder(self.pontadd, self.distadd)
        MainWindow.setTabOrder(self.distadd, self.momadd)

        self.vigaadd.clicked.connect(self.vigas)
        self.fixoadd.clicked.connect(self.supfixo)
        self.moveladd.clicked.connect(self.supmovel)
        self.pontadd.clicked.connect(self.pointload)
        self.momadd.clicked.connect(self.moment)
        self.distadd.clicked.connect(self.load)
        self.calcular.clicked.connect(self.solve)
        self.visualizar.clicked.connect(self.visualize)
        self.resetar.triggered.connect(self.reset)
        self.molaadd.clicked.connect(self.supspring)
        self.trussadd.clicked.connect(self.truss)
        self.nodadd.clicked.connect(self.node)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADA 0.4"))
        self.label_33.setText(_translate("MainWindow", "Criar Viga"))
        self.label_3.setText(_translate("MainWindow", "EA"))
        self.label_31.setText(_translate("MainWindow", "Capacidade Plástica"))
        self.label.setText(_translate("MainWindow", "Coordenada X1"))
        self.label_2.setText(_translate("MainWindow", "Coordenada Y1"))
        self.label_42.setText(_translate("MainWindow", "Coordenada X2"))
        self.label_32.setText(_translate("MainWindow", "Mola (posição)"))
        self.label_4.setText(_translate("MainWindow", "EI"))
        self.label_30.setText(_translate("MainWindow", "Peso Por Metro"))
        self.label_43.setText(_translate("MainWindow", "Coordenada Y2"))
        self.vigaadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_34.setText(_translate("MainWindow", "Criar Treliça"))
        self.label_36.setText(_translate("MainWindow", "EA"))
        self.label_35.setText(_translate("MainWindow", "Coordenada X1"))
        self.label_41.setText(_translate("MainWindow", "Coordenada Y1"))
        self.label_44.setText(_translate("MainWindow", "Coordenada X2"))
        self.label_45.setText(_translate("MainWindow", "Coordenada Y2"))
        self.trussadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_37.setText(_translate("MainWindow", "Inserir Vértice"))
        self.label_38.setText(_translate("MainWindow", "Adicionar após o vértice:"))
        self.label_39.setText(_translate("MainWindow", "Coordenada X"))
        self.label_40.setText(_translate("MainWindow", "Coordenada Y"))
        self.nodadd.setText(_translate("MainWindow", "Adicionar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Elementos"))
        self.label_5.setText(_translate("MainWindow", "Fixo"))
        self.label_9.setText(_translate("MainWindow", "Posição"))
        self.fixoadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_7.setText(_translate("MainWindow", "Engaste"))
        self.label_12.setText(_translate("MainWindow", "Posição"))
        self.engadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_6.setText(_translate("MainWindow", "Móvel"))
        self.label_16.setText(_translate("MainWindow", "Ângulo"))
        self.label_11.setText(_translate("MainWindow", "Direção Livre"))
        self.label_10.setText(_translate("MainWindow", "Posição"))
        self.moveladd.setText(_translate("MainWindow", "Adicionar"))
        self.label_8.setText(_translate("MainWindow", "Mola"))
        self.label_17.setText(_translate("MainWindow", "Translação Controlada"))
        self.label_14.setText(_translate("MainWindow", "Eixo de Translação"))
        self.label_13.setText(_translate("MainWindow", "Posição"))
        self.label_15.setText(_translate("MainWindow", "Resistência"))
        self.molaadd.setText(_translate("MainWindow", "Adicionar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Apoios"))
        self.label_25.setText(_translate("MainWindow", "Carga pontual"))
        self.label_18.setText(_translate("MainWindow", "Posição"))
        self.pontadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_20.setText(_translate("MainWindow", "Intensidade em X"))
        self.label_21.setText(_translate("MainWindow", "Rotação"))
        self.label_19.setText(_translate("MainWindow", "Intensidade em Y"))
        self.label_26.setText(_translate("MainWindow", "Carga distribuída"))
        self.label_29.setText(_translate("MainWindow", "Direção"))
        self.distadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_27.setText(_translate("MainWindow", "Posição"))
        self.label_28.setText(_translate("MainWindow", "Intensidade"))
        self.momadd.setText(_translate("MainWindow", "Adicionar"))
        self.label_24.setText(_translate("MainWindow", "Intensidade"))
        self.label_23.setText(_translate("MainWindow", "Posição"))
        self.label_22.setText(_translate("MainWindow", "Momento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Cargas e Momentos"))
        self.visualizar.setText(_translate("MainWindow", "Visualizar"))
        self.calcular.setText(_translate("MainWindow", "Calcular"))
        self.menuOp_es.setTitle(_translate("MainWindow", "Opções"))
        self.ajuda.setText(_translate("MainWindow", "Como utilizar"))
        self.resetar.setText(_translate("MainWindow", "Resetar valores"))
        self.resetar.setShortcut(_translate("MainWindow", "Ctrl+R"))

    def vigas(self):
        self.listavx1.append(float(self.vigacx1.text()))
        self.listavy1.append(float(self.vigacy1.text()))
        self.listavx2.append(float(self.vigacx2.text()))
        self.listavy2.append(float(self.vigacy2.text()))

        if self.vigaea.text() == '':
            self.listavea.append(0)
        else:
            self.listavea.append(float(self.vigaea.text()))

        if self.vigaei.text() == '':
            self.listavei.append(0)
        else:
            self.listavei.append(float(self.vigaei.text()))

        if self.vigag.text() == '':
            self.listavg.append(0)
        else:
            self.listavg.append(float(self.vigag.text()))

        if self.vigamp.text() == '':
            self.listavmp.append(0)
        else:
            self.listavmp.append(float(self.vigamp.text()))

        if self.vigamola.text() == '':
            self.listavmola.append(str('None'))
        else:
            self.listavmola.append(int(self.vigamola.text()))

        self.vigacx1.setText(self.vigacx2.text())
        self.vigacy1.setText(self.vigacy2.text())
        self.vigacx2.clear()
        self.vigacy2.clear()
        self.vigaea.clear()
        self.vigaei.clear()
        self.vigag.clear()
        self.vigamp.clear()
        self.vigamola.clear()

    def truss(self):
        self.listatx1.append(float(self.trusscx1.text()))
        self.listaty1.append(float(self.trusscy1.text()))
        self.listatx2.append(float(self.trusscx2.text()))
        self.listaty2.append(float(self.trusscy2.text()))
        if self.trussea.text() == '':
            self.listatea.append(0)
        else:
            self.listatea.append(float(self.trussea.text()))
        self.trusscx1.setText(self.trusscx2.text())
        self.trusscy1.setText(self.trusscy2.text())
        self.trusscx2.clear()
        self.trusscy2.clear()
        self.trussea.clear()

    def node(self):
        self.listanid.append(int(self.nodpv.text()))
        self.listanx.append(float(self.noduv.text()))
        self.listany.append(float(self.nodpos.text()))
        self.nodpos.clear()
        self.noduv.clear()
        self.nodpv.clear()

    def supfixo(self):
        self.listafixo.append(int(self.fixopos.text()))
        self.fixopos.clear()

    def supmovel(self):
        self.listamovel.append(int(self.movelpos.text()))
        if self.moveldir.text() == '':
            self.listamdir.append('y')
        else:
            self.listamdir.append(str(self.moveldir.text()))
        if self.movelang.text() == '':
            self.listamang.append(0)
        else:
            self.listamang.append(float(self.movelang.text()))
        self.movelpos.clear()
        self.moveldir.clear()
        self.movelang.clear()

    def supeng(self):
        self.listaeng.append(self.engpos.text())

    def supspring(self):
        self.listamolapos.append(int(self.molapos.text()))

        if self.molactrl.text() == '':
            self.listamolactrl.append(str('False'))
        else:
            self.listamolactrl.append(str(self.molactrl.text()))

        if self.molares.text() == '':
            self.listamolares.append(0)
        else:
            self.listamolares.append(float(self.molares.text()))

        if self.molatra.text() == 'x' or 'X':
            self.listamolatra.append(1)
        elif self.molatra.text() == 'z' or 'Z':
            self.listamolatra.append(2)
        elif self.molatra.text() == 'y' or 'Y':
            self.listamolatra.append(3)
        else:
            self.listamolatra.append(1)

        self.molapos.clear()
        self.molatra.clear()
        self.molares.clear()
        self.molactrl.clear()

    def pointload(self):
        self.listappos.append(int(self.pontpos.text()))
        if self.pontyint.text() == '':
            self.listapyint.append(0)
        else:
            self.listapyint.append(float(self.pontyint.text()))
        if self.pontxint.text() == '':
            self.listapxint.append(0)
        else:
            self.listapxint.append(float(self.pontxint.text()))
        if self.pontrot.text() == '':
            self.listaprot.append(0)
        else:
            self.listaprot.append(float(self.pontrot.text()))
        self.pontpos.clear()
        self.pontyint.clear()
        self.pontxint.clear()
        self.pontrot.clear()

    def load(self):
        self.listalpos.append(int(self.distpos.text()))
        self.listalint.append(float(self.distint.text()))
        if self.distdir.text() == '' or 'viga' or 'Viga':
            self.listaldir.append('element')
        else:
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
        for c in range(len(self.listavx1)):
            self.ss.add_element(location=[[self.listavx1[self.cont], self.listavy1[self.cont]],
                                          [self.listavx2[self.cont], self.listavy2[self.cont]]],
                                EA=self.listavea[self.cont], EI=self.listavei[self.cont], g=self.listavg[self.cont])
                                #mp=self.listavmp[self.cont], spring=self.listavmola[self.cont])
            self.cont += 1

        for c in range(len(self.listatx1)):
            self.ss.add_truss_element(location=[[self.listatx1[self.contt], self.listaty1[self.contt]],
                                                [self.listatx2[self.contt], self.listaty2[self.contt]]],
                                      EA=self.listatea[self.contt])
            self.contt += 1

        for c in range(len(self.listanid)):
            self.ss.insert_node(element_id=self.listanid[self.contn], location=[self.listanx[self.contn],
                                                                                self.listany[self.contn]])
            self.contn += 1

        for c in range(len(self.listafixo)):
            self.ss.add_support_hinged(node_id=self.listafixo[self.contfixo])
            self.contfixo += 1

        for c in range(len(self.listamovel)):
            self.ss.add_support_roll(node_id=self.listamovel[self.contmovel],
                                     direction=self.listamdir[self.contmovel], angle=self.listamang[self.contmovel])
            self.contmovel += 1

        for c in range(len(self.listaeng)):
            self.ss.add_support_fixed(node_id=self.listaeng[self.conteng])
            self.conteng += 1

        for c in range(len(self.listamolapos)):
            self.ss.add_support_spring(node_id=self.listamolapos[self.contmola],
                                       translation=self.listamolatra[self.contmola],
                                       k=self.listamolares[self.contmola], roll=self.listamolactrl[self.contmola])
            self.contmola += 1

        for c in range(len(self.listapyint)):
            self.ss.point_load(node_id=self.listappos[self.contpont],
                               Fy=self.listapyint[self.contpont], Fx=self.listapxint[self.contpont],
                               rotation=self.listaprot[self.contpont])
            self.contpont += 1

        for c in range(len(self.listamint)):
            self.ss.moment_load(node_id=self.listampos[self.contmom], Ty=self.listamint[self.contmom])
            self.contmom += 1

        for c in range(len(self.listalint)):
            self.ss.q_load(element_id=self.listalpos[self.contload], q=self.listalint[self.contload],
                           direction=self.listaldir[self.contload])
            self.contload += 1

        self.cont = self.contpont = self.contfixo = self.contmovel = self.conteng = self.contmola = self.contmom =\
            self.contload = self.contt = self.contn = 0

        self.ss.solve()
        self.ss.show_structure()
        self.ss.show_axial_force()
        self.ss.show_reaction_force()
        self.ss.show_bending_moment()

    def visualize(self):
        for c in range(len(self.listavx1)):
            self.ss.add_element(location=[[self.listavx1[self.cont], self.listavy1[self.cont]],
                                          [self.listavx2[self.cont], self.listavy2[self.cont]]],
                                EA=self.listavea[self.cont], EI=self.listavei[self.cont], g=self.listavg[self.cont])
                                #mp=self.listavmp[self.cont], spring=self.listavmola[self.cont])
            self.cont += 1

        for c in range(len(self.listatx1)):
            self.ss.add_truss_element(location=[[self.listatx1[self.contt], self.listaty1[self.contt]],
                                                [self.listatx2[self.contt], self.listaty2[self.contt]]],
                                      EA=self.listatea[self.contt])
            self.contt += 1

        for c in range(len(self.listanid)):
            self.ss.insert_node(element_id=self.listanid[self.contn], location=[self.listanx[self.contn],
                                                                                self.listany[self.contn]])
            self.contn += 1

        for c in range(len(self.listafixo)):
            self.ss.add_support_hinged(node_id=self.listafixo[self.contfixo])
            self.contfixo += 1

        for c in range(len(self.listamovel)):
            self.ss.add_support_roll(node_id=self.listamovel[self.contmovel],
                                     direction=self.listamdir[self.contmovel], angle=self.listamang[self.contmovel])
            self.contmovel += 1

        for c in range(len(self.listaeng)):
            self.ss.add_support_fixed(node_id=self.listaeng[self.conteng])
            self.conteng += 1

        for c in range(len(self.listamolapos)):
            self.ss.add_support_spring(node_id=self.listamolapos[self.contmola],
                                       translation=self.listamolatra[self.contmola],
                                       k=self.listamolares[self.contmola], roll=self.listamolactrl[self.contmola])
            self.contmola += 1

        for c in range(len(self.listapyint)):
            self.ss.point_load(node_id=self.listappos[self.contpont],
                               Fy=self.listapyint[self.contpont], Fx=self.listapxint[self.contpont],
                               rotation=self.listaprot[self.contpont])
            self.contpont += 1

        for c in range(len(self.listamint)):
            self.ss.moment_load(node_id=self.listampos[self.contmom], Ty=self.listamint[self.contmom])
            self.contmom += 1

        for c in range(len(self.listalint)):
            self.ss.q_load(element_id=self.listalpos[self.contload], q=self.listalint[self.contload],
                           direction=self.listaldir[self.contload])
            self.contload += 1

        self.cont = self.contpont = self.contfixo = self.contmovel = self.conteng = self.contmola = self.contmom = \
            self.contload = self.contt = self.contn = 0

        self.ss.show_structure()

    def reset(self):
        self.ss.remove_loads()
        self.listavx1.clear()
        self.listavy1.clear()
        self.listavx2.clear()
        self.listavy2.clear()
        self.listatx.clear()
        self.listaty.clear()
        self.listamdir.clear()
        self.listamang.clear()
        self.listappos.clear()
        self.listaprot.clear()
        self.listapyint.clear()
        self.listapxint.clear()
        self.listafixo.clear()
        self.listamovel.clear()
        self.listamolapos.clear()
        self.listamolactrl.clear()
        self.listamolares.clear()
        self.listamolatra.clear()
        self.listaeng.clear()
        self.listamint.clear()
        self.listampos.clear()
        self.listalint.clear()
        self.listaldir.clear()
        self.listalpos.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
