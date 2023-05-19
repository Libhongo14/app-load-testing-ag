import requests

def main():
    endpoint_url = "https://api.github.com/users/bard"
    response = requests.get(endpoint_url)
    print("Status Code:", response.status_code)

    for header in response.headers:
        print("Header:", header,":",response.headers[header])
    
    print("Body:",response.content)

if __name__ == "__main__":
    main()