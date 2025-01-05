library(FactoMineR)
library(factoextra)
library(readxl)
library(Factoshiny)
# Charger les données
data <- read_excel("fichier_pour_ACM_nettoye.xlsx")

# Vérifier et convertir les colonnes en facteurs
data <- data.frame(lapply(data, as.factor))

# Réaliser l'ACM
res <- MCA(data, graph = FALSE)
MCAshiny(data)

# Visualisation du cercle des corrélations avec noms des variables
fviz_mca_var(res, 
             choice = "mca.cor", 
             col.var = "blue", 
             repel = TRUE, 
             geom = c("arrow","text")) +
  coord_fixed() +
  ggtitle("Cercle des corrélations - Variables actives")

"
# Convertir en facteurs
data_acm <- data.frame(lapply(data_acm, as.factor))

# Réaliser l'ACM
resultat_acm <- MCA(data_acm, graph = FALSE)

# Visualiser les individus et modalités ensemble
fviz_mca_var(resultat_acm)
""
