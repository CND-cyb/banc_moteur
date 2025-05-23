import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPixmap
from pilotage_frein_profil_ui import Ui_Form
import paho.mqtt.client as mqtt 


class AppPilotageProfil(QWidget):
    def __init__(self,identifiant,moteur_choisi):
        super().__init__()
        self.identifiant=identifiant
        self.moteur_choisi=moteur_choisi
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tabWidget.setEnabled(True)  
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabEnabled(i, False)
        self.ui.pb_choisir_frein_profil.clicked.connect(self.choisirProfil)
        self.ui.pb_retour_profil1.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil2.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil3.clicked.connect(self.retourChoixProfil)
        self.ui.pb_retour_profil4.clicked.connect(self.retourChoixProfil)        
        self.ui.pb_retour_profil5.clicked.connect(self.retourChoixProfil)
        self.ui.pb_frein_profil_quitter.clicked.connect(self.quitter)
        self.ui.pb_valider_profil1.clicked.connect(self.validerProfil1)
        self.ui.pb_valider_profil2.clicked.connect(self.validerProfil2)
        self.ui.pb_valider_profil3.clicked.connect(self.validerProfil3)
        self.ui.pb_valider_profil4.clicked.connect(self.validerProfil4)
        self.ui.pb_valider_profil5.clicked.connect(self.validerProfil5)
        self.ui.tabWidget.setCurrentIndex(0)
        label_image_profil1=self.ui.l_image_profil1
        pixmap1 = QPixmap("C:/pyqt6/banc_moteur-main/constant.png")  # Remplace par ton chemin d'image
        label_image_profil1.setPixmap(pixmap1)
        label_image_profil1.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil2=self.ui.l_image_profil2
        pixmap2 = QPixmap("C:/pyqt6/banc_moteur-main/affine.png")  # Remplace par ton chemin d'image
        label_image_profil2.setPixmap(pixmap2)
        label_image_profil2.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil3=self.ui.l_image_profil3
        pixmap3 = QPixmap("C:/pyqt6/banc_moteur-main/expo.png")  # Remplace par ton chemin d'image
        label_image_profil3.setPixmap(pixmap3)
        label_image_profil3.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil4=self.ui.l_image_profil4
        pixmap4 = QPixmap("C:/pyqt6/banc_moteur-main/bizarre.png")  # Remplace par ton chemin d'image
        label_image_profil4.setPixmap(pixmap4)
        label_image_profil4.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        label_image_profil5=self.ui.l_image_profil5
        pixmap5 = QPixmap("C:/pyqt6/banc_moteur-main/cyclique.png")  # Remplace par ton chemin d'image
        label_image_profil5.setPixmap(pixmap5)
        label_image_profil5.setScaledContents(True)  # Redimensionne l'image à la taille du QLabel
        
        self.show()

    def choisirProfil(self):
        index = self.ui.cB_choix_profil.currentIndex()
        if 0 <= index < self.ui.tabWidget.count():
            for i in range(self.ui.tabWidget.count()):
                self.ui.tabWidget.setTabEnabled(i, False)
            self.ui.tabWidget.setTabEnabled(index, True)
            self.ui.tabWidget.setCurrentIndex(index)
            
    def validerProfil1(self):
        profil1_coefA=self.ui.sB_coupleInitial.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(1))
        client.publish(topic2,str(profil1_coefA))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
    
    def validerProfil2(self):
        profil2_coefA=self.ui.sB_coefficientDirecteur_profil2.value()
        profil2_coefB=self.ui.sB_ordonneeOrigine_profil2.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        topic3 = "Frein/CoeffB"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(2))
        client.publish(topic2,str(profil2_coefA))
        client.publish(topic3,str(profil2_coefB))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
        
    def validerProfil3(self):
        profil3_coefA=self.ui.sB_coefficientDirecteur_profil3.value()
        profil3_coefB=self.ui.sB_ordonneeOrigine_profil3.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        topic3 = "Frein/CoeffB"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(3))
        client.publish(topic2,str(profil3_coefA))
        client.publish(topic3,str(profil3_coefB))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
        
    def validerProfil4(self):
        profil4_coefA=self.ui.sB_coupleInitial_profil4.value()
        profil4_coefB=self.ui.sB_dureeConstante_profil4.value()
        profil4_coefC=self.ui.sB_coefficientDirecteur_profil4.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        topic3 = "Frein/CoeffB"
        topic4 = "Frein/CoeffC"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(4))
        client.publish(topic2,str(profil4_coefA))
        client.publish(topic3,str(profil4_coefB))
        client.publish(topic4,str(profil4_coefC))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
        
    def validerProfil5(self):
        profil5_coefA=self.ui.sB_coupleEtatHaut_profil5.value()
        profil5_coefB=self.ui.sB_coupleEtatBas_profil5.value()
        profil5_coefC=self.ui.sB_dureeEtatHaut_profil5.value()
        profil5_coefD=self.ui.sB_dureeEtatBas_profil5.value()
        broker = "192.168.2.100"  
        port = 1883 
        topic1 = "Frein/Profil"
        topic2 = "Frein/CoeffA"
        topic3 = "Frein/CoeffB"
        topic4 = "Frein/CoeffC"
        topic5 = "Frein/CoeffD"
        mqtt_username = "bancmoteur" 
        mqtt_password = "CestGenialCeBts2025"  
        client = mqtt.Client()
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(broker,port,60)
        client.publish(topic1, str(5))
        client.publish(topic2,str(profil5_coefA))
        client.publish(topic3,str(profil5_coefB))
        client.publish(topic4,str(profil5_coefC))
        client.publish(topic5,str(profil5_coefD))
        client.disconnect()
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
    
    def retourChoixProfil(self):
        for i in range(self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabEnabled(i, False)
        
    def quitter(self):
        from CAccueil_prof import AppBancMotProf
        self.accueil = AppBancMotProf(self.identifiant,self.moteur_choisi)
        self.accueil.show()
        self.close()
        
# Programme principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    monApplication = AppPilotageProfil()
    sys.exit(app.exec())
