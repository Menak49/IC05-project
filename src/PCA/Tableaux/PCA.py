

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
import plotly.express as px


def analyse_pca(excel_path, columns_to_analyze, country_column='Pays', n_components=2):
    """
    Effectue une analyse PCA sur un fichier Excel contenant des données sur des pays.

    Args:
    - excel_path (str): Chemin vers le fichier Excel.
    - columns_to_analyze (list): Liste des colonnes numériques à inclure dans l'analyse PCA.
    - country_column (str): Nom de la colonne contenant les noms des pays (par défaut : 'Pays').
    - n_components (int): Nombre de composantes principales à conserver (par défaut : 2).

    Returns:
    - pca_df (pd.DataFrame): Résultats de la PCA avec les pays et les composantes principales.
    """
    # Charger les données depuis le fichier Excel
    df = pd.read_excel(excel_path)
    print("Données originales :")
    print(df.head())

    # Remplacer "No Data" par NaN pour faciliter le traitement des valeurs manquantes
    df = remplacer_no_data_par_moyenne(df, columns_to_analyze)

    # Gérer les valeurs manquantes en les remplissant avec la moyenne des colonnes
    for col in columns_to_analyze:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].astype(float).fillna(df[col].mean())

    # Extraire les colonnes numériques pour la PCA
    data_to_analyze = df[columns_to_analyze]

    # Standardiser les données
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_to_analyze)

    # Appliquer la PCA
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(data_scaled)

    # Créer un DataFrame avec les résultats de la PCA
    pca_df = pd.DataFrame(pca_result, columns=[f'PC{i + 1}' for i in range(n_components)])
    pca_df[country_column] = df[country_column]

    # Afficher la variance expliquée
    explained_variance = pca.explained_variance_ratio_
    print(f"Variance expliquée par chaque composante principale : {explained_variance}")
    print(f"Variance totale expliquée : {sum(explained_variance):.2f}")

    # Visualisation 2D si le nombre de composantes est >= 2
    if n_components >= 2:
        # Création du graphique pour la projection sur les deux premières composantes principales
        plt.figure(figsize=(10, 7))
        plt.scatter(pca_df['PC1'], pca_df['PC2'], c='blue', alpha=0.7)
        for i, country in enumerate(pca_df[country_column]):
            plt.text(pca_df['PC1'][i], pca_df['PC2'][i], country, fontsize=8)

        # Affichage des labels pour les axes, avec la variance expliquée
        plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f} variance expliquée)')
        plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f} variance expliquée)')
        plt.title('Projection des pays sur les deux premières composantes principales')
        plt.grid()
        plt.show()

    # Biplot (optionnel) : Montrer les variables avec les flèches
    if n_components >= 2:
        loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
        plt.figure(figsize=(10, 7))
        plt.scatter(pca_df['PC1'], pca_df['PC2'], c='blue', alpha=0.7)
        for i, country in enumerate(pca_df[country_column]):
            plt.text(pca_df['PC1'][i], pca_df['PC2'][i], country, fontsize=8)

        # Ajouter les flèches pour les variables (les charges des variables sur les PC)
        for i, var in enumerate(columns_to_analyze):
            plt.arrow(0, 0, loadings[i, 0], loadings[i, 1], color='red', alpha=0.7)
            plt.text(loadings[i, 0] * 1.15, loadings[i, 1] * 1.15, var, color='red', fontsize=10)

        # Affichage des labels pour les axes avec la variance expliquée
        plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2f} variance expliquée)')
        plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2f} variance expliquée)')
        plt.title('Biplot : PCA avec variables')
        plt.grid()
        plt.show()

    # Retourner les résultats
    return pca_df


import pandas as pd
import streamlit as st
import plotly.express as px

def analyse_excel(path):
    """Fonction pour analyser un fichier Excel avec 4 colonnes spécifiques."""
    st.title("Analyse des données : IDH, Internet et Cyberattaques")

    # Lecture des données
    try:
        data = pd.read_excel(path)

        # Afficher les données brutes
        st.write("### Aperçu des données")
        st.dataframe(data)

        # Colonnes requises
        required_columns = ['country', 'IDH', 'Connections Internet (en %)', 'count']
        if all(col in data.columns for col in required_columns):
            # Statistiques descriptives
            st.write("### Statistiques descriptives")
            st.write(data.describe())

            # Graphique 1 : Barplot IDH par pays
            st.write("### Distribution de l'IDH par pays")
            fig1 = px.bar(data, x='country', y='IDH', title='IDH par pays', text='IDH')
            st.plotly_chart(fig1)

            # Graphique 2 : Scatter plot Connexion Internet vs Cyberattaques
            st.write("### % de Connexion Internet vs Nombre de Cyberattaques")
            fig2 = px.scatter(
                data,
                x='Connections Internet (en %)',
                y='count',
                size='IDH',
                color='country',
                title='% de Connexion Internet vs Nombre de Cyberattaques',
                hover_name='country'
            )
            st.plotly_chart(fig2)
        else:
            st.error("Le fichier doit contenir les colonnes suivantes : " + ", ".join(required_columns))
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")





if __name__ == "__main__":
    # Chemin vers votre fichier Excel
    #excel_path = "fichier_avec_idh.2.2.xlsx"

    # Colonnes numériques pour l'analyse PCA
    #columns_to_analyze = ['IDH','Connections Internet (en %)',  'count']

    # Exécuter l'analyse PCA
    #pca_results = analyse_pca(excel_path, columns_to_analyze, country_column='country', n_components=2)

    # Afficher les résultats
    #print(pca_results)
    #analyse_excel("fichier_avec_idh.2.2.xlsx")

    df = pd.read_excel("fichier_nettoye1.xlsx")
    df.to_csv("fichier_net.csv")
    """

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)


    df_nettoye = df[~((df.isnull().any(axis=1)) | (df.eq("No data").any(axis=1)))]


    # Sauvegarder le fichier nettoyé au format Excel
    df_nettoye.to_excel("fichier_nettoye1.xlsx", index=False)"""

















