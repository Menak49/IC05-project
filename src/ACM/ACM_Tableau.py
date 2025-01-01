
import matplotlib
matplotlib.use('TkAgg')  # Utiliser un backend compatible pour éviter l'erreur
import pandas as pd
import matplotlib.pyplot as plt
import prince

file= "fichier_pour_ACM_nettoye.xlsx"

df= pd.read_excel(file)
#colonne_categorie=["year","actor_type","industry","event_type","event_subtype","region","region_attaquée"]
colonne_categorie=["region_attaquée","event_type","industry","year"]
df[colonne_categorie]=df[colonne_categorie].astype('category')

acm=prince.MCA(n_components=2,random_state=42)
acm=acm.fit(df[colonne_categorie])

# Récupérer les coordonnées des individus et des modalités
individus = acm.row_coordinates(df[colonne_categorie])  # Coordonnées des individus
modalites = acm.column_coordinates(df[colonne_categorie])  # Coordonnées des modalités

# Création de la figure
plt.figure(figsize=(14, 10))  # Augmenter la taille

# Tracer les individus
plt.scatter(individus[0], individus[1], label="Individus", alpha=0.1, c='blue', s=10)  # Taille réduite

# Tracer les modalités
plt.scatter(modalites[0], modalites[1], label="Modalités", alpha=0.6, c='red')

# Ajouter les étiquettes pour les modalités
for i, label in enumerate(modalites.index):
    #print(label)
    plt.text(modalites.iloc[i, 0], modalites.iloc[i, 1], label, fontsize=9, color='darkred')

# Ajouter les étiquettes pour les individus (optionnel selon la lisibilité)
"""
for i, label in enumerate(individus.index):
    plt.text(individus.iloc[i, 0], individus.iloc[i, 1], label, fontsize=7, color='darkblue', alpha=0.6)
"""

# Personnalisation du graphique
plt.axhline(0, color='grey', linestyle='--', linewidth=0.5)  # Ligne horizontale
plt.axvline(0, color='grey', linestyle='--', linewidth=0.5)  # Ligne verticale
plt.title("Analyse des Correspondances Multiples (ACM)", fontsize=16)
plt.xlabel("Dimension 1", fontsize=12)
plt.ylabel("Dimension 2", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("acm_modalités", dpi=300)  # Enregistrer avec une meilleure résolution
