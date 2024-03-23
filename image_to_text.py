import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxx"}

def generate_semantics(file):
    response = requests.post(API_URL, headers=headers, data=file)
    return response.json()

