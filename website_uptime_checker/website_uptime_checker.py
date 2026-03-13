import requests

print("Website Uptime checker")

url = input("Enter website URL (e.g., https://google.com): ")

try:
    response = requests.get(url,timeout=5)

    if response.status_code == 200:
        print(f"{url} is UP ✅")
    else:
         print(f"{url} returned status code {response.status_code}")

except requests.exceptions.RequestException:
    print("f{url}is DOWN ❌")


