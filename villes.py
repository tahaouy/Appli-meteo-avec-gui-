from base_d import connect
import requests

def rech_ville_uti(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT villes.id, villes.nom
        FROM villes
        INNER JOIN utilisateurs_villes ON villes.id = utilisateurs_villes.ville_id
        WHERE utilisateurs_villes.utilisateur_id = ? AND villes.nom = ?
    ''', (utilisateur_id, nom_ville))
    
    villes = cursor.fetchall()
    conn.close()
    
    if len(villes) == 0:  
        return False
    else:
        return True

def ajouter_ville_utilisateur(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id FROM villes WHERE nom = ?', (nom_ville,))
        ville = cursor.fetchone()

        if not rech_ville_uti(utilisateur_id, nom_ville):
            if ville is None:
                cursor.execute('INSERT INTO villes (nom) VALUES (?)', (nom_ville,))
                ville_id = cursor.lastrowid
            else:
                ville_id = ville[0]

            cursor.execute('INSERT INTO utilisateurs_villes (utilisateur_id, ville_id) VALUES (?, ?)', (utilisateur_id, ville_id))
            conn.commit()
            print(f"\nLa ville '{nom_ville}' a été ajoutée avec succès.")
            return 1
        else:
            print(f"\nLa ville '{nom_ville}' est déjà enregistrée pour cet utilisateur.")
            return 0
    finally:
        conn.close()

def supprimer_ville_utilisateur(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()

    try:
        
        cursor.execute('SELECT id FROM villes WHERE nom = ?', (nom_ville,))
        ville = cursor.fetchone()

        if ville is None:
            print(f"\nLa ville '{nom_ville}' n'existe pas dans la base de données.")
            return 0

        ville_id = ville[0]

        
        if rech_ville_uti(utilisateur_id, nom_ville):
            
            cursor.execute('DELETE FROM utilisateurs_villes WHERE utilisateur_id = ? AND ville_id = ?', (utilisateur_id, ville_id))
            conn.commit()
            print(f"\nLa ville '{nom_ville}' a été supprimée pour cet utilisateur.")
            return 1
        else:
            print(f"\nL'utilisateur n'a pas cette ville associée.")
            return 0
    finally:
        conn.close()


def afficher_villes_utilisateur(utilisateur_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT villes.nom
        FROM villes
        INNER JOIN utilisateurs_villes ON villes.id = utilisateurs_villes.ville_id
        WHERE utilisateurs_villes.utilisateur_id = ?
    ''', (utilisateur_id,))
    
    villes = cursor.fetchall()
    conn.close()
    
    if villes == []:
        print("\nAucune ville enregistrée.")
        return None

    return villes