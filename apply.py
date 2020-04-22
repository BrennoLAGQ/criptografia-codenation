import requests
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=6bc4d8acd865d38e9629061667e72965feb8f14d'
answer = {'answer': open('answer.json', "rb")}
r = requests.post(url, files=answer)
r.text
