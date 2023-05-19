# An app that makes requests to an http end point
# Libhongo Mko

import requests

def main():
    endpoint_url = "https://api.github.com/users/bard" # endpoint url
    response = requests.get(endpoint_url) # send request
    print("Status Code:", response.status_code)

    for header in response.headers: # iterating through the response headers and printing them out
        print("Header:", header,":",response.headers[header])
    
    print("Body:",response.content)

if __name__ == "__main__":
    main()