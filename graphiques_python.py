import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt


def charger_donnees(file_path, sheet_name):
    """Charge les données Excel."""
    return pd.read_excel(file_path, sheet_name=sheet_name)


def compter_attaques_par_pays(data):
    """Compte le nombre d'attaques par pays et applique une transformation logarithmique."""
    country_counts = data['actor_country'].value_counts().reset_index()
    country_counts.columns = ['actor_country', 'attack_count']
    country_counts['log_attack_count'] = country_counts['attack_count'].apply(lambda x: np.log1p(x))
    return country_counts


def charger_shapefile(file_path):
    """Charge le shapefile des pays."""
    return gpd.read_file(file_path)


def appliquer_corrections_noms(country_counts, correction_noms):
    """Applique les corrections de noms de pays dans le DataFrame."""
    country_counts['actor_country'] = country_counts['actor_country'].replace(correction_noms)
    return country_counts


def fusionner_donnees_shapefile(world, country_counts):
    """Fusionne les données des attaques avec le shapefile."""
    return world.merge(country_counts, how='left', left_on='ADMIN', right_on='actor_country')


def creer_carte(world, title, cmap='OrRd'):
    """Crée et affiche une carte des données avec une échelle semi-logarithmique."""
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1, color='black')  # Tracer les frontières des pays
    world.plot(
        ax=ax,
        column='log_attack_count',
        cmap=cmap,
        legend=True,
        legend_kwds={
            'label': "Nombre d'attaques (logarithme)",
            'orientation': "horizontal"
        },
        missing_kwds={
            "color": "lightgrey",
            "label": "Pas de données"
        }
    )
    ax.set_title(title, fontsize=15)
    ax.axis("off")  # Cacher les axes
    plt.show()


def analyser_evolution_attaques_par_annee(data):
    """Analyse l'évolution du nombre d'attaques chaque année."""
    data['event_date'] = pd.to_datetime(data['event_date'])
    attacks_per_year = data.groupby(data['year']).size()
    plt.figure(figsize=(12, 8))
    attacks_per_year.plot(kind='line', marker='o', color='b')
    plt.title("Évolution du nombre d'attaques par année")
    plt.xlabel("Année")
    plt.ylabel("Nombre d'attaques")
    plt.grid(True)
    plt.xticks(attacks_per_year.index, rotation=45)
    plt.tight_layout()
    plt.show()


def analyser_industries_par_annee(data):
    """Analyse les industries les plus attaquées par année."""
    data['industry'] = data['industry'].str.strip().str.lower()
    data['industry'] = data['industry'].replace("professional, scientific, and technical services", "PSTS")
    data_filtered = data[data['industry'].notnull()]
    attacks_by_industry_year = data_filtered.groupby(['year', 'industry']).size().unstack(fill_value=0)

    for year in attacks_by_industry_year.index:
        print(f"\nClassement des secteurs les plus attaqués en {year}:")
        industry_rank = attacks_by_industry_year.loc[year].sort_values(ascending=False)
        print(industry_rank.head(10))

        plt.figure(figsize=(10, 6))
        industry_rank.head(10).plot(kind='bar', color='lightcoral')
        plt.title(f"Top 10 des secteurs les plus attaqués en {year}")
        plt.xlabel('Secteurs')
        plt.ylabel("Nombre d'attaques")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def analyser_pays_par_annee(data):
    """Analyse les pays les plus attaquants par année."""
    data['actor_country'] = data['actor_country'].replace({
        "United Kingdom of Great Britain and Northern Ireland": "UK",
        "Korea (the Democratic People's Republic of)": "North Korea"
    })
    data_filtered = data[data['actor_country'] != 'Undetermined']
    attacks_by_country_year = data_filtered.groupby(['year', 'actor_country']).size().unstack(fill_value=0)

    for year in attacks_by_country_year.index:
        print(f"\nClassement des pays qui ont le plus attaqués en {year}:")
        country_rank = attacks_by_country_year.loc[year].sort_values(ascending=False)
        print(country_rank.head(10))

        plt.figure(figsize=(10, 6))
        country_rank.head(10).plot(kind='bar', color='skyblue')
        plt.title(f"Top 10 des pays qui ont le plus attaqués en {year}")
        plt.xlabel('Pays')
        plt.ylabel("Nombre d'attaques")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Exemple d'utilisation
file_path = r'C:\Users\aissa\Desktop\IC05\projet\Data2_v2.xlsx'
shapefile_path = r'C:\Users\aissa\Desktop\IC05\projet\shapefiles\naturalearth_lowres.shp'
correction_noms = {
    "USA": "United States of America",
    "UK": "United Kingdom",
    "Taiwan (Province of China)": "Taiwan",
    "Iran (Islamic Republic of)": "Iran",
    "Venezuela (Bolivarian Republic of)": "Venezuela",
    "Tanzania, United Republic of": "United Republic of Tanzania",
    "Korea (the Democratic People's Republic of)": "North Korea",
    "Korea (the Republic of)": "South Korea",
    "Russia": "Russian Federation",
    "Moldova (the Republic of)": "Moldova",
    "Syria": "Syrian Arab Republic",
    "Lao People's Democratic Republic": "Laos",
    "Hong Kong": "China",
    "Czech Republic": "Czechia",
    "Malta": "Republic of Malta",
    "Serbia": "Republic of Serbia",
    "Palestine, State of": "Palestine",
    "The Bahamas": "Bahamas",
    "Democratic Republic of the Congo": "Democratic Republic of the Congo",
    "Republic of the Congo": "Congo",
    "Venezuela (Bolivarian Republic of)": "Venezuela",  # Nom corrigé de l'Excel vers le shapefile
    "Russian Federation": "Russia",
    "Moldova (the Republic of)": "Moldova",
    "Venezuela": "Venezuela (Bolivarian Republic of)",  # Ajout inverse pour les incohérences
    "Isle of Man": "United Kingdom",
    "Malta": "Malta",
    "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Maldives": "Maldives",
    "Republic of North Macedonia": "North Macedonia",
    "Undetermined": "Not Determined",
    "Liechtenstein": "Liechtenstein",
    "Gibraltar": "Gibraltar",
    "Czech Republic": "Czechia",  # Correction vers nom normalisé
    "Guadeloupe": "Guadeloupe",
    "Sint Maarten": "Sint Maarten",
    "Guam": "Guam",
    "Viet Nam": "Vietnam",  # Correction pour correspondance internationale
    "Bahamas": "The Bahamas",
    "American Samoa": "American Samoa",
    "Iran (Islamic Republic of)": "Iran",
    "Syrian Arab Republic": "Syria",  # Simplification des noms
    "Taiwan (Province of China)": "Taiwan",
    "European Union": "European Union",
    "Hong Kong": "Hong Kong",
    "Palau": "Palau",
    "Nauru": "Nauru",
    "French Guiana": "French Guiana",
    "Multiple": "Multiple",
    "Kiribati": "Kiribati",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Cabo Verde": "Cape Verde",
    "Bermuda": "Bermuda",
    "Bolivia (Plurinational State of)": "Bolivia",
    "Serbia": "Serbia",
    "Monaco": "Monaco",
    "Bahrain": "Bahrain",
    "Korea (the Democratic People's Republic of)": "North Korea",  # Simplification
    "Seychelles": "Seychelles",
    "Holy See": "Holy See",
    "Andorra": "Andorra",
    "Bonaire, Sint Eustatius and Saba": "Bonaire, Sint Eustatius and Saba",
    "Cayman Islands": "Cayman Islands",
    "Palestine, State of": "Palestine",
    "Lao People's Democratic Republic": "Laos",
    "Islamic Republic of Iran": "Iran",
    "Korea (the Republic of)": "South Korea",  # Normalisation des noms
    "Singapore": "Singapore",
    "Tanzania, United Republic of": "United Republic of Tanzania",
    "Lebanon ": "Lebanon",
    "Tonga": "Tonga"
}
correction_noms.update({
    "French Southern and Antarctic Lands": "French Southern and Antarctic Lands",
    "Chad": "Chad",
    "Djibouti": "Djibouti",
    "Somaliland": "Somaliland",
    "eSwatini": "eSwatini",
    "Botswana": "Botswana",
    "South Sudan": "South Sudan",
    "Liberia": "Liberia",
    "Central African Republic": "Central African Republic",
    "Equatorial Guinea": "Equatorial Guinea",
    "Syria": "Syrian Arab Republic",
    "Antarctica": "Antarctica",
    "Guinea-Bissau": "Guinea-Bissau",
    "Burundi": "Burundi",
    "Mozambique": "Mozambique",
    "Guinea": "Guinea",
    "Benin": "Benin",
    "Gambia": "Gambia",
    "Burkina Faso": "Burkina Faso",
    "Kyrgyzstan": "Kyrgyzstan",
    "Somalia": "Somalia",
    "Brunei": "Brunei",
    "Western Sahara": "Western Sahara",
    "Mauritania": "Mauritania",
    "East Timor": "East Timor",
    "Honduras": "Honduras",
    "Madagascar": "Madagascar",
    "Suriname": "Suriname",
    "Guyana": "Guyana",
    "Republic of Serbia": "Republic of Serbia",
    "Solomon Islands": "Solomon Islands",
    "Niger": "Niger",
    "Bolivia": "Bolivia",
    "Ivory Coast": "Ivory Coast",
    "Falkland Islands": "Falkland Islands",
    "Laos": "Laos",
    "Belize": "Belize",
    "Cameroon": "Cameroon",
    "Republic of the Congo": "Congo",
    "Bhutan": "Bhutan",
    "North Macedonia": "North Macedonia",
    "New Caledonia": "New Caledonia",
    "Iran": "Iran",
    "Moldova": "Moldova"
})

data = charger_donnees(file_path, sheet_name=0)
world = charger_shapefile(shapefile_path)
country_counts = compter_attaques_par_pays(data)
country_counts = appliquer_corrections_noms(country_counts, correction_noms)
world = fusionner_donnees_shapefile(world, country_counts)
creer_carte(world, "Carte des pays attaquants (Échelle semi-logarithmique)")
analyser_evolution_attaques_par_annee(data)
analyser_industries_par_annee(data)
analyser_pays_par_annee(data)
