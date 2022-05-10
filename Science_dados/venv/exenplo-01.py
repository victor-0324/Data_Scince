#importando biblioteca pandas 
import pandas as pd

data = pd.read_csv('deteset/kc_house_data.csv') 
data = data.drop_duplicates(subset=['id'], keep='first')

# 1. Mostre na tela as 5 primeiras linhas do conjunto de dado
print(data.head())

# 2. Mostre o numero de linhas e de colunas  
print(data.shape)

# 3. Mostre o nome das colunas 
print(data.columns) 

# 4. Mostre na tela o conjunto de dados ordenado pela coluna price 
print(data[['id','price']].sort_values('price')) 

# 5. Mostre na tela o conjunto de dados ordenado pela coluna price do maior para o menor 
print(data[['id','price']].sort_values('price' , ascending=False))

# 6. Quantos quartos tem no conjunto de dados
print(data['bedrooms'].sum()) 

# 7. Quantas casas possuem dois banheiros 
print(data.loc[data['bathrooms'] == 2, 'id']) 

# 8. Qual o proço medio de todas as casas no conjunto de dados
print(data.describe()) 
 
# 9. Qual o preço médio de casas com 2 banheiros?
print(data.loc[data['bathrooms']==2, 'price'].mean())

# 10. Qual o preço mínimo entre as casas com 3 quartos?
print(data.loc[data['bedrooms']== 3, 'price'].describe()) 

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
print(len(data.loc[data['sqft_living'] > 300, 'sqft_living']))
    
#12. Quantas casas tem mais de 2 andares?
print(len(data.loc[data['floors']>2, 'floors']))

#13. Quantas casas tem vista para o mar?
print(len(data.loc[data['waterfront']!= 0, 'waterfront']))
    
#14. Das casas com vista para o mar, quantas tem 3 quartos?
print(len(data.loc[(data['waterfront']!=0) & (data['bedrooms']==3), 'id']))
    
#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
print(len(data.loc[(data['sqft_living'] > 300) & (data['bathrooms'] > 2),'id'])) 


print(data.shape)
