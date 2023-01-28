import requests
from urllib3.exceptions import MaxRetryError

url = "https://eapcet-sche.aptonline.in/EAPCET/eapAllotment.xls"
data = {'hallticket':'90261030113', 'dob':'27/08/2004'}
print(requests)
try:
    x = requests.post(url, data)
    print(x.text)
except MaxRetryError:
    print("Error Fucks")
except requests.exceptions.SSLError:
    print("SSLError sucks")

