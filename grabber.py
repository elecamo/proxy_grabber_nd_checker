import requests
from bs4 import BeautifulSoup
import re

#change urls to input("") if you wanna add a custom link
urls = ['https://www.socks-proxy.net/', 'http://sslproxies.org', 'http://free-proxy-list.net', 'http://us-proxy.org']


proxies = []


for url in urls:
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', {'class': 'table table-striped table-bordered'})


    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            ip_address = columns[0].text
            port = columns[1].text
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
                proxies.append(f'{ip_address}:{port}')


for proxy in proxies:
    print(proxy)


with open("proxies.txt", "w") as f:
    for proxy in proxies:
        f.write(proxy + "\n")

print("Proxies saved to proxies.txt")
