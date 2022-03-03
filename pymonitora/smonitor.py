import csv
from time import time
import requests
requests.packages.urllib3.disable_warnings()

BASE_URL = "http://192.168.79.130/" 
csvfile = open('./monitor.csv', 'a', newline='')
writer = csv.writer(csvfile)

def app_monitor(app_name, url):
    try:
        start = time()
        app = requests.get(url, verify=False, timeout=2)
    except requests.exceptions.Timeout as error:
        status = 'DOWN'
        stop = time()
        writer.writerow([start, app_name, status, stop-start, time()])
    else:
        status = 'DOWN'
        if app.status_code == 200:
            status = 'UP'
        #Ordem de leitura: DATA_REGISTRO, APLICAÇÃO, STATUS, LATÊNCIA, DATA_COLETA
        writer.writerow([start, app_name, status, app.elapsed.total_seconds(), time()]) 

#Testa acesso ao container app1
app_monitor('app1', f'{BASE_URL}/app1/status')

#Testa acesso ao container app2
app_monitor('app2', f'{BASE_URL}/app2/status')

#Testa acesso ao container nginx
app_monitor('nginx', BASE_URL)

csvfile.close()