import pandas as pd

def nettoyer_fichier_excel(fichier_excel, colonnes_a_supprimer):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)        # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None) # Affiche tout le contenu des cellules

    # Trouver le nom du fichier sans extension
    nb = fichier_excel.find('.')

    # Charger le fichier Excel
    df = pd.read_excel(fichier_excel)

    print("Affichage avant nettoyage :")
    print(df.iloc[0:5])  # Affichage avant nettoyage

    # Supprimer les colonnes spécifiées
    df = df.drop(columns=colonnes_a_supprimer)

    print("\n\nFichier nettoyé de ses colonnes : \n")

    # Sauvegarder dans un nouveau fichier Excel
    nouveau_fichier = fichier_excel[:nb] + "_nettoye.xlsx"
    df.to_excel(nouveau_fichier, index=False)

    print("Affichage après nettoyage :")
    print(df.iloc[0:10])  # Affichage après nettoyage

    return df  # Retourner le DataFrame nettoyé


def ajouter_colonne_lat_long(fichier_excel, list_colonnes, dico_pays):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)  # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules


    df = pd.read_excel(fichier_excel)

    for colonne in list_colonnes:
        df[colonne] = 0

    # on remplit les colonnes 'lat' et 'long' en fonction du dictionnaire
    def traiter_ligne(row):
        # si le pays existe dans le dictionnaire on l'ajoute
        pays = row['country']
        if pays in dico_pays:
            return pd.Series({'lat': dico_pays[pays][0], 'long': dico_pays[pays][1]})
        else:
            return pd.Series({'lat': None, 'long': None})

    # appliquer la fonction sur chaque ligne
    result = df.apply(traiter_ligne, axis=1)
    df['lat'] = result['lat']
    df['long'] = result['long']


    df.to_excel(fichier_excel, index=False)

    print("Affichage après nettoyage :")
    print(df.iloc[0:10])  # Affichage après nettoyage

    return df  # Retourner le DataFrame nettoyé

def delete_all_except(fichier_excel, list_colonnes):
    #suppression de toutes les colonnes sauf celles mentionnées
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)  # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None)  # Affiche tout le contenu des cellules

    # Trouver le nom du fichier sans extension
    nb = fichier_excel.find('.')

    # Charger le fichier Excel
    df = pd.read_excel(fichier_excel)

    print("Affichage avant nettoyage :")
    print(df.iloc[0:5])  # Affichage avant nettoyage

    # Supprimer les colonnes spécifiées
    df = df[list_colonnes]
    nouveau_fichier = fichier_excel[:nb] + "_nettoye.xlsx"
    df.to_excel(nouveau_fichier, index=False)
    return df


def afficher_fichiers(fichiers_excel):
    # Modifier les options d'affichage
    pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
    pd.set_option('display.width', None)        # Ajuste la largeur pour éviter les coupures
    pd.set_option('display.max_colwidth', None) # Affiche tout le contenu des cellules

    # Traiter chaque fichier de la liste
    for fichier in fichiers_excel:
        # Vérifier l'extension et lire le fichier en fonction de son type
        if fichier.endswith('.xlsx'):  # Si le fichier est un Excel
            df = pd.read_excel(fichier)
        elif fichier.endswith('.csv'):  # Si le fichier est un CSV
            df = pd.read_csv(fichier)
        else:
            print(f"Erreur pour : {fichier}")
            continue  # Passer au fichier suivant si le type n'est ni Excel ni CSV

        # Affichage du fichier et des 10 premières lignes
        print(f"\nFichier : {fichier}")
        print(df.iloc[0:10])  # Affiche les 10 premières lignes du fichier


def supprimer_lignes_excel(fichier, colonne, valeur):
        # charger le fichier Excel dans un DataFrame
        df = pd.read_excel(fichier)

        # supprimer les lignes où la colonne contient la valeur
        df_filtre = df[df[colonne] != valeur]

        df_filtre.to_excel(fichier, index=False)



# Exemple d'utilisation :
# supprimer_lignes_excel('fichier.xlsx', 'fichier_modifie.xlsx', 'Colonne', 'ValeurASupprimer')

if "__main__" == __name__:
    #afficher_fichiers(["Data2.xlsx"])
    #ajouter_colonne_lat_long("Data2_v2.xlsx",["long", "lat"], {'United States of America': [39.7837304, -100.445882], 'Australia': [-24.7761086, 134.755], 'Malaysia': [4.5693754, 102.2656823], 'China': [35.0000663, 104.999955], 'Japan': [36.5748441, 139.2394179], 'United Kingdom of Great Britain and Northern Ireland': [54.7023545, -3.2765753], 'Tajikistan': [38.6281733, 70.8156541], 'Canada': [61.0666922, -107.991707], 'Germany': [51.1638175, 10.4478313], 'Namibia': [-23.2335499, 17.3231107], 'Turkey': [38.9597594, 34.9249653], 'Montenegro': [-29.6826112, -51.4687455], 'Czechia': [49.7439047, 15.3381061], 'Syrian Arab Republic': [34.6401861, 39.0494106], 'Saudi Arabia': [25.6242618, 42.3528328], 'Korea (the Republic of)': [37.5358612, 127.0117095], 'Armenia': [4.536307, -75.6723751], 'Israel': [30.8124247, 34.8594762], 'India': [22.3511148, 78.6677428], 'Brazil': [-10.3333333, -53.2], 'Finland': [63.2467777, 25.9209164], 'Nigeria': [9.6000359, 7.9999721], 'Italy': [42.6384261, 12.674297], 'Belgium': [50.6402809, 4.6667145], 'Ukraine': [49.4871968, 31.2718321], 'Philippines': [12.7503486, 122.7312101], 'Russian Federation': [64.6863136, 97.7453061], 'France': [46.603354, 1.8883335], 'Turkmenistan': [39.3763807, 59.3924609], 'Singapore': [1.357107, 103.8194992], 'Nepal': [28.3780464, 83.9999901], 'United Arab Emirates': [24.0002488, 53.9994829], 'Slovenia': [46.1199444, 14.8153333], 'Lithuania': [55.3500003, 23.7499997], 'Venezuela (Bolivarian Republic of)': [8.0018709, -66.1109318], 'Sweden': [59.6749712, 14.5208584], 'Spain': [39.3260685, -4.8379791], 'Austria': [47.59397, 14.12456], 'Paraguay': [-23.3165935, -58.1693445], 'Cyprus': [34.9174159, 32.889902651331866], 'Guatemala': [15.5855545, -90.345759], 'Palau': [42.5717989, 2.9600905], 'Ecuador': [-1.3397668, -79.3666965], 'Kuwait': [29.3796532, 47.9734174], 'Pakistan': [30.3308401, 71.247499], 'Egypt': [26.2540493, 29.2675469], 'Slovakia': [48.7411522, 19.4528646], 'Ireland': [52.865196, -7.9794599], 'New Zealand': [-41.5000831, 172.8344077], 'Denmark': [55.670249, 10.3333283], 'Taïwan': [23.5983227, 120.83537694479215], 'Viet Nam': [15.9266657, 107.9650855], 'Myanmar': [17.1750495, 95.9999652], 'Norway': [64.5731537, 11.52803643954819], 'Kenya': [1.4419683, 38.4313975], 'Lebanon': [40.375713, -76.4626118], 'Poland': [52.215933, 19.134422], 'Azerbaijan': [40.3936294, 47.7872508], 'Bangladesh': [24.4769288, 90.2934413], 'Romania': [45.9852129, 24.6859225], 'Mexico': [19.4326296, -99.1331785], 'Indonesia': [-2.4833826, 117.8902853], 'Sri Lanka': [7.5554942, 80.7137847], 'Albania': [5.7587654, -73.9151617], 'Bulgaria': [42.6073975, 25.4856617], 'Switzerland': [46.7985624, 8.2319736], 'Morocco': [28.3347722, -10.371337908392647], 'Ghana': [8.0300284, -1.0800271], 'Netherlands': [52.2434979, 5.6343227], 'Chile': [-31.7613365, -71.3187697], 'Portugal': [39.6621648, -8.1353519], 'Kazakhstan': [48.1012954, 66.7780818], 'Holy See': [30.034098800664776, -95.81166865095464], 'Isle of Man': [54.1936805, -4.5591148], 'Malta': [35.8885993, 14.4476911], 'Guam': [13.4499943, 144.7651677], 'Iran (Islamic Republic of)': [32.6475314, 54.5643516], 'Uzbekistan': [41.32373, 63.9528098], 'Thailand': [14.8971921, 100.83273], "Lao People's Democratic Republic": [20.0171109, 103.378253], 'Cambodia': [12.5433216, 104.8144914], 'Bahrain': [26.030093, 50.553336789123236], 'Colombia': [4.099917, -72.9088133], 'Georgia': [32.3293809, -83.1137366], 'South Africa': [-28.8166236, 24.991639], 'Cayman Islands': [19.703182249999998, -79.9174627243246], 'Iraq': [33.0955793, 44.1749775], 'Iceland': [64.9841821, -18.1059013], 'Barbados': [13.1500331, -59.5250305], 'Costa Rica': [10.2735633, -84.0739102], 'Oman': [21.0000287, 57.0036901], 'Uganda': [1.5333554, 32.2166578], 'Senegal': [14.4750607, -14.4529612], 'Rwanda': [-1.9646631, 30.0644358], 'Bolivia (Plurinational State of)': [-17.0568696, -64.9912286], 'Tanzania, United Republic of': [-6.5247123, 35.7878438], 'Angola': [-11.8775768, 17.5691241], 'Panama': [8.559559, -81.1308434], 'Qatar': [25.3336984, 51.2295295], 'Greece': [38.9953683, 21.9877132], 'Maldives': [3.7203503, 73.2244152], 'Dominican Republic': [19.0974031, -70.3028026], 'Bosnia and Herzegovina': [44.3053476, 17.5961467], 'Monaco': [43.7323492, 7.4276832], 'Jordan': [44.6663146, -93.6261918], 'Fiji': [-18.1239696, 179.0122737], 'Trinidad and Tobago': [10.7466905, -61.0840075], 'Tunisia': [36.8002068, 10.1857757], 'Argentina': [-34.9964963, -64.9672817], 'Zimbabwe': [-18.4554963, 29.7468414], 'Afghanistan': [33.7680065, 66.2385139], 'Bermuda': [32.3040273, -64.7563086], 'Luxembourg': [49.6112768, 6.129799], 'Libya': [26.8234472, 18.1236723], 'Malawi': [-13.2687204, 33.9301963], 'Mali': [16.3700359, -2.2900239], 'Bahamas': [24.7736546, -78.0000547], 'Hungary': [47.1817585, 19.5060937], 'Liechtenstein': [47.1416307, 9.5531527], 'Latvia': [56.8406494, 24.7537645], 'Estonia': [58.7523778, 25.3319078], 'Belarus': [53.4250605, 27.6971358], 'North Korea': [40.3736611, 127.0870417], 'Algeria': [28.0000272, 2.9999825], 'Sint Maarten': [18.0423736, -63.0549948], 'Mongolia': [46.8250388, 103.8499736], 'Gabon': [-0.8999695, 11.6899699], 'Yemen': [16.3471243, 47.8915271], 'Togo': [8.7800265, 1.0199765], 'Croatia': [45.3658443, 15.6575209], 'Ethiopia': [10.2116702, 38.6521203], 'Sierra Leone': [8.6400349, -11.8400269], 'Seychelles': [-4.6574977, 55.4540146], 'Serbia': [44.024322850000004, 21.07657433209902], 'Jamaica': [18.1850507, -77.3947693], 'Republic of North Macedonia': [41.6171214, 21.7168387], 'Gibraltar': [36.1285933, -5.3474761], 'Cabo Verde': [16.0000552, -24.0083947], 'Hong Kong': [22.350627, 114.1849161], 'Moldova (the Republic of)': [47.0229142, 28.8299748], 'El Salvador': [13.8000382, -88.9140683], 'Papua New Guinea': [-5.6816069, 144.2489081], 'Andorra': [42.5407167, 1.5732033], 'French Guiana': [4.0039882, -52.999998], 'Nauru': [-0.5252306, 166.9324426], 'Peru': [-6.8699697, -75.0458515], 'Zambia': [-14.5189121, 27.5589884], 'Greenland': [43.0361995, -70.8328322], 'Kiribati': [0.3448612, 173.6641773], 'American Samoa': [-14.297124, -170.7131481], 'Uruguay': [-32.8755548, -56.0201525], 'Vanuatu': [-16.5255069, 168.1069154], 'Bonaire': [12.167, -68.28764385602938], 'Guadeloupe': [16.2528827, -61.5686855], 'Cuba': [23.0131338, -80.8328748], 'Tonga': [-19.9160819, -175.202642], 'Puerto Rico': [18.2247706, -66.4858295], 'Saint Vincent and the Grenadines': [12.90447, -61.2765569], 'Palestine, State of': [42.2089038065726, -79.46849684080372], 'Sudan': [34.0678644, -102.524362], 'Nicaragua': [12.6090157, -85.2936911], 'Lesotho': [-29.6039267, 28.3350193], 'Lebanon ': [40.375713, -76.4626118], 'Islamic Republic of Iran': [32.6475314, 54.5643516], 'Taiwan': [23.5983227, 120.83537694479215], 'Czech Republic': [49.7439047, 15.3381061], 'Multiple': [32.7979615, -117.1509655], 'Vietnam': [15.9266657, 107.9650855], 'Kosovo': [42.5869578, 20.9021231], 'European Union': [42.6795963, 23.3214829]})
    #supprimer_lignes_excel("Data2_v2.xlsx", colonne="country", valeur="Undetermined")
    nettoyer_fichier_excel("Data2_v2.xlsx",["event_date","month","organization","source_url","description","motive","actor"])
    delete_all_except("Database2Quanti.xlsx",["start_date","incident_type","receiver_country","receiver_category_subcode","initiator_country",])