import pandas as pd
from pandas.core.dtypes import dtypes
from pandas.core.reshape.concat import concat
import requests as r 
from geopy.geocoders import Nominatim 
import ipywidgets as widgets
import plotly_express as px 
from ipywidgets import fixed
from matplotlib import colorbar, colors, pyplot as plt 
from matplotlib import cm
from matplotlib import gridspec

data = pd.read_csv('deteset/execício_4.csv')
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#4. Adicione os seguintes filtros no mapa:
#- Tamanho mínimo da área da sala de estar
# - Número mínino de banheiros
# - Valor máximo do preço
# - Tamanho máximo da área do porão
# - Filtro das condições do imóvel
# - Filtro por ano de construção
data['sqft_size'] = '0'
data.loc[(data['sqft_living']>= 0) & (data['sqft_living']< 1427), 'sqft_size'] = 'size_0'
data.loc[(data['sqft_living']>= 1427) & (data['sqft_living']< 1910), 'sqft_size'] = 'size_1'
data.loc[(data['sqft_living']>= 1910) & (data['sqft_living']< 2550), 'sqft_size'] = 'size_2'
data.loc[(data['sqft_living']> 2550), 'sqft_size'] = 'size_3'

print(data['bedrooms'].min())

dt_mapa = data[['id','lat','long','price']].copy()

mapa = px.scatter_mapbox(dt_mapa, lat='lat' , lon='long', 
                        hover_name='id',
                        hover_data =['price'], 
                        color_discrete_sequence=['blueviolet'],
                        size = 'price',
                        zoom=3,
                        height=300)
mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0} )
mapa.show()

#mapa.write_html('deteset/mapa_house_2.html#')
#5. Adicione os seguintes filtros no Dashboard:
# - Filtro por data disponível para compra
#- Filtro por ano de renovação
# - Filtro se possui vista para água ou não.

data_limit = widgets.SelectionSlider(
    options= data['date'].sort_values().unique().tolist(),
    values='2014-12-01',
    description= 'Disponivel',
    continuous_update=False,
    orientation='horizontal',
    readout=True
)


'''def update_map(data,limit):
    data = data[data['date']>= limit].copy() 
    fig = plt.figure(figsize=(21,12)) 
    specs = gridspec.GridSpec(ncols=2 , nrows=2, figure=fig) 
    
    ax1 = fig.add_subplot(specs[0, :])
    ax2 = fig.add_subplot(specs[1, 1]) 
    ax3 = fig.add_subplot(specs[1, 0]) 
    
    by_ano = data[['id','yaer']].groupby('yaer').sum().reset_index() 
    ax2.bar(by_ano['yaer'], by_ano['id'] ) 
    plt.grid()
    ax2.set_xlabel('yaer')
    ax2.set_ylabel('id')

    by_renova = data[['id','yr_renovated']].groupby('yr_renovated').mean().reset_index() 
    ax1.plot(by_renova['yr_renovated'],by_renova['id'])
    plt.grid()
    
    plasma = cm.get_cmap('plasma', 12)
    by_vista = data[['id','waterfront']].groupby('waterfront').sum().reset_index()
    ax3.bar(by_vista['waterfront'],by_vista['id'],color=plasma(range(0,15,2))) 
    
widgets.interactive(update_map,data=fixed(data),limit=data_limit).show() '''