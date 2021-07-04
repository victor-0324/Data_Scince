#carregar biblotecas
from datetime import date, datetime, time
from typing import Match
from numpy.core.fromnumeric import shape
import pandas as pd 
from numpy import int64
from pandas.core.dtypes import dtypes

#carrega um arquivo do disco rigido para a memoria 
dt = pd.read_csv('deteset/kc_house_data.csv')

#converte date de objet para data:
dt['date'] = pd.to_datetime(dt['date']) 

#1. Qual a data do imóvel mais antigo no portfólio? 
#print(f"O imoveis mas antigo no portifolio e: {dt.sort_values('date',ascending=True)}")

#2. Quantos imóveis possuem o número máximo de andares?
#print(dt[dt['floors']==3.5].shape)

#3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrã o de acordo com o preço 
#acima de 540.000 = alto padrão 
#Abaixo de 540.00 = baixo padrão
#dt['level'] = 'standard'
#print(dt.columns)
#dt.loc[dt['price']>540000,'level'] = 'higt_level'
#dt.loc[dt['price']<54000,'level']= 'low_level'
#print(dt.head)

#4. Fazer um relatório ordenado pelo preço e contendo as seguintes informações: 
#Id do imóvel 
#Data que o imóvel ficou disponível para compra
#O número de quartos
#O tamanho total do terreno
#O preço
#A classificação do imóvel (alto e baixo padrão)
#report = dt[['id','date','price','bedrooms','sqft_lot','level']].sort_values('price', ascending=False)
#print(report.head())
#report.to_csv('deteset/exenplo2.csv',index=False)

#potly - Biblioteca que usa uma funçao que desenha mapas
#5. Criar um mapa indicando onde as casas estão localizadas geograficamente
#Scatter Mapbox - funçao que desenha o mapa
#import plotly_express as px
#dt_mapa = dt[['id','lat','long','price']]

#mapa = px.scatter_mapbox(dt_mapa, lat='lat' , lon='long', 
#hover_name='id',
#hover_data =['price'], 
#color_discrete_sequence=['blueviolet'],
#zoom=3,
#height=300)
#mapa.update_layout(mapbox_style='open-street-map')
#mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0} )
#mapa.show() 
#mapa.write_html('deteset/mapa_house.html#')
#=======================================//=======================================================

#6. Crie um anova coluna chamada: "house_age"
#- Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house
#- Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house
dt['house_age'] = 'old'
dt.loc[dt['date']> '2014-01-01','house_age'] = 'new_house'
dt.loc[dt['date']< '2014-01-01','house_age'] = 'old_house'

#7. Crie uma nova coluna chamada: "dormitory_type"
#- Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
#- Se o valor da coluna "bedrooms" for igual à 2 => 'apartament'
#- Se o valor da coluna "bedrooms" for maior que 2 => 'house'
dt['dormitory_type'] = '0'
dt.loc[dt['bedrooms']==1,'dormitory_type'] = 'studio'
dt.loc[dt['bedrooms']==2,'dormitory_type'] = 'apartament'
dt.loc[dt['bedrooms']>2,'dormitory_type'] = 'house'

#8. Crie uma nova coluna chamada: "condition_type"
#- Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
#- Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
#- Se o valor da coluna "condition" for igual à 5 => 'good'
dt['condition_type'] = 'none'
dt.loc[dt['condition']<= 2,'condition_type']= 'bad'
dt.loc[(dt.condition==3)|(dt.condition==4),'condition_type']= 'regular'
dt.loc[dt['condition']== 5,'condition_type']= 'good'
#print(dt['condition_type'])

#9. Modifique o TIPO da coluna "condition" para STRING
dt['condition'] = pd.to_datetime(dt['condition'])
dt['condition'] = dt['condition'].astype(str)

#10. Delete as colunas "sqft_living15" e "sqft_lot15"
cols = ['sqft_living15','sqft_lot15']
dt = dt.drop(cols,axis=1)

#11. Modifique o TIPO da coluna "yr_built" para DATE
dt['yr_built'] = pd.to_datetime(dt['yr_built'], format='%Y')

#12. Modifique o TIPO da coluna "yr_renovated" para DATE
dt['yr_renovatede'] = pd.to_datetime(dt['yr_renovated'],format='%Y',errors='coerce')

#13. Qual a data mais antiga de construção de um imóvel?
#print(f"A data mas antiga de contruçao e:{dt['yr_built'].min()}")

#14. Qual a data mais antiga de renovação de um imóvel?
#print(f"A data mais antiga de renovaçao e:{dt['yr_renovated'].min()}")

#15. Quantos imóveis tem 2 andares?
#print(f"imoveis com 2 andares:{dt[dt['floors']==2].shape}")

#16. Quantos imóveis estão com a condição igual à "regular"?
#print(f"Imoveis com condiçao igual a regula:{dt.loc[dt['condition_type']== 'regular'].shape}")

#17. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para água"?
#print(f"Imoveis com a condição igual a 'bad' e possuem vista para o mar{dt.loc[(dt.condition_type == 'bad')&(dt.waterfront == 1 )].shape}")

#18. Quantos imóveis estão com a condição igual a "good" e são "new_house"?
#print(f"Os imoveis que sao 'good' e sao 'new_house':{dt.loc[(dt.condition_type =='good')|(dt.sort_values == 'new_house')].shape}")

#19. Qual o valor do imóvel mais caro do tipo "studio"?
#print(f"O imovel mas caro do tipo studio: {dt.loc[(dt.dormitory_type=='studio')|(dt.sort_values == 'price')].describe().max()}")

#20. Quantos imóveis do tipo "apartament" foram reformados em 2015?
#print(f"os apartamento que foram reformado em 2015:{dt.loc[(dt.dormitory_type == 'apartament')&(dt.yr_renovated == 2015-0-0 )].shape}")

#21. Qual o maior número de quartos que um imóvel do tipo "house" possui?
#print(f"O maior numero de quartos do tipo house {dt.loc[(dt.sort_values == 'bedrooms')|(dt.dormitory_type == 'house')].max()}")

#22. Quandos imóveis "new_house" foram reformados no ano de 2014?
#print(f"foram reformados em 2014: {dt.loc[(dt.house_age == 'new_house')&(dt.yr_renovated == 2014-0-0)].shape} ")

#23. Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelo método:
#- Direto pelo nome das colunas
#- Pelos índices
#- Pelos índices das linhas e o nome das colunas
#- Índices booleanos 
#print(dt[['id','date','price','floors','zipcode']])
#print(dt[['id','date','price','floors','zipcode']].sort_index())
#print(dt[['id','date','price','floors','zipcode']].index.head())

#24. Salve um arquivo .csv com somente as colunas do item 10 
report= dt[['view', 'condition', 'grade','sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode','lat', 'long', 'house_age', 'dormitory_type', 'condition_type']]
report.to_csv('deteset/execício_2.csv',index=False)

#25. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro'