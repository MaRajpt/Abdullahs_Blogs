import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
#  "https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean"  request line is before ?

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']


