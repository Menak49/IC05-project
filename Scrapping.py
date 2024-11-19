from bs4 import BeautifulSoup
import requests
import csv
import re  # module for regular expression
# test
if __name__ == "__main__":

    links = []  # ensemble des sites web interessants
    response = requests.get(
        'https://www.jedha.co/formation-cybersecurite/liste-des-organisations-victimes-dune-cyberattaque-en-2024')
    soup = BeautifulSoup(response.content, "html.parser")
    soup.prettify()
    print(response)  # looking if the connection worked


    def get_all_line():
        all_line = []
        count=0
        for item in soup.select("li"):
            text = item.get_text(strip=True)
            if count > 1:
                all_line.append(text)
            count += 1
        return all_line


    def get_entreprise():
        entreprise = []
        for item in soup.select("li strong"):
            text = item.get_text(strip=True)
            entreprise.append(text)
        return entreprise


    def get_dates():
        dates = []
        for item in soup.select("li"):
            text = item.get_text()
            date_match = re.search(r'\d{1,2} \w+ 2024', text)
            if date_match:
                dates.append(date_match.group())
        return dates


    def get_type():
        type = []
        for item in soup.select("li"):
            text = item.get_text()
            type_match = re.search(r'-\s+\d{1,2} \w+ 2024\s+-\s+(.*?)\s*\(', text)
            if type_match:
                type.append(type_match.group(1).strip())
        return type

#correction pour les entreprises
    entreprise = get_entreprise()
    correction = []
    for elt in entreprise:
        if elt != "\u200d":
            correction.append(elt)
entreprise = correction

#correction pour les dates et types
dates = get_dates()
dates.append("22 août 2024")
type=get_type()
type.append("Mise en vente des données de 60 000 allocataires sur le DarkWeb")

# insert into the csv file

with open('cyber_attack.csv', 'w', encoding='utf-8',newline='' ) as file:
    writer = csv.writer(file)
    field = ["entreprise","date","type"]
    ls_entreprise = entreprise
    ls_dates = dates
    ls_types = type
    writer.writerow(field)
    for i in range(len(entreprise)):
        writer.writerow([ls_entreprise[i],ls_dates[i],ls_types[i]])
    file.close()

