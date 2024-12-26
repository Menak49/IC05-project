

import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
from rapidfuzz import process

countries = [
    "United States of America", "Canada", "Guatemala", "Cayman Islands", "Barbados", "Costa Rica", "Panama",
    "Dominican Republic", "Cuba", "Puerto Rico", "Bermuda", "Jamaica", "El Salvador", "French Guiana", "Guadeloupe",
    "Saint Vincent and the Grenadines", "Nicaragua", "Bahamas", "Brazil", "Paraguay", "Ecuador", "Chile", "Colombia",
    "Argentina", "Peru", "Uruguay", "Bolivia (Plurinational State of)", "Suriname",
    "United Kingdom of Great Britain and Northern Ireland", "Germany", "France", "Belgium", "Netherlands",
    "Luxembourg", "Ireland", "Portugal", "Switzerland", "Monaco", "Andorra", "Malta", "Liechtenstein", "Iceland",
    "Gibraltar", "Italy", "Spain", "Greece", "Cyprus", "Albania", "Bosnia and Herzegovina", "Croatia", "Serbia",
    "North Macedonia", "Montenegro", "Kosovo", "Poland", "Ukraine", "Romania", "Bulgaria",
    "Moldova (the Republic of)", "Slovakia", "Czech Republic", "Hungary", "Belarus", "Lithuania", "Latvia", "Estonia",
    "Finland", "Sweden", "Denmark", "Norway", "Russia", "Armenia", "Georgia", "Azerbaijan", "Egypt", "Morocco",
    "Algeria", "Tunisia", "Libya", "Nigeria", "Ghana", "Senegal", "Sierra Leone", "Gabon", "Côte d'Ivoire", "Liberia",
    "Togo", "Mali", "Burkina Faso", "Cameroon", "Central African Republic", "Republic of the Congo", "Chad",
    "Equatorial Guinea", "São Tomé and Príncipe", "Kenya", "Ethiopia", "Uganda", "Rwanda", "Seychelles", "Tanzania",
    "Somalia", "Djibouti", "Mozambique", "South Africa", "Namibia", "Angola", "Zimbabwe", "Botswana", "Lesotho",
    "Swaziland", "Malawi", "China", "Japan", "South Korea", "North Korea", "Taiwan", "Mongolia", "Hong Kong", "Macau",
    "India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Maldives", "Afghanistan", "Malaysia", "Singapore",
    "Thailand", "Vietnam", "Philippines", "Indonesia", "Brunei", "Laos", "Myanmar", "Cambodia", "Timor-Leste",
    "Turkey", "Saudi Arabia", "Iran", "Iraq", "Israel", "Jordan", "Lebanon", "Syria", "Kuwait", "Qatar", "Bahrain",
    "Oman", "United Arab Emirates", "Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan",
    "Australia", "New Zealand", "Palau", "Fiji", "Papua New Guinea", "Nauru", "Kiribati", "Vanuatu", "Tonga",
    "American Samoa", "Guam", "Samoa", "Isle of Man", "Bonaire, Sint Eustatius and Saba", "Sint Maarten", "Greenland",
    "European Union", "Multiple"
]

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

def comparaison_pays(region, dico_pays):
    var = 0
    for country in dico_pays:
        print(country)
        if country in region:
            var += 1
    print(var, len(dico_pays))


# URL de la page contenant l'IDH par pays
url = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"

def scrap_idh(url):



    # Récupération du contenu HTML de la page
    response = requests.get(url)
    if response.status_code == 200:
        # Parser le contenu HTML avec lxml
        tree = html.fromstring(response.content)

        # Utiliser XPath pour trouver la table avec les classes spécifiées
        xpath_expr = "//*[@id='mw-content-text']/div[1]/table[2]/tbody//tr"
        table = tree.xpath(xpath_expr)
        #print(len(table[4].text_content()))
        dico = {}
        for i in range(1, len(table)):
            if len(table[i]) == 5:
                idh = table[i][3].text_content()
                #print(table[i][0].text_content(),table[i][2].text_content(),idh)
                dico[table[i][2].text_content().replace('\xa0', '')[:-1]] = idh
            else:
                #print( table[i][1].text_content(), table[i][2].text_content())
                dico[table[i][1].text_content().replace('\xa0', '')[:-1]] = idh

        print(dico)
        return dico
    else:
        print(f"Erreur de requête : {response.status_code}")



def update_excel(excel_path, dico_pays, colonne):
    # Parcourir chaque ligne du tableau

    # Lire le fichier Excel existant
    df = pd.read_excel(excel_path)

    # Ajouter une colonne 'IDH' basée sur les pays
    for index, row in df.iterrows():
        country = row['country']  # Supposons que la colonne des pays s'appelle 'Pays'
        result = process.extractOne(country, dico_pays.keys(), score_cutoff=80)
        if result:  # Si un résultat est trouvé avec un score suffisant
            match, score, _ = result  # Déballer correctement le tuple
            df.at[index, colonne] = dico_pays[match]
        else:
            df.at[index, colonne] = "No data"  # Si aucun score trouvé
    excel = excel_path[:-4] + "2.xlsx"
    # Sauvegarder le fichier modifié
    df.to_excel(excel, index=False)
    print("Le fichier avec les IDH a été sauvegardé sous le nom 'fichier_avec_idh.xlsx'.")

def scrap_internet(url): #ITU
    # Récupération du contenu HTML de la page
    response = requests.get(url)
    if response.status_code == 200:
        # Parser le contenu HTML avec lxml
        tree = html.fromstring(response.content)

        # Utiliser XPath pour trouver la table avec les classes spécifiées
        xpath_expr = "//*[@id='mw-content-text']/div[1]/table[3]/tbody/tr"

        table = tree.xpath(xpath_expr)
        print(table[2][1].text_content())
        print(len(table[1][5].text_content()))
        dico = {}
        for i in range(1, len(table)):
            dico[table[i][0].text_content()[1:]] = table[i][3].text_content()
        print(dico)
        return dico
    else:
        print(f"Erreur de requête : {response.status_code}")




if __name__ == "__main__":
    #update_excel_with_idh("fichier_grouped.xlsx", url, regions)
    #dico_idh = scrap_idh("https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index")
    #print(countries)
    #update_excel_with_idh("Tableaux/fichier_avec_idh.xlsx", dico_idh)
    dico_internet = scrap_internet("https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users")
    update_excel("Tableaux/fichier_avec_idh.2.xlsx", dico_internet, 'Connections Internet (en %)')




