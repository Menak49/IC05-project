



import pandas as pd

# Modifier les options d'affichage
pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.width', None)       # Ajuste la largeur pour éviter les coupures
pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules


fichier_excel = "Data1.xlsx"
nb = fichier_excel.find('.')




df = pd.read_excel(fichier_excel)

print(df.iloc[0:5])  # Affichage avant


colonne_limite = 'cyber_conflict_issue'



# Supprimer les colonnes (par nom)
colonnes_a_supprimer = ['inclusion_criteria_subcode', 'source_incident_detection_disclosure', 'receiver_region', 'receiver_category','initiator_category','number_of_attributions','attribution_ID','attribution_date','attribution_type','attribution_basis', 'attributing_actor',
                        'attribution_it_company', 'attributing_country','attributed_initiator', 'attributed_initiator_country', 'attributed_initiator_category' ]#changer les colonnes en fonction des besoins
df = df.drop(columns=colonnes_a_supprimer)



print("\n\nFichier nettoyé de ses colonnes : \n")

# sauvegarder dans un nouveau fichier Excel
df.to_excel(fichier_excel[nb] + "_v2" + ".xlsx", index=False)

print(df.iloc[0:10])  # Affichage apres


