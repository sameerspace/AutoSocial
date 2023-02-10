import requests

filename = ""


req = {
    'caption': "Picture of Emma",
    'files': open("emma.jpg", "wb").read(),
}

response = requests.post("http://127.0.0.1:8000/post_instag", data=req)
print(response.text)
