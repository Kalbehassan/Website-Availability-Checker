import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ The website {url} is UP!")
        else:
            print(f"⚠️ The website {url} might be DOWN! Status Code: {response.status_code}")
    except requests.ConnectionError:
        print(f"❌ Failed to connect to {url}. The website is DOWN.")
    except requests.Timeout:
        print(f"⌛ Timeout! {url} took too long to respond.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    website = input("Enter the website URL (include http:// or https://): ")
    check_website(website)
