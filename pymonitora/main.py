import requests
import urllib, urllib.request
#import scrapy

#class QuotesSpider(scrapy.Spider):
#    name = 'QuotesSpider'
#    start_urls = ['http://quotes.toscrape.com/']
#
#    def parse(self, response):
#        quotes = response.xpath('*//div[@class="quote]')
#        for q in quotes:
#            yield {
#                'title':q.xpath('.//span[@class="text"]/text()').get(),
#                'author':q.xpath('.//small[@class="author"]/text()').get(),
#                'tags':q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
#            }

#Testa acesso ao container nginx
try :
    nginx=urllib.request.urlopen('http://192.168.1.72/')
except urllib.request.URLError:
    print ('Nginx server is down\n')
else  :
    responsenginx = requests.get('http://192.168.1.72/')
    print ("Nginx server is up.", "Http code:", responsenginx.status_code,'\n')

#Testa acesso ao container app1
try :
    app1=urllib.request.urlopen('http://192.168.1.72/app1/status')
except urllib.request.URLError:
    print ('App1 is down\n')
else  :
    responseapp1 = requests.get('http://192.168.1.72/app1/status') 
    print ("App1 is up.","Http code:", responseapp1.status_code,'\n')
#    elif responseapp1.status_code==502 :
#        print ("App1 is down, but nginx server is up.","Http code:", responseapp1.status_code,'\n')

#Testa acesso ao container app2
try :
    app2=urllib.request.urlopen('http://192.168.1.72/app2/status')
except urllib.request.URLError:
    print ('App2 is down')
else  :
    responseapp2 = requests.get('http://192.168.1.72/app2/status')
    print ("App2 is up.","Http code:", responseapp2.status_code)
