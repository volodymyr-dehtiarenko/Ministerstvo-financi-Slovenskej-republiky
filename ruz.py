import requests, json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# URL
from matplotlib.ticker import MultipleLocator

url_kraje = 'https://www.registeruz.sk/cruz-public/api/kraje'
url_okresy = 'https://www.registeruz.sk/cruz-public/api/okresy'
url_sablony = 'https://www.registeruz.sk/cruz-public/api/sablony'
api_kraje = requests.get(url_kraje).text
api_okresy = requests.get(url_okresy).text
api_sablony = requests.get(url_sablony).text
ext_js_kraje = json.loads(api_kraje)
ext_js_okresy = json.loads(api_okresy)
ext_js_sablony = json.loads(api_sablony)


# print('-= Example N1 =-')
# # By For Loops
for item in ext_js_kraje['lokacie']:
    print(item['kod'].ljust(5, ' '), item['nazov']['sk'].ljust(20, ' '), item['nazov']['en'], sep='\t')

print('-= Example N2 =-')
# By Pandas

_okresy = pd.json_normalize(ext_js_okresy['lokacie'])
print(_okresy)

# print('-= Example N3 =-')
# # By Matplotlib
def data_plot():
    x_list = []
    y_list = []
    for item in ext_js_kraje['lokacie']:
        x_list.append(item['nazov']['sk']+' '+(item['kod']))
        y_list.append(item['kod'])
    return x_list
np.random.seed(8361)
perfomens = 3 + 10 * np.random.rand(len(data_plot()))
plt.barh(width = perfomens, y=data_plot(), align='center', label = 'Slovensko')
plt.title('Zodpovedá ŠÚSR číselníku 0023/RSUJ3', fontsize = 16, color = 'red')
plt.ylabel('Lokacie')
plt.xlabel('Rok 2021',color='red')
plt.legend()
plt.grid()
plt.show()

# print('-= Example N4 =-')
# # By Matplotlib
def data_plot():
    x_list = []
    for item in ext_js_kraje['lokacie']:
        x_list.append(item['kod'])
    return x_list
np.random.seed(83426)
lab = np.array([0])
perfomens = -6 + 10 * np.random.rand(len(data_plot()))
plt.bar(x=data_plot(), y = lab, width=0.70, height=perfomens, align='center', color = 'hotpink' )
plt.title('Slovensko 2021', fontsize = 20, color = 'red')
plt.grid()
plt.show()