import requests

url = "https://webexapis.com/v1/messages"

payload = "{\n  \"toPersonEmail\":\"sekregie@cisco.com\",\n  \"text\": \"Bonjour from Python3! :)\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ZDM4NjZhYjItMDA4ZC00MjU3LWJiY2EtMjY5NzUyMGYxNDI1MDliNmM4ODQtY2Vi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
