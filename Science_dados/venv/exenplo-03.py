from numpy.core.fromnumeric import mean
import pandas as pd
from numpy import int64
from matplotlib import colorbar, colors, pyplot as plt 
from matplotlib import cm
from matplotlib import gridspec
import streamlit

data = pd.read_csv('deteset/kc_house_data.csv') 
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#$$$$$$$$$$$$$$$$$(Novas pergunta do ceo)$$$$$$$$$$$$$$$$$$$$$$$
#1. Crie uma nova coluna chamada:"dormitory_type"
 #-Se o valor da coluna " bedrooms" for igual a 1 => 'studio'
 #-Se o valor da coluna "bedrooms" for igual a 2 => 'apartament'
 #-Se o valor da coluna "bedroms" for maior que 2 => 'house'
data['dormitory_type'] = None
data.loc[data['bedrooms']== 1,'dormitory_type'] = 'studio'
data.loc[data['bedrooms']== 2,'dormitory_type'] = 'apartament'
data.loc[data['bedrooms']>  2,'dormitory_type'] = 'house'

#2.Faça um gráfico de barras que representa a soma dos preços pelo 
#número de quartos.
grafic = data[['price','bedrooms']].groupby('bedrooms').sum().reset_index()
plt.figure(figsize=(5,4))
plt.grid(axis='y')
plt.xlabel('number of bedrooms')
plt.ylabel('price')
plasma = cm.get_cmap('plasma', 12)
plt.bar(grafic['bedrooms'], grafic['price'],color=plasma(range(0,15,2)))
plt.show()

#3.Faça um gráfico de linhas que representa a media dos preços pelo 
#ano de construção de imoveis.
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y') 
grf = data[['price','yr_built']].groupby('yr_built').mean().reset_index() 
plt.figure(figsize=(10,4))
plt.grid()
plt.xlabel('yr_built')
plt.ylabel('price')
plt.plot(grf['yr_built'], grf['price'],color='red')
plt.xticks(rotation=50)
plt.show()

#4.Faça um gráfico de barras que representa a media dos preços pelo 
#tipo de dormitórios
media = data[['price','dormitory_type']].groupby('dormitory_type').mean().reset_index()
plt.figure(figsize=(10,4))
plt.grid(axis='y')
plasma = cm.get_cmap('plasma', 12)
plt.bar(media['dormitory_type'],media['price'],color=plasma(range(0,20,2)))
plt.show()

#5.Faça um gráfico de linhas que mostre a evolução da media dos 
#preços pelo ano de reforma dos imoveis, a parti do ano de 1930.
by_renovated = data[['price','yr_renovated']].groupby('yr_renovated').mean().reset_index()
by_renovated = by_renovated.loc[by_renovated['yr_renovated']>=1930,:]
plt.figure(figsize=(10,4))
plt.grid(axis='y')
plt.plot(by_renovated['yr_renovated'],by_renovated['price'],color='black')
plt.xticks(rotation=40)
plt.show()

#6.Faça uma tabela que mostra a média dos preços por ano de 
#contrução e tipo de dormitórios dos imoveis
meanpby_built_type = data[["price", "yr_built", "dormitory_type"]].groupby(["yr_built", "dormitory_type"]).mean().reset_index()
print(meanpby_built_type)

#7. Crie um Dashboard com os gráficos das questões 02,03,04
#(Dashboard:1 Linha e 2 coluna)
fig = plt.figure(figsize=(10,5))
specs = gridspec.GridSpec(ncols=2,nrows=2,figure=fig)
ax2 =fig.add_subplot(specs[0, :])
ax1 =fig.add_subplot(specs[1, 0])
ax3 =fig.add_subplot(specs[1, 1])

#1.grafico
grafic = data[['price','bedrooms']].groupby('bedrooms').sum().reset_index()
ax1.grid(axis='y')
ax1.set_xlabel('number of bedrooms')
ax1.set_ylabel('price')
plasma = cm.get_cmap('plasma', 12)
ax1.bar(grafic['bedrooms'], grafic['price'],color=plasma(range(0,20,2)))

#2.grafico
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y') 
grf = data[['price','yr_built']].groupby('yr_built').mean().reset_index() 
ax2.grid()
ax2.set_xlabel('yr_built')
ax2.set_ylabel('price')
ax2.plot(grf['yr_built'], grf['price'],color='purple')

#.3 colunas
media = data[['price','dormitory_type']].groupby('dormitory_type').mean().reset_index()
ax3.grid(axis='y')
plasma = cm.get_cmap('plasma', 12)
ax3.bar(media['dormitory_type'],media['price'],color=plasma(range(0,20,2)))
fig.tight_layout(pad=0.7)
plt.show()

#8. Crie um Dashboard com os gráficos das perguntas 02,04
#(Dashboard:2colunas
fig = plt.figure(figsize=(13,5))
spec = gridspec.GridSpec(ncols=2, nrows=1 ,figure=fig)
ax4 = fig.add_subplot(spec[0, :])
ax5 = fig.add_subplot(spec[0, 1])

grafic = data[['price','bedrooms']].groupby('bedrooms').sum().reset_index()
ax4.grid(axis='y')
plasma = cm.get_cmap('plasma', 12)
ax4.bar(grafic['bedrooms'], grafic['price'],color=plasma(range(0,15,2)))

media = data[['price','dormitory_type']].groupby('dormitory_type').mean().reset_index()
ax5.grid(axis='y')
plasma = cm.get_cmap('plasma', 12)
ax5.bar(media['dormitory_type'],media['price'],color=plasma(range(0,20,2)))
fig.tight_layout(pad=0.7)
plt.show()



