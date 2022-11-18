import requests as rq
import json

#getting url using request method
def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")

#load the data from url
def load_json(data):
    if not data is None:
        j=json.loads(data)
        email = j["data"]["email"]
        return email


def main():
    search = input("Enter the user id:")
    url = "https://reqres.in/api/users/"+ search

    values=load_json(get_data(url))

    if not values is None:
        print("Email:",values)


if __name__=='__main__':
    main()
