import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and 'url' in data[0]:
            return data[0]['url']
        elif data and 'url' not in data[0] and 'image' in data[0]:
            return data[0]['image']
        return data[0].get('url')
    else:
        return None
