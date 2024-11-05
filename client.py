import requests

SERVER_URL = "http://server:8080"

def send_get():
    response = requests.get(SERVER_URL)
    print("GET Response:", response.text)

def send_post():
    response = requests.post(SERVER_URL, data={'key': 'value'})
    print("POST Response:", response.text)

def send_head():
    response = requests.head(SERVER_URL)
    print("HEAD Response Headers:", response.headers)

if __name__ == "__main__":
    print("Sending GET request...")
    send_get()
    
    print("\nSending POST request...")
    send_post()
    
    print("\nSending HEAD request...")
    send_head()
