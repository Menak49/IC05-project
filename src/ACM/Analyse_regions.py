import pandas as pd

# Dictionnaire des régions
regions = {
    "Amérique du Nord": ["United States of America", "Canada"],
    "Amérique centrale et Caraïbes": ["Guatemala", "Cayman Islands", "Barbados", "Costa Rica", "Panama", "Dominican Republic", "Cuba", "Puerto Rico", "Bermuda", "Jamaica", "El Salvador", "French Guiana", "Guadeloupe", "Cayman Islands", "Saint Vincent and the Grenadines", "Nicaragua", "Bahamas"],
    "Amérique du Sud": ["Brazil", "Paraguay", "Ecuador", "Chile", "Colombia", "Argentina", "Peru", "Uruguay", "Bolivia (Plurinational State of)", "Suriname"],
    "Europe de l'Ouest": ["United Kingdom of Great Britain and Northern Ireland", "Germany", "France", "Belgium", "Netherlands", "Luxembourg", "Ireland", "Portugal", "Switzerland", "Monaco", "Andorra", "Malta", "Liechtenstein", "Iceland", "Gibraltar"],
    "Europe du Sud": ["Italy", "Spain", "Greece", "Cyprus", "Portugal", "Albania", "Bosnia and Herzegovina", "Croatia", "Serbia", "North Macedonia", "Montenegro", "Kosovo"],
    "Europe de l'Est": ["Poland", "Ukraine", "Romania", "Bulgaria", "Moldova (the Republic of)", "Slovakia", "Czech Republic", "Hungary", "Belarus", "Lithuania", "Latvia", "Estonia"],
    "Europe du Nord": ["Finland", "Sweden", "Denmark", "Norway", "Estonia", "Latvia", "Lithuania"],
    "Europe de l'Est (ex-URSS)": ["Russia", "Armenia", "Georgia", "Azerbaijan"],
    "Afrique du Nord": ["Egypt", "Morocco", "Algeria", "Tunisia", "Libya"],
    "Afrique de l'Ouest": ["Nigeria", "Ghana", "Senegal", "Sierra Leone", "Gabon", "Côte d'Ivoire", "Liberia", "Togo", "Mali", "Burkina Faso"],
    "Afrique centrale": ["Cameroon", "Gabon", "Central African Republic", "Republic of the Congo", "Chad", "Equatorial Guinea", "São Tomé and Príncipe"],
    "Afrique de l'Est": ["Kenya", "Ethiopia", "Uganda", "Rwanda", "Seychelles", "Tanzania", "Somalia", "Djibouti", "Mozambique"],
    "Afrique australe": ["South Africa", "Namibia", "Angola", "Zimbabwe", "Botswana", "Lesotho", "Swaziland", "Malawi"],
    "Asie de l'Est": ["China", "Japan", "South Korea", "North Korea", "Taiwan", "Mongolia", "Hong Kong", "Macau"],
    "Asie du Sud": ["India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Maldives", "Afghanistan"],
    "Asie du Sud-Est": ["Malaysia", "Singapore", "Thailand", "Vietnam", "Philippines", "Indonesia", "Brunei", "Laos", "Myanmar", "Cambodia", "Timor-Leste"],
    "Asie de l'Ouest (Moyen-Orient)": ["Turkey", "Saudi Arabia", "Iran", "Iraq", "Israel", "Jordan", "Lebanon", "Syria", "Kuwait", "Qatar", "Bahrain", "Oman", "United Arab Emirates"],
    "Asie centrale": ["Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan"],
    "Australie et Nouvelle-Zélande": ["Australia", "New Zealand"],
    "Océanie du Pacifique": ["Palau", "Fiji", "Papua New Guinea", "Nauru", "Kiribati", "Vanuatu", "Tonga", "American Samoa", "Guam", "Samoa"],
    "Territoires et régions spéciales": ["Isle of Man", "Bonaire, Sint Eustatius and Saba", "Sint Maarten", "Hong Kong", "Macau", "Greenland", "Kosovo", "Palestine, State of", "European Union", "Multiple"]
}

# Fonction pour ajouter la colonne "région" basée sur "country"
def ajouter_region(fichier_excel):
    # Charger le fichier Excel
    df = pd.read_excel(fichier_excel)

    # Fonction pour trouver la région en fonction du pays
    def trouver_region(pays):
        for region, pays_list in regions.items():
            if pays in pays_list:
                return region
        return "Inconnu"  # Si le pays n'est pas trouvé


    # Appliquer la fonction à chaque ligne de la colonne 'country'
    df['region_attaquée'] = df['actor_country'].apply(trouver_region)

    # Sauvegarder le fichier modifié
    df.to_excel("fichier_avec_region.xlsx", index=False)
    print("Colonne 'region' ajoutée et fichier sauvegardé sous 'fichier_avec_region.xlsx'.")


def group_by(path):

    # Lire le fichier Excel
    df = pd.read_excel(path)


    # Afficher les premières lignes du fichier pour vérifier les données


    # Effectuer un "group by" sur la colonne 'Pays' et sommer
    result = df.groupby('country').size().reset_index(name='count')
    print(result)
    result.to_excel("fichier_grouped.xlsx", index=False)



# Exemple d'utilisation
if(__name__ == "__main__"):
    ajouter_region("fichier_avec_region_nettoye.xlsx")
