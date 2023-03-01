import requests

def client():
    token_h = "Token fe218ee3a0651b5e6ac8719ffe07ee15711f18ba"
    credentials = {"username":"admin", "password":"1111"}

    #token_h = "Token 9a51adfe45803ea88de8b2e5f31c9ad3978220c6"
    #credentials = {"username":"test2", "password":"changeme123"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                            data=credentials)

    headers = {"Authorization": token_h}

    #response = requests.get("http://127.0.0.1:8000/api/users/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()