# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 688)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(10, 10, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_dir.setFont(font)
        self.btn_dir.setObjectName("btn_dir")
        self.list_files = QtWidgets.QListWidget(self.centralwidget)
        self.list_files.setGeometry(QtCore.QRect(10, 70, 181, 571))
        self.list_files.setObjectName("list_files")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(210, 80, 541, 571))
        self.image.setObjectName("image")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(770, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_left.setFont(font)
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(770, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_right.setFont(font)
        self.btn_right.setObjectName("btn_right")
        self.mirror_1 = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_1.setGeometry(QtCore.QRect(770, 170, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mirror_1.setFont(font)
        self.mirror_1.setObjectName("mirror_1")
        self.btn_bw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bw.setGeometry(QtCore.QRect(770, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_bw.setFont(font)
        self.btn_bw.setObjectName("btn_bw")
        self.btn_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.btn_contrast.setGeometry(QtCore.QRect(770, 280, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_contrast.setFont(font)
        self.btn_contrast.setObjectName("btn_contrast")
        self.btn_blur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blur.setGeometry(QtCore.QRect(770, 330, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_blur.setFont(font)
        self.btn_blur.setObjectName("btn_blur")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(770, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_1.setFont(font)
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(770, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_2.setFont(font)
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фото-Редактор"))
        self.btn_dir.setText(_translate("MainWindow", "Папка"))
        self.image.setText(_translate("MainWindow", "Картинка"))
        self.btn_left.setText(_translate("MainWindow", "Поворот вліво"))
        self.btn_right.setText(_translate("MainWindow", "Поворот вправо"))
        self.mirror_1.setText(_translate("MainWindow", "Дзеркально\n"
" з ліва на право"))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))
        self.btn_contrast.setText(_translate("MainWindow", "Контраст"))
        self.btn_blur.setText(_translate("MainWindow", "Блюр"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())