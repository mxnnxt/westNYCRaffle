import requests
import time
from bs4 import BeautifulSoup as bs
import random
from random import getrandbits
import json
import names

session = requests.session()

times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of accounts you would like: ")))
domain = input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter your domain (ex: domain.com): "))


print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ----------------------------------------------")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "                WEST NYC       ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + "           Developed by @mxnnxt            ")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ----------------------------------------------\n")

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://manage.kmail-lists.com',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://manage.kmail-lists.com/subscriptions/subscribe?a=Qmfm7G&g=Q468Mg',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}


def submit():
	global session
	name = names.get_first_name()
	last_name = names.get_last_name()
	email = (name + "{}" + "@"+domain).format(getrandbits(40))
	sizes = ["7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","14","15"]
	size = sizes[random.randint(0, 14)]

	print("[" + (time.strftime("%H:%M:%S")) + "]" + " - Collecting CSRF TOKEN ")

	raffle_url = 'https://manage.kmail-lists.com/subscriptions/subscribe?a=Qmfm7G&g=Q468Mg'
	res1 = requests.get(raffle_url,headers=headers)
	soup1 = bs(res1.text,"html.parser")
	csrf = soup1.find_all("input",{"name":"csrfmiddlewaretoken"})
	csrf_id = csrf[0]["value"]
	#print(csrf_id)

	print("[" + (time.strftime("%H:%M:%S")) + "]" + " - TOKEN COLLECTED - "+csrf_id)


	data = {
 	'csrfmiddlewaretoken': csrf_id,
  	'k8789a8e588f36bf522d0f24a53805327': email,
  	'k169d59f89d4d6519617a660b32b6695a':name,
  	'k9c364e249686c0c90a6558c31862ef21': last_name,
  	'k411af701ac56c3593160da27cb153048': size,
	}

	res2 = session.post(raffle_url,headers=headers,data=data)
	#print(res2.text)

	if ('"Confirm Your Email"' in res2.text):
		print("[" + (time.strftime("%H:%M:%S")) + "]" + " - SUCCESSFULLY SUBMITTED - "+email)

for i in range(times):
	submit()