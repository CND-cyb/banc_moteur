# Form implementation generated from reading ui file 'authentifier.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Connexion(object):
    def setupUi(self, Connexion):
        Connexion.setObjectName("Connexion")
        Connexion.resize(400, 300)
        self.pb_connecter = QtWidgets.QPushButton(parent=Connexion)
        self.pb_connecter.setGeometry(QtCore.QRect(140, 200, 121, 31))
        self.pb_connecter.setObjectName("pb_connecter")
        self.le_identifier = QtWidgets.QLineEdit(parent=Connexion)
        self.le_identifier.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.le_identifier.setObjectName("le_identifier")
        self.le_mdp = QtWidgets.QLineEdit(parent=Connexion)
        self.le_mdp.setGeometry(QtCore.QRect(170, 130, 113, 22))
        self.le_mdp.setObjectName("le_mdp")
        self.label = QtWidgets.QLabel(parent=Connexion)
        self.label.setGeometry(QtCore.QRect(90, 130, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Connexion)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 61, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Connexion)
        self.pb_connecter.clicked.connect(Connexion.authentifier) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Connexion)

    def retranslateUi(self, Connexion):
        _translate = QtCore.QCoreApplication.translate
        Connexion.setWindowTitle(_translate("Connexion", "Form"))
        self.pb_connecter.setText(_translate("Connexion", "Se connecter"))
        self.label.setText(_translate("Connexion", "Mot de passe"))
        self.label_2.setText(_translate("Connexion", "Identifiant"))
