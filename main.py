import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt6.uic import loadUi
from base_d import connect, create_tables
from utilisateurs import ajouter_utilisateur, supprimer_utilisateur_par_nom, rechercher_id_utilisateur
from villes import ajouter_ville_utilisateur, supprimer_ville_utilisateur, afficher_villes_utilisateur
from meteo import obtenir_meteo_ville

create_tables()



class meteo_w(QDialog):
    def __init__(self):
        super(meteo_w, self).__init__()  
        loadUi('rech.ui', self)
        self.rech_ville.clicked.connect(self.recherche)
        
    def recherche(self):
            ville = self.ville_saisie.text().lower()
            obtenir_meteo_ville(self,ville, "b9fc7ccd767c8f02d78333045699b865")
        
        
    
            

class MainWindow(QMainWindow):
    def __init__(self, id_utilisateur):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)
        self.id_utilisateur = id_utilisateur  
        self.supp_v.clicked.connect(self.suppp)
        self.ajout_v.clicked.connect(self.ajout)
        self.recherch_v.clicked.connect(self.invite)
        self.affich_v.clicked.connect(self.affich)
    def invite(self):
        self.dialog = meteo_w() 
        self.dialog.show()

    def ajout(self):
        self.dialog = ajout(self.id_utilisateur)  
        self.dialog.show()
        
        
    def suppp(self):
        self.dialog = supp(self.id_utilisateur)  
        self.dialog.show()
        
    def affich(self):
        self.dialog = affichag(self.id_utilisateur) 
        self.dialog.show()
        
        
    
        
        
        
class ajout(QDialog):
    def __init__(self, id_utilisateur):
        super(ajout, self).__init__()
        loadUi('ajt.ui', self)
        self.id_utilisateur = id_utilisateur  
        self.ajouter_v.clicked.connect(self.ajout_ville)

    def ajout_ville(self):
        ville = self.ville_saisie.text().lower()

        if ajouter_ville_utilisateur(self.id_utilisateur, ville) == 1:
            self.etat_p.setText(f"La ville '{ville}' a été ajoutée avec succès.")
        else:
            self.etat_n.setText(f"La ville '{ville}' existe déjà.")
            
            
            
class supp(QDialog):
    def __init__(self, id_utilisateur):
        super(supp, self).__init__()
        loadUi('supp.ui', self)
        self.id_utilisateur = id_utilisateur  
        self.supr_v.clicked.connect(self.supp_ville)

    def supp_ville(self):
        ville = self.ville_saisie.text().lower()

        if supprimer_ville_utilisateur(self.id_utilisateur, ville) == 1:
            self.etat_p.setText(f"La ville '{ville}' a été supprimée avec succès.")
        else:
            self.etat_n.setText(f"La ville '{ville}' n'existe pas.")            


class affichag(QDialog):
    def __init__(self, id_utilisateur):
        super(affichag, self).__init__()
        loadUi('affichag.ui', self)
        self.id_utilisateur = id_utilisateur  
        
        villes = afficher_villes_utilisateur(self.id_utilisateur)
        print(villes)
        
        if villes is None:
            self.etat_n.setText("Il n'y a aucune ville pour cet utilisateur.")
        else:
            
            for i in range(len(villes)):
                self.listWidget.addItem(villes[i][0])

        
        self.listWidget.itemSelectionChanged.connect(self.mettre_a_jour_selection)

        
        self.ville_selec.setText("Aucune ville sélectionnée")
    
    def mettre_a_jour_selection(self):
        
        selection = self.listWidget.selectedItems()

        if selection:
            ville=selection[0].text().lower()
            self.ville_selec.setText(ville)
            self.boutonoui.clicked.connect(lambda: self.chercher_ville(ville))

            
        else:
            
            self.ville_selec.setText("Aucune ville sélectionnée")
            
            
    def chercher_ville(self, ville):
        if obtenir_meteo_ville(self,ville, "b9fc7ccd767c8f02d78333045699b865")==0:
            self.etat_n.setText("ville inexistante")
            


            

            
        
        
        


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("gui.ui", self)
        self.co.clicked.connect(self.fonction_connection)
        self.cre_co.clicked.connect(self.fonction_creation)
        self.invit.clicked.connect(self.invite)

    def fonction_connection(self):
        nom = self.username_u.text().lower()
        mdp = self.mdp_u.text().lower()
        self.id_utilisateur = rechercher_id_utilisateur(nom, mdp)
        if self.id_utilisateur is None:
            self.indic.setText("Utilisateur non trouvé ou mot de passe incorrect.")
        else:
            self.open_main_window() 

    def open_main_window(self):
        self.main_window = MainWindow(self.id_utilisateur)  
        self.main_window.show()           
        self.close() 
                  

    def invite(self):
        self.dialog = meteo_w()  
        self.dialog.show()  


    def fonction_creation(self):
        nom = self.username_u.text().lower()
        mdp = self.mdp_u.text().lower()
        id = rechercher_id_utilisateur(nom, mdp)
    
        if id is None:
            ajouter_utilisateur(nom, mdp)
            self.id_utilisateur = rechercher_id_utilisateur(nom, mdp)
            self.open_main_window() 
        else:
            self.indic.setText("Utilisateur déjà présent dans la base de données.")
    


if __name__ == "__main__":
    appli = QApplication(sys.argv)
    window = Login()
    window.setFixedWidth(475)
    window.setFixedHeight(450)
    window.show()

    sys.exit(appli.exec())
