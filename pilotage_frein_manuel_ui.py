# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pilotage_frein_manuel.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(998, 182)
        Form.setStyleSheet(u"QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.pb_marche = QPushButton(Form)
        self.pb_marche.setObjectName(u"pb_marche")
        self.pb_marche.setGeometry(QRect(310, 340, 81, 31))
        self.pb_marche.setStyleSheet(u"QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.pb_arret = QPushButton(Form)
        self.pb_arret.setObjectName(u"pb_arret")
        self.pb_arret.setGeometry(QRect(470, 340, 81, 31))
        self.pb_arret.setStyleSheet(u"QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.pb_valider = QPushButton(Form)
        self.pb_valider.setObjectName(u"pb_valider")
        self.pb_valider.setGeometry(QRect(390, 280, 81, 31))
        self.pb_valider.setStyleSheet(u"QPushButton {\n"
"    background-color: #dfe6e9;\n"
"    border: 1px solid #b2bec3;\n"
"    border-radius: 5px;\n"
"    color: #2d3436;\n"
"    padding: 6px 12px;\n"
"    font: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b2bec3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #636e72;\n"
"    color: #ffffff;\n"
"}")
        self.sB_valeurFrein = QSpinBox(Form)
        self.sB_valeurFrein.setObjectName(u"sB_valeurFrein")
        self.sB_valeurFrein.setGeometry(QRect(410, 210, 42, 22))
        self.sB_valeurFrein.setMaximum(100)
        self.slider_valeurFrein = QSlider(Form)
        self.slider_valeurFrein.setObjectName(u"slider_valeurFrein")
        self.slider_valeurFrein.setGeometry(QRect(340, 180, 160, 22))
        self.slider_valeurFrein.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #E0E0E0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #4A90E2;\n"
"    border: 2px solid #357ABD;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -4px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4CAF50;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #E0E0E0;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.slider_valeurFrein.setMaximum(100)
        self.slider_valeurFrein.setOrientation(Qt.Horizontal)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 80, 151, 51))
        self.pb_quitter = QPushButton(Form)
        self.pb_quitter.setObjectName(u"pb_quitter")
        self.pb_quitter.setGeometry(QRect(390, 440, 81, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pb_marche.setText(QCoreApplication.translate("Form", u"Marche ", None))
        self.pb_arret.setText(QCoreApplication.translate("Form", u"Arr\u00eat ", None))
        self.pb_valider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choisir la consigne de frein ", None))
        self.pb_quitter.setText(QCoreApplication.translate("Form", u"Quitter", None))
    # retranslateUi

