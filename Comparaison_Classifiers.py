import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from skimage.io import imread
from skimage.color import rgb2grey
from skimage.filters import threshold_mean
from sklearn import tree
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
# DEFINITION DE LA FONCTION QUI CHARGE LES IMAGES D'APPRENTISSAGE
def apprentissage_des_images():
# la base de donnees D'apprentissage contient les images suivants:
# 5a-3b-3c-2d-3e-3f-2g-3h-4i-3j-2k-2l-2m-3n-3o-3p-2q-2r-3s-2t-3u-2v-2w-2x-2y-2z
    y = np.array(
        [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13,
         14, 14,
         15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26])
    images = []
    for i in range(1, 63):
        img = "C:/Users/HP/Desktop/circuit/MST_s2/images/apprentissage/".__add__(i.__str__()).__add__(".png")
        imageRGB = imread(img)
        image = rgb2grey(imageRGB)
        thresh = threshold_mean(image)
        binary = image > thresh
        binary = binary * 1
        images.append(np.ravel(binary))
    return images, y

# DEFINITION DE LA FONCTION QUI CHARGE LES IMAGES DE TEST
def image_test():
    y = np.array([1,1,2,2,3,3,4,4,5,5,6,6,6,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,
                      18,19,19,20,21,21,22,23,24,25,26])
    images = []
    for i in range(1, 45):
        img = "C:/Users/HP/Desktop/circuit/MST_s2/images/TEST/".__add__(i.__str__()).__add__(".png")
        imageRGB = imread(img)
        #ON FAIT LE TRAITEMENT SUR LES IMAGES POUR QU'ILS ETRE DES IMAGES BINAIRE
        image = rgb2grey(imageRGB)
        thresh = threshold_mean(image)
        binary = image > thresh
        binary = binary * 1
        images.append(np.ravel(binary))
    return images, y

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(290, 50, 50, 50))
        self.image.setText("")
        self.image.setObjectName("image")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(34, 20, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(34, 80, 731, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(34, 120, 731, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(34, 160, 731, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(34, 200, 731, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(24, 30, 20, 301))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(144, 30, 20, 301))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(314, 30, 20, 301))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(754, 30, 20, 301))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(534, 30, 20, 301))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(64, 50, 51, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(44, 140, 91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(54, 180, 81, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(164, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.TG = QtWidgets.QLabel(self.centralwidget)
        self.TG.setGeometry(QtCore.QRect(164, 100, 151, 20))
        self.TG.setText("")
        self.TG.setObjectName("TG")
        self.TM = QtWidgets.QLabel(self.centralwidget)
        self.TM.setGeometry(QtCore.QRect(164, 140, 151, 20))
        self.TM.setText("")
        self.TM.setObjectName("TM")
        self.TB = QtWidgets.QLabel(self.centralwidget)
        self.TB.setGeometry(QtCore.QRect(164, 180, 151, 20))
        self.TB.setText("")
        self.TB.setObjectName("TB")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(344, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.PG = QtWidgets.QLabel(self.centralwidget)
        self.PG.setGeometry(QtCore.QRect(334, 100, 191, 20))
        self.PG.setText("")
        self.PG.setObjectName("PG")
        self.PM = QtWidgets.QLabel(self.centralwidget)
        self.PM.setGeometry(QtCore.QRect(340, 140, 181, 20))
        self.PM.setText("")
        self.PM.setObjectName("PM")
        self.PB = QtWidgets.QLabel(self.centralwidget)
        self.PB.setGeometry(QtCore.QRect(340, 180, 181, 20))
        self.PB.setText("")
        self.PB.setObjectName("PB")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(594, 30, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.CG = QtWidgets.QLabel(self.centralwidget)
        self.CG.setGeometry(QtCore.QRect(510, 100, 131, 20))
        self.CG.setText("")
        self.CG.setObjectName("CG")
        self.CM = QtWidgets.QLabel(self.centralwidget)
        self.CM.setGeometry(QtCore.QRect(510, 140, 131, 20))
        self.CM.setText("")
        self.CM.setObjectName("CM")
        self.CB = QtWidgets.QLabel(self.centralwidget)
        self.CB.setGeometry(QtCore.QRect(510, 180, 131, 20))
        self.CB.setText("")
        self.CB.setObjectName("CB")
        self.ouvrir = QtWidgets.QPushButton(self.centralwidget)
        self.ouvrir.setGeometry(QtCore.QRect(510, 350, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ouvrir.setFont(font)
        self.ouvrir.setObjectName("ouvrir")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(520, 390, 210, 210))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.PTG = QtWidgets.QLabel(self.centralwidget)
        self.PTG.setGeometry(QtCore.QRect(550, 100, 201, 20))
        self.PTG.setText("")
        self.PTG.setObjectName("PTG")
        self.PTM = QtWidgets.QLabel(self.centralwidget)
        self.PTM.setGeometry(QtCore.QRect(550, 140, 201, 20))
        self.PTM.setText("")
        self.PTM.setObjectName("PTM")
        self.PTB = QtWidgets.QLabel(self.centralwidget)
        self.PTB.setGeometry(QtCore.QRect(550, 180, 201, 20))
        self.PTB.setText("")
        self.PTB.setObjectName("PTB")
        self.gaussian = QtWidgets.QPushButton(self.centralwidget)
        self.gaussian.setGeometry(QtCore.QRect(20, 410, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gaussian.setFont(font)
        self.gaussian.setObjectName("gaussian")
        self.multinomial = QtWidgets.QPushButton(self.centralwidget)
        self.multinomial.setGeometry(QtCore.QRect(20, 470, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.multinomial.setFont(font)
        self.multinomial.setObjectName("multinomial")
        self.bernouli = QtWidgets.QPushButton(self.centralwidget)
        self.bernouli.setGeometry(QtCore.QRect(20, 530, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bernouli.setFont(font)
        self.bernouli.setObjectName("bernouli")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(60, 610, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resultat.setFont(font)
        self.resultat.setText("")
        self.resultat.setObjectName("resultat")
        self.extra_tree = QtWidgets.QPushButton(self.centralwidget)
        self.extra_tree.setGeometry(QtCore.QRect(260, 470, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extra_tree.setFont(font)
        self.extra_tree.setObjectName("extra_tree")
        self.decision_tree = QtWidgets.QPushButton(self.centralwidget)
        self.decision_tree.setGeometry(QtCore.QRect(260, 410, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decision_tree.setFont(font)
        self.decision_tree.setObjectName("decision_tree")
        self.mlp = QtWidgets.QPushButton(self.centralwidget)
        self.mlp.setGeometry(QtCore.QRect(260, 530, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mlp.setFont(font)
        self.mlp.setObjectName("mlp")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(30, 240, 731, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(30, 280, 731, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(30, 320, 731, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(40, 700, 731, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(40, 740, 731, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(30, 710, 20, 81))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(40, 780, 731, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(760, 710, 20, 81))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(270, 710, 20, 81))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(540, 710, 20, 81))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 720, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 720, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 720, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 220, 81, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 260, 81, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 300, 81, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.TDT = QtWidgets.QLabel(self.centralwidget)
        self.TDT.setGeometry(QtCore.QRect(160, 220, 151, 20))
        self.TDT.setText("")
        self.TDT.setObjectName("TDT")
        self.PDT = QtWidgets.QLabel(self.centralwidget)
        self.PDT.setGeometry(QtCore.QRect(340, 220, 181, 20))
        self.PDT.setText("")
        self.PDT.setObjectName("PDT")
        self.PTDT = QtWidgets.QLabel(self.centralwidget)
        self.PTDT.setGeometry(QtCore.QRect(560, 220, 181, 20))
        self.PTDT.setText("")
        self.PTDT.setObjectName("PTDT")
        self.TET = QtWidgets.QLabel(self.centralwidget)
        self.TET.setGeometry(QtCore.QRect(160, 260, 151, 20))
        self.TET.setText("")
        self.TET.setObjectName("TET")
        self.PET = QtWidgets.QLabel(self.centralwidget)
        self.PET.setGeometry(QtCore.QRect(330, 260, 191, 20))
        self.PET.setText("")
        self.PET.setObjectName("PET")
        self.PTET = QtWidgets.QLabel(self.centralwidget)
        self.PTET.setGeometry(QtCore.QRect(550, 260, 191, 20))
        self.PTET.setText("")
        self.PTET.setObjectName("PTET")
        self.TMLP = QtWidgets.QLabel(self.centralwidget)
        self.TMLP.setGeometry(QtCore.QRect(160, 300, 151, 20))
        self.TMLP.setText("")
        self.TMLP.setObjectName("TMLP")
        self.PMLP = QtWidgets.QLabel(self.centralwidget)
        self.PMLP.setGeometry(QtCore.QRect(330, 300, 191, 20))
        self.PMLP.setText("")
        self.PMLP.setObjectName("PMLP")
        self.PTMLP = QtWidgets.QLabel(self.centralwidget)
        self.PTMLP.setGeometry(QtCore.QRect(550, 300, 191, 20))
        self.PTMLP.setText("")
        self.PTMLP.setObjectName("PTMLP")
        self.TEM = QtWidgets.QLabel(self.centralwidget)
        self.TEM.setGeometry(QtCore.QRect(50, 760, 211, 20))
        self.TEM.setText("")
        self.TEM.setObjectName("TEM")
        self.MTA = QtWidgets.QLabel(self.centralwidget)
        self.MTA.setGeometry(QtCore.QRect(290, 760, 241, 20))
        self.MTA.setText("")
        self.MTA.setObjectName("MTA")
        self.MTT = QtWidgets.QLabel(self.centralwidget)
        self.MTT.setGeometry(QtCore.QRect(560, 760, 191, 20))
        self.MTT.setText("")
        self.MTT.setObjectName("MTT")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Classifier"))
        self.label_2.setText(_translate("MainWindow", "GaussianNB"))
        self.label_3.setText(_translate("MainWindow", "MultinomialNB"))
        self.label_4.setText(_translate("MainWindow", "BernoulliNB"))
        self.label_5.setText(_translate("MainWindow", "Temps d\'execution"))
        self.label_9.setText(_translate("MainWindow", "Phase d\'apprentissage"))
        self.label_13.setText(_translate("MainWindow", "phase de test"))
        self.ouvrir.setText(_translate("MainWindow", "parcourir"))
        self.gaussian.setText(_translate("MainWindow", "GAUSSIAN"))
        self.multinomial.setText(_translate("MainWindow", "Multinomial"))
        self.bernouli.setText(_translate("MainWindow", "Bernouli"))
        self.extra_tree.setText(_translate("MainWindow", "Extra tree"))
        self.decision_tree.setText(_translate("MainWindow", "Decision tree"))
        self.mlp.setText(_translate("MainWindow", "MLP"))
        self.label_6.setText(_translate("MainWindow", "Temps d\'execution minimum"))
        self.label_7.setText(_translate("MainWindow", "meilleur en terme d\'apprentissage"))
        self.label_8.setText(_translate("MainWindow", "meilleur en terme de test"))
        self.label_10.setText(_translate("MainWindow", "Decision tree"))
        self.label_11.setText(_translate("MainWindow", "Extra tree"))
        self.label_12.setText(_translate("MainWindow", "MLP"))
        
        self.TG.setText(str(t11-t1))
        self.TM.setText(str(t33-t3))
        self.TB.setText(str(t22-t2))
        self.PG.setText(str(gnb.score(x1,y1)*100))
        self.PM.setText(str(mnb.score(x1,y1)*100))
        self.PB.setText(str(bnb.score(x1,y1)*100))
        self.PTG.setText(str(gnb.score(x2,y2)*100))
        self.PTM.setText(str(mnb.score(x2,y2)*100))
        self.PTB.setText(str(bnb.score(x2,y2)*100))
        
        self.TDT.setText(str(tt22-tt2))
        self.PDT.setText(str(dtc.score(x1,y1)*100))
        self.PTDT.setText(str(dtc.score(x2,y2)*100))
        
        self.TET.setText(str(tt11-tt1))
        self.PET.setText(str(etc.score(x1,y1)*100))
        self.PTET.setText(str(etc.score(x2,y2)*100))
        
                
        
        self.TMLP.setText(str(end-start))
        self.PMLP.setText(str(cl.score(x1,y1)*100))
        self.PTMLP.setText(str(cl.score(x2,y2)*100))
        
        
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==gnb.score(x1,y1)*100:
            self.MTA.setText("Gaussian")
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==mnb.score(x1,y1)*100:
            self.MTA.setText("Multinomial")
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==bnb.score(x1,y1)*100:
            self.MTA.setText("Bernouli")
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==dtc.score(x1,y1)*100:
            self.MTA.setText("Gaussian, Decision tree")
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==etc.score(x1,y1)*100:
            self.MTA.setText("Extra tree")
        if max(gnb.score(x1,y1)*100,mnb.score(x1,y1)*100,bnb.score(x1,y1)*100,dtc.score(x1,y1)*100,etc.score(x1,y1)*100,cl.score(x1,y1)*100)==cl.score(x1,y1)*100:
            self.MTA.setText("Gaussian, Decision tree, Extra tree, MLP")
        
        
        if max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==gnb.score(x2,y2)*100:
            self.MTT.setText("Gaussian")
        elif max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==mnb.score(x2,y2)*100:
            self.MTT.setText("Multinomial")
        elif max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==bnb.score(x2,y2)*100:
            self.MTT.setText("Bernouli")
        elif max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==dtc.score(x2,y2)*100:
            self.MTT.setText("Decision tree")
        elif max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==etc.score(x2,y2)*100:
            self.MTT.setText("Extra tree")
        elif max(gnb.score(x2,y2)*100,mnb.score(x2,y2)*100,bnb.score(x2,y2)*100,dtc.score(x2,y2)*100,etc.score(x2,y2)*100,cl.score(x2,y2)*100)==cl.score(x2,y2)*100:
            self.MTT.setText("MLP")
            
            
        if min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==t11-t1:
            self.TEM.setText("Gaussian")
        elif min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==t22-t2:
            self.TEM.setText("Bernouli")
        elif min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==t33-t3:
            self.TEM.setText("Multinomial")
        elif min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==tt11-tt1:
            self.TEM.setText("Extra tree")
        elif min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==tt22-tt2:
            self.TEM.setText("Decision tree")
        elif min(t11-t1,t22-t2,t33-t3,tt11-tt1,tt22-tt2,end-start)==end-start:
            self.TEM.setText("MLP")
            
        self.ouvrir.setText(_translate("MainWindow", "parcourir"))
        self.gaussian.setText(_translate("MainWindow", "GAUSSIAN"))
        self.multinomial.setText(_translate("MainWindow", "Multinomial"))
        self.bernouli.setText(_translate("MainWindow", "Bernouli"))
        
        self.ouvrir.clicked.connect(self.openFile)
        self.gaussian.clicked.connect(self.gaussianT)
        self.bernouli.clicked.connect(self.bernouliT)
        self.multinomial.clicked.connect(self.multinomialT)
        self.decision_tree.clicked.connect(self.DecisionTreeClassifier)
        self.extra_tree.clicked.connect(self.ExtraTreeClassifier)
        self.mlp.clicked.connect(self.MLPclass)

# CETTE FONCTION PERMET DE OUVRIR UNE FENETRE POUR CHOISIR UNE IMAGE POUR LE TEST
    def openFile(self):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
        nom_fichier = QFileDialog.getOpenFileName(self, 'Open file',"C:/Users/HP/Desktop/circuit/MST_s2/images/TEST/")
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(151, 301, QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(QtGui.QPixmap(pixmap4))
        imageTestRGB = imread(self.path)
        imageTest = rgb2grey(imageTestRGB)
        thresh = threshold_mean(imageTest)
        binaryTest = imageTest > thresh
        binaryTest = binaryTest * 1
        self.imageTest = np.ravel(binaryTest)
        
    def gaussianT(self):
        y_predg = gnb.predict([self.imageTest])
        y_predg = np.int(y_predg[0])
        self.resultat.setText("Resultat gaussian : " + alphabet[y_predg - 1])

    def bernouliT(self):
        y_predb = bnb.predict([self.imageTest])
        y_predb = np.int(y_predb[0])
        self.resultat.setText("Resultat bernouli : " + alphabet[y_predb - 1])

    
    def multinomialT(self):
        y_predm = mnb.predict([self.imageTest])
        y_predm = np.int(y_predm[0])
        self.resultat.setText("Resultat multinomial : " + alphabet[y_predm - 1])
        
    def DecisionTreeClassifier(self):
        y_predg = dtc.predict([self.imageTest])
        y_predg = np.int(y_predg[0])
        self.resultat.setText("Resultat Decision Tree Classifier : " + alphabet[y_predg - 1])

    # LA PREDICTION DE LA METHODE Extra Tree Classifier
    def ExtraTreeClassifier(self):
        y_predb = etc.predict([self.imageTest])
        y_predb = np.int(y_predb[0])
        self.resultat.setText("Resultat Extra Tree Classifier : " + alphabet[y_predb - 1])
    
    def MLPclass(self):
        y_pred = cl.predict([self.imageTest])
        y_pred = np.int(y_pred[0])
        print(alphabet[y_pred-1])
        self.resultat.setText("Resultat MLP Classifier : " +alphabet[y_pred-1])

if __name__ == "__main__":
    import sys
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    x1, y1 = apprentissage_des_images()
    x2, y2 = image_test()
    # GaussianNB

    t1 = time.perf_counter()
    gnb = GaussianNB()
    gnb.fit(x1, y1)
    t11 = time.perf_counter()
    
    
    # BernoulliNB
    t2 = time.perf_counter()
    bnb = BernoulliNB(alpha=0.4)
    bnb.fit(x1, y1)
    t22 = time.perf_counter()
    
    
    # MultinomialNB
    t3 = time.perf_counter()
    mnb = MultinomialNB(alpha=0.1)
    mnb.fit(x1, y1)
    t33 = time.perf_counter()
    
    
    tt1 = time.perf_counter()
    etc = tree.ExtraTreeClassifier(random_state=0,criterion='entropy')
    etc.fit(x1, y1)
    tt11 = time.perf_counter()
    
    
    
    tt2 = time.perf_counter()
    dtc = tree.DecisionTreeClassifier(criterion='entropy')
    dtc.fit(x1, y1)
    tt22 = time.perf_counter()
    
    
    cl = MLPClassifier(activation="relu", max_iter=2000,learning_rate="adaptive",hidden_layer_sizes=200)
    start=time.perf_counter()
    cl.fit(x1, y1)
    end=time.perf_counter()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())