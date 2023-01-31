import requests


working_proxies = []


with open("proxies.txt", "r") as f:

    for proxy in f:
        proxy = proxy.strip() 
        try:
            response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy}, timeout=3)
            working_proxies.append(proxy)
            print(f"{proxy} is working")
        except:

            print(f"{proxy} is not working")
            pass
