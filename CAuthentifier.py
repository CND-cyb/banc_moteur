import sys
import mysql.connector
import bcrypt
from PySide6.QtWidgets import QApplication, QWidget
from authentifier import Ui_Connexion
from CAccueil import AppBancMot  

class Connexion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Connexion()
        self.ui.setupUi(self)
        self.ui.pb_connecter.clicked.connect(self.authentifier)

    def authentifier(self):
        identifiant = self.ui.le_identifiant.text().strip()
        mdp = self.ui.le_mdp.text().strip()

        if identifiant == "" or mdp == "":
            self.afficher_message("Veuillez remplir tous les champs.")
            return

        host = 'mysql-eguidat.alwaysdata.net'
        user = 'eguidat_banc_mot'
        db_password = 'CestGénialCeBts2025*!'
        database = 'eguidat_banc_moteur'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=db_password,
                database=database
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT mdp FROM utilisateur WHERE identifiant = %s", (identifiant,))
            result = cursor.fetchone()

            if result is None:
                self.afficher_message("Identifiant ou mot de passe incorrect.")
            else:
                hashed_password = result["mdp"]

                if bcrypt.checkpw(mdp.encode(), hashed_password.encode()):
                    cursor.execute("SELECT secret FROM utilisateur WHERE identifiant = %s", (identifiant,))
                    result=cursor.fetchone()
                    if result is None:
                        self.accueil = AppBancMot(identifiant)
                        self.accueil.show()
                        self.close()
                    else:
                        self.accueil = AppBancMot(identifiant)
                        self.accueil.show()
                        self.close()
                else:
                    self.afficher_message("Identifiant ou mot de passe incorrect.")
            cursor.close()
            connection.close()

        except mysql.connector.Error as e:
            self.afficher_message(f"Problème de connexion à la base de données : {e}")

    def afficher_message(self, message):
        self.ui.l_erreur.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Connexion()
    fenetre.show()
    sys.exit(app.exec())
