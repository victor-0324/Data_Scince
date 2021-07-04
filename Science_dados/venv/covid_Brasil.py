import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

r = requests.get('https://coronavirus-19-api.herokuapp.com/countries')

# print(r.json())

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(f"Current Time: {now}")

js = json.dumps(r.json(), indent=4)
file = open('covid19.json', 'w')
file.write(js)
file.close()

df = pd.read_json('covid19.json')

df.to_csv('covid_19.csv')
# Alterar Brazil pra World caso deseje saber o total de tudo no mundo inteiro e não só no país
# item indicado abaixo fará com que não apareça o Nome e o dtype no print
print(f"Total de casos: {df.loc[df['country'] == 'Brazil', 'cases'].item()}")
print(f"Total de mortos: {df.loc[df['country'] == 'Brazil', 'deaths'].item()}")
print(f"Total de recuperados: {df.loc[df['country'] == 'Brazil', 'recovered'].item()}") 
print(f"Óbitos hoje: {df.loc[df['country'] == 'Brazil', 'todayDeaths'].item()}")
print(f"Casos hoje: {df.loc[df['country'] == 'Brazil', 'todayCases'].item()}")

attribute = 'deaths'

inflim = 1
suplim = 40
countries = df['country'][inflim:suplim]
variable = df[attribute][inflim:suplim]
x = np.arange(0, len(countries), 1)

plt.figure("Covid-19", (13, 6))
plt.title(f"Attribute of the data under analysis: {attribute}")
plt.bar(countries, variable, width=0.8)
plt.xticks(x, countries, rotation=45)
plt.grid(True)
plt.tight_layout(pad=1.0)
plt.show()








