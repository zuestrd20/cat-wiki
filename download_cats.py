import os
import requests
import json
import re

# Cat breed data with IDs from previous logic
cats = [
    {"name": "Abyssinian", "id": "abys", "zh": "阿比西尼亞貓"},
    {"name": "Aegean", "id": "aege", "zh": "愛琴貓"},
    {"name": "American Bobtail", "id": "abob", "zh": "美國短尾貓"},
    {"name": "American Curl", "id": "acur", "zh": "美國捲耳貓"},
    {"name": "American Shorthair", "id": "asho", "zh": "美國短毛貓"},
    {"name": "American Wirehair", "id": "awir", "zh": "美國硬毛貓"},
    {"name": "Arabian Mau", "id": "amau", "zh": "阿拉伯貓"},
    {"name": "Australian Mist", "id": "amis", "zh": "澳洲霧貓"},
    {"name": "Balinese", "id": "bali", "zh": "巴里貓"},
    {"name": "Bambino", "id": "bamb", "zh": "斑比諾貓"},
    {"name": "Bengal", "id": "beng", "zh": "孟加拉貓"},
    {"name": "Birman", "id": "birm", "zh": "伯曼貓"},
    {"name": "Bombay", "id": "bomb", "zh": "孟買貓"},
    {"name": "British Longhair", "id": "bslo", "zh": "英國長毛貓"},
    {"name": "British Shorthair", "id": "bsho", "zh": "英國短毛貓"},
    {"name": "Burmese", "id": "bure", "zh": "緬甸貓"},
    {"name": "Burmilla", "id": "buri", "zh": "波米拉貓"},
    {"name": "California Spangled", "id": "cspa", "zh": "加州閃亮貓"},
    {"name": "Chantilly-Tiffany", "id": "ctif", "zh": "蒂芬妮貓"},
    {"name": "Chartreux", "id": "char", "zh": "沙特爾貓"},
    {"name": "Chausie", "id": "chau", "zh": "喬西貓"},
    {"name": "Cheetoh", "id": "chee", "zh": "切托貓"},
    {"name": "Colorpoint Shorthair", "id": "csho", "zh": "彩色點短毛貓"},
    {"name": "Cornish Rex", "id": "crex", "zh": "柯尼斯捲毛貓"},
    {"name": "Cymric", "id": "cymr", "zh": "威爾斯貓"},
    {"name": "Cyprus", "id": "cypr", "zh": "賽普勒斯貓"},
    {"name": "Devon Rex", "id": "drex", "zh": "德文捲毛貓"},
    {"name": "Donskoy", "id": "dons", "zh": "頓斯科伊貓"},
    {"name": "Dragon Li", "id": "lihu", "zh": "狸花貓"},
    {"name": "Egyptian Mau", "id": "emau", "zh": "埃及貓"}
]

os.makedirs("cat-wiki/images", exist_ok=True)

# Fetch breed details to get reference image IDs
response = requests.get("https://api.thecatapi.com/v1/breeds")
breeds_data = response.json()
breed_to_image = {b['id']: b.get('reference_image_id') for b in breeds_data}

mapping = {}

for cat in cats:
    img_id = breed_to_image.get(cat['id'])
    if img_id:
        img_url = f"https://cdn2.thecatapi.com/images/{img_id}.jpg"
        try:
            img_data = requests.get(img_url).content
            filename = f"{cat['id']}.jpg"
            with open(f"cat-wiki/images/{filename}", "wb") as f:
                with open(f"cat-wiki/images/{filename}", "wb") as f:
                    f.write(img_data)
            mapping[cat['zh']] = f"images/{filename}"
            print(f"Downloaded {cat['zh']}")
        except:
            print(f"Failed {cat['zh']}")

# Update index.html
with open("cat-wiki/index.html", "r", encoding="utf-8") as f:
    content = f.read()

for zh_name, local_path in mapping.items():
    # Replace the specific URL for each cat
    pattern = rf'name: "{zh_name}", img: "[^"]+"'
    replacement = f'name: "{zh_name}", img: "{local_path}"'
    content = re.sub(pattern, replacement, content)

with open("cat-wiki/index.html", "w", encoding="utf-8") as f:
    f.write(content)
