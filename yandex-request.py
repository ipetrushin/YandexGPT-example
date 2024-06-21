import requests
import json


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
IAM_TOKEN = '****'
FOLDER_ID = '****'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IAM_TOKEN}",
    "x-folder-id": FOLDER_ID
}


request = {
  "modelUri": "gpt://****/yandexgpt-lite",
  "completionOptions": {
    "stream": False,
    "temperature": 0.1,
    "maxTokens": "1000"
  },
  "messages": [
    {
      "role": "system",
      "text": "Перескажи заданный текст в смешной форме"
    },
    {
      "role": "user",
      "text": input("Введите свой текст, который переведётся в смешную форму (анекдот):\n")
    }
  ]
}

response = requests.post('https://llm.api.cloud.yandex.net/foundationModels/v1/completion', headers=headers,data=json.dumps(request)).json()
print(response['result']['alternatives'][0]['message']['text'])
