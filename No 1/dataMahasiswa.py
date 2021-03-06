# from Modul4.DialogUI.DialogUi import Ui_Form
from addData import *
from dialogDelete import *
from editData import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dataMahasiswa(QtWidgets.QDialog):
    def setupUi(self, dataMahasiswa):
        dataMahasiswa.setObjectName("dataMahasiswa")
        dataMahasiswa.resize(441, 312)
        self.widget = QtWidgets.QWidget(dataMahasiswa)
        self.widget.setGeometry(QtCore.QRect(10, 10, 421, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.mainTitle.setFont(font)
        self.mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")
        self.verticalLayout.addWidget(self.mainTitle)
        self.tblMahasiswa = QtWidgets.QTableWidget(self.widget)
        self.tblMahasiswa.setMouseTracking(False)
        self.tblMahasiswa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblMahasiswa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tblMahasiswa.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tblMahasiswa.setAutoScroll(True)
        self.tblMahasiswa.setShowGrid(True)
        self.tblMahasiswa.setRowCount(4)
        self.tblMahasiswa.setColumnCount(4)
        self.tblMahasiswa.setObjectName("tblMahasiswa")
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMahasiswa.setItem(3, 3, item)
        self.tblMahasiswa.horizontalHeader().setVisible(True)
        self.tblMahasiswa.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tblMahasiswa)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnAdd = QtWidgets.QPushButton(self.widget)
        self.btnAdd.setDefault(True)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnAdd.clicked.connect(self.onBtnAddClicked)

        self.btnDelete = QtWidgets.QPushButton(self.widget)
        self.btnDelete.setDefault(False)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnDelete.clicked.connect(self.onBtnDeleteClicked)
        
        self.btnEdit = QtWidgets.QPushButton(self.widget)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout.addWidget(self.btnEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnEdit.clicked.connect(self.onBtnEditClicked)

        self.retranslateUi(dataMahasiswa)
        QtCore.QMetaObject.connectSlotsByName(dataMahasiswa)
        
    def onBtnAddClicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_addDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def onBtnEditClicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_editDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def onBtnDeleteClicked(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def retranslateUi(self, dataMahasiswa):
        _translate = QtCore.QCoreApplication.translate
        dataMahasiswa.setWindowTitle(_translate("dataMahasiswa", "Data Mahasiswa"))
        self.mainTitle.setText(_translate("dataMahasiswa", "Data Mahasiswa"))
        self.tblMahasiswa.setSortingEnabled(False)
        item = self.tblMahasiswa.verticalHeaderItem(0)
        item.setText(_translate("dataMahasiswa", "1"))
        item = self.tblMahasiswa.verticalHeaderItem(1)
        item.setText(_translate("dataMahasiswa", "2"))
        item = self.tblMahasiswa.verticalHeaderItem(2)
        item.setText(_translate("dataMahasiswa", "3"))
        item = self.tblMahasiswa.verticalHeaderItem(3)
        item.setText(_translate("dataMahasiswa", "4"))
        item = self.tblMahasiswa.horizontalHeaderItem(0)
        item.setText(_translate("dataMahasiswa", "NIM"))
        item = self.tblMahasiswa.horizontalHeaderItem(1)
        item.setText(_translate("dataMahasiswa", "Nama"))
        item = self.tblMahasiswa.horizontalHeaderItem(2)
        item.setText(_translate("dataMahasiswa", "Jurusan"))
        item = self.tblMahasiswa.horizontalHeaderItem(3)
        item.setText(_translate("dataMahasiswa", "No.Telp"))
        __sortingEnabled = self.tblMahasiswa.isSortingEnabled()
        self.tblMahasiswa.setSortingEnabled(False)
        item = self.tblMahasiswa.item(0, 0)
        item.setText(_translate("dataMahasiswa", "19104017"))
        item = self.tblMahasiswa.item(0, 1)
        item.setText(_translate("dataMahasiswa", "Putu Restu"))
        item = self.tblMahasiswa.item(0, 2)
        item.setText(_translate("dataMahasiswa", "RPL"))
        item = self.tblMahasiswa.item(0, 3)
        item.setText(_translate("dataMahasiswa", "085156123123"))
        item = self.tblMahasiswa.item(1, 0)
        item.setText(_translate("dataMahasiswa", "19104018"))
        item = self.tblMahasiswa.item(1, 1)
        item.setText(_translate("dataMahasiswa", "Kadek Dwi"))
        item = self.tblMahasiswa.item(1, 2)
        item.setText(_translate("dataMahasiswa", "SI"))
        item = self.tblMahasiswa.item(1, 3)
        item.setText(_translate("dataMahasiswa", "08414144124"))
        item = self.tblMahasiswa.item(2, 0)
        item.setText(_translate("dataMahasiswa", "19104019"))
        item = self.tblMahasiswa.item(2, 1)
        item.setText(_translate("dataMahasiswa", "Nyoman Candra"))
        item = self.tblMahasiswa.item(2, 2)
        item.setText(_translate("dataMahasiswa", "TI"))
        item = self.tblMahasiswa.item(2, 3)
        item.setText(_translate("dataMahasiswa", "08312421512"))
        item = self.tblMahasiswa.item(3, 0)
        item.setText(_translate("dataMahasiswa", "19104020"))
        item = self.tblMahasiswa.item(3, 1)
        item.setText(_translate("dataMahasiswa", "Ketut Tingkih"))
        item = self.tblMahasiswa.item(3, 2)
        item.setText(_translate("dataMahasiswa", "DKV"))
        item = self.tblMahasiswa.item(3, 3)
        item.setText(_translate("dataMahasiswa", "08341312412"))
        self.tblMahasiswa.setSortingEnabled(__sortingEnabled)
        self.btnAdd.setText(_translate("dataMahasiswa", "Tambah"))
        self.btnDelete.setText(_translate("dataMahasiswa", "Hapus"))
        self.btnEdit.setText(_translate("dataMahasiswa", "Edit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_dataMahasiswa()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
