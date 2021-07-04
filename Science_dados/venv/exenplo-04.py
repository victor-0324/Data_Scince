import pandas as pd
from pandas.core.dtypes import dtypes
from pandas.core.reshape.concat import concat
import requests as r 
from geopy.geocoders import Nominatim 
import ipywidgets as widgets
import plotly_express as px

data = pd.read_csv('deteset/kc_house_data.csv') 
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#1. Qual a quantidade de imóveis por nível?
# - Nivel 0: Preço entre R$ 0.00 e R$ 321.950
# - Nivel 1: Preço entre R$ 321.950 e R$ 450.000
# - Nivel 2: Preço entre R$ 450.000 e R$ 645.000
# - Nivel 3: Preço entre R$ Acima de R$ 645.000
#_Primeiro vou criar uma nova coluna chamada nivel.
#_Para cada valor  de price colocarei referente a o nivel. 
data['nivel'] = 'na'
data.loc[(data['price'] >= 0) & (data['price']< 321950),'nivel'] = 'nivel_i'
data.loc[(data['price']>= 320950)&(data['price']< 450000),'nivel'] = 'nivel_1'
data.loc[(data['price']>= 450000)&(data['price']< 645000),'nivel'] = 'nivel_2'
data.loc[(data['price']> 645000),'nivel'] = 'nivel_3' 
print(data['bedrooms'].max())
#2. Qual a média do tamanho da sala de estar dos imoveis por "size"?
#- Size 0: Tamanho entre 0 e 1427 sqft
# - Size 1: Tamanho entre 1427 e 1910 sqft
#- Size 2: Tamanho entre 1910 e 2550 sqft
# - Size 3: Tamanho acima de 2550 sqtf
data['sqft_size'] = 'i'
data.loc[(data['sqft_living']>= 0) & (data['sqft_living']< 1427), 'sqft_size'] = 'size_i'
data.loc[(data['sqft_living']>= 1427) & (data['sqft_living']< 1910), 'sqft_size'] = 'size_1'
data.loc[(data['sqft_living']>= 1910) & (data['sqft_living']< 2550), 'sqft_size'] = 'size_2'
data.loc[(data['sqft_living']> 2550), 'sqft_size'] = 'size_3' 

#3. Adicione as seguintes informações ao conjunto de dados original?
# - Place ID:Identificação da localização
#- OSM type: Open Street Map Type
# - Country: Nome do País
# - Country CODE: Código do País  
data['place_id']    = 'na' 
data['osm_type']    = 'na' 
data['country']     = 'na' 
data['coutry_code'] = 'na'

geolocator = Nominatim(user_agent='execici') 
data = data.head(200)

for i in range(len(data) ):
    # concatenando lat e long
    query = str(data.loc[i,'lat']) + ',' + str(data.loc[i,'long']) 
     
    #passando por lat e long
    response = geolocator.reverse(query)

    data.loc[i,'place_id']   =  response.raw['place_id']
    data.loc[i,'osm_type']   =  response.raw['osm_type'] 

    if 'coutry' in response.raw['address']:    
        data.loc[i,'country']    =  response.raw['address']['country'] 
    elif 'coutry_type' in response.raw['address']:   
        data.loc[i,'coutry_code']=  response.raw['address']['country_code']
    print(i)

#rsp_geolocator = data.sample(100)
#rsp_geolocator.to_csv('deteset/execício_4.csv',index=False)





