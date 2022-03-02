from requests import get
from urllib import request

BASE_URL = 'https://192.168.79.130/' 

#Testa acesso ao container nginx
try :
    nginx = request.urlopen(BASE_URL)
except request.URLError:
    print('Nginx server is down\n')
else  :
    responsenginx = get(BASE_URL)
    print("Nginx server is up.", "Http code:", responsenginx.status_code,'\n')

#Testa acesso ao container app1
try :
    app1 = request.urlopen(f'{BASE_URL}/app1/status')
except request.URLError:
    print('App1 is down\n')
else  :
    responseapp1 = get(f'{BASE_URL}/app1/status') 
    print("App1 is up.","Http code:", responseapp1.status_code,'\n')
#    elif responseapp1.status_code==502 :
#        print ("App1 is down, but nginx server is up.","Http code:", responseapp1.status_code,'\n')

#Testa acesso ao container app2
try :
    app2 = request.urlopen(f'{BASE_URL}/app2/status')
except request.URLError:
    print('App2 is down')
else  :
    responseapp2 = get(f'{BASE_URL}/app2/status')
    print("App2 is up.","Http code:", responseapp2.status_code)
