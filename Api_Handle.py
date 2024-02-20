import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()

    if (data["success"] and "data" in data):
        user = data["data"]
        print(user["login"]["username"])
    else:
      raise Exception("Error while fetching Data")


def main():
    fetch_random_user_freeapi()

if __name__ == "__main__":
    main()
     