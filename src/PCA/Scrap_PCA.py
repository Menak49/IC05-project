import requests
from bs4 import BeautifulSoup
import pandas as pd

# Liste des régions et pays
regions = {
    "Amérique du Nord": ["United States of America", "Canada"],
    "Amérique centrale et Caraïbes": ["Guatemala", "Cayman Islands", "Barbados", "Costa Rica", "Panama",
                                      "Dominican Republic", "Cuba", "Puerto Rico", "Bermuda", "Jamaica", "El Salvador",
                                      "French Guiana", "Guadeloupe", "Cayman Islands",
                                      "Saint Vincent and the Grenadines", "Nicaragua", "Bahamas"],
    "Amérique du Sud": ["Brazil", "Paraguay", "Ecuador", "Chile", "Colombia", "Argentina", "Peru", "Uruguay",
                        "Bolivia (Plurinational State of)", "Suriname"],
    "Europe de l'Ouest": ["United Kingdom of Great Britain and Northern Ireland", "Germany", "France", "Belgium",
                          "Netherlands", "Luxembourg", "Ireland", "Portugal", "Switzerland", "Monaco", "Andorra",
                          "Malta", "Liechtenstein", "Iceland", "Gibraltar"],
    "Europe du Sud": ["Italy", "Spain", "Greece", "Cyprus", "Portugal", "Albania", "Bosnia and Herzegovina", "Croatia",
                      "Serbia", "North Macedonia", "Montenegro", "Kosovo"],
    "Europe de l'Est": ["Poland", "Ukraine", "Romania", "Bulgaria", "Moldova (the Republic of)", "Slovakia",
                        "Czech Republic", "Hungary", "Belarus", "Lithuania", "Latvia", "Estonia"],
    "Europe du Nord": ["Finland", "Sweden", "Denmark", "Norway", "Estonia", "Latvia", "Lithuania"],
    "Europe de l'Est (ex-URSS)": ["Russia", "Armenia", "Georgia", "Azerbaijan"],
    "Afrique du Nord": ["Egypt", "Morocco", "Algeria", "Tunisia", "Libya"],
    "Afrique de l'Ouest": ["Nigeria", "Ghana", "Senegal", "Sierra Leone", "Gabon", "Côte d'Ivoire", "Liberia", "Togo",
                           "Mali", "Burkina Faso"],
    "Afrique centrale": ["Cameroon", "Gabon", "Central African Republic", "Republic of the Congo", "Chad",
                         "Equatorial Guinea", "São Tomé and Príncipe"],
    "Afrique de l'Est": ["Kenya", "Ethiopia", "Uganda", "Rwanda", "Seychelles", "Tanzania", "Somalia", "Djibouti",
                         "Mozambique"],
    "Afrique australe": ["South Africa", "Namibia", "Angola", "Zimbabwe", "Botswana", "Lesotho", "Swaziland", "Malawi"],
    "Asie de l'Est": ["China", "Japan", "South Korea", "North Korea", "Taiwan", "Mongolia", "Hong Kong", "Macau"],
    "Asie du Sud": ["India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Maldives", "Afghanistan"],
    "Asie du Sud-Est": ["Malaysia", "Singapore", "Thailand", "Vietnam", "Philippines", "Indonesia", "Brunei", "Laos",
                        "Myanmar", "Cambodia", "Timor-Leste"],
    "Asie de l'Ouest (Moyen-Orient)": ["Turkey", "Saudi Arabia", "Iran", "Iraq", "Israel", "Jordan", "Lebanon", "Syria",
                                       "Kuwait", "Qatar", "Bahrain", "Oman", "United Arab Emirates"],
    "Asie centrale": ["Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan"],
    "Australie et Nouvelle-Zélande": ["Australia", "New Zealand"],
    "Océanie du Pacifique": ["Palau", "Fiji", "Papua New Guinea", "Nauru", "Kiribati", "Vanuatu", "Tonga",
                             "American Samoa", "Guam", "Samoa"],
    "Territoires et régions spéciales": ["Isle of Man", "Bonaire, Sint Eustatius and Saba", "Sint Maarten", "Hong Kong",
                                         "Macau", "Greenland", "Kosovo", "Palestine, State of", "European Union",
                                         "Multiple"]
}

# URL de la page contenant l'IDH par pays
url = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"


def update_excel_with_idh(excel_path, url, regions):
    """
    Récupère les IDH des pays à partir d'un site web et les ajoute à un fichier Excel existant.

    Args:
        excel_path (str): Le chemin du fichier Excel à modifier.
        url (str): URL de la page contenant les IDH des pays.
        regions (dict): Dictionnaire contenant les régions et leurs pays associés.
    """

    # Effectuer la requête HTTP pour récupérer le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code != 200:
        print("Erreur lors de la récupération de la page.")
        return

    # Analyser le contenu avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraire le tableau des pays et de leur IDH
    table = soup.find('table', {'class': 'flagicon'})

    # Créer un dictionnaire pour stocker les IDH par pays
    idh_by_country = {}

    # Parcourir chaque ligne du tableau
    for row in table.find_all('tr')[1:]:  # Ignorer la première ligne d'en-tête
        columns = row.find_all('td')
        if len(columns) >= 3:
            country = columns[1].get_text(strip=True)  # Nom du pays
            idh = columns[2].get_text(strip=True)  # IDH
            idh_by_country[country] = idh

    # Lire le fichier Excel existant
    df = pd.read_excel(excel_path)

    # Ajouter une colonne 'IDH' basée sur les pays
    df['IDH'] = df['country'].apply(lambda country: idh_by_country.get(country, 'Non disponible'))

    # Sauvegarder le fichier modifié
    df.to_excel("fichier_avec_idh.xlsx", index=False)
    print("Le fichier avec les IDH a été sauvegardé sous le nom 'fichier_avec_idh.xlsx'.")


# Exemple d'utilisation
if __name__ == "__main__":
    update_excel_with_idh("fichier_grouped.xlsx", url, regions)
