import time
from bs4 import BeautifulSoup
import requests

import re



t = time.time()



fasfd = time.strftime('???? link in time or ~~~', time.localtime(t))
##or
fasfd =('link')




res = requests.get(fasfd, headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
})

soup = BeautifulSoup(res.text, 'html.parser')
meal = soup.find('?????','?????')



print (meal)
