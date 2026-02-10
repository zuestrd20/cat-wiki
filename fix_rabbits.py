import requests
import os
import subprocess
import time

# Popular rabbit breeds list (same as before)
rabbit_breeds = [
    {"name": "荷蘭侏儒兔", "id": "netherland_dwarf"},
    {"name": "垂耳兔", "id": "holland_lop"},
    {"name": "獅子兔", "id": "lionhead"},
    {"name": "安哥拉兔", "id": "english_angora"},
    {"name": "雷克斯兔", "id": "rex_rabbit"},
    {"name": "紐西蘭兔", "id": "new_zealand_rabbit"},
    {"name": "佛萊明巨兔", "id": "flemish_giant"},
    {"name": "喜馬拉雅兔", "id": "himalayan_rabbit"},
    {"name": "荷蘭兔", "id": "dutch_rabbit"},
    {"name": "侏儒海棠兔", "id": "dwarf_hotot"},
    {"name": "英國垂耳兔", "id": "english_lop"},
    {"name": "澤西羊毛兔", "id": "jersey_wooly"},
    {"name": "侏儒垂耳兔", "id": "mini_lop"},
    {"name": "阿金特兔", "id": "argente_rabbit"},
    {"name": "比利時野兔", "id": "belgian_hare"},
    {"name": "迷你雷克斯兔", "id": "mini_rex"},
    {"name": "波蘭兔", "id": "polish_rabbit"},
    {"name": "銀貂兔", "id": "silver_marten"},
    {"name": "蘇門答臘兔", "id": "sumatran_rabbit"},
    {"name": "加利福尼亞兔", "id": "californian_rabbit"},
    {"name": "金吉拉兔", "id": "chinchilla_rabbit"},
    {"name": "維也納兔", "id": "vienna_rabbit"},
    {"name": "哈瓦那兔", "id": "havana_rabbit"},
    {"name": "大丹兔", "id": "checkered_giant"},
    {"name": "薩蘭德兔", "id": "sallander_rabbit"},
    {"name": "阿拉斯加兔", "id": "alaska_rabbit"},
    {"name": "英國點兔", "id": "english_spot"},
    {"name": "美洲兔", "id": "american_rabbit"},
    {"name": "小狐兔", "id": "mini_fox"},
    {"name": "緞毛兔", "id": "satin_rabbit"}
]

os.makedirs("cat-wiki/images/rabbits", exist_ok=True)

# Using a combination of sources and random locks to ensure variety
for i, rabbit in enumerate(rabbit_breeds):
    try:
        # Varying the source and adding a lock to force different images
        # Source 1: Unsplash (via source.unsplash.com legacy fallback or just placeholder)
        # Source 2: LoremFlickr with specific lock
        img_url = f"https://loremflickr.com/600/600/rabbit,bunny?lock={i+100}"
        
        print(f"Downloading unique image for {rabbit['name']} (lock={i+100})...")
        img_data = requests.get(img_url, timeout=15).content
        
        filename = f"{rabbit['id']}.webp"
        output_path = f"cat-wiki/images/rabbits/{filename}"
        temp_jpg = f"cat-wiki/images/rabbits/{rabbit['id']}.jpg"
        
        with open(temp_jpg, "wb") as f:
            f.write(img_data)
        
        subprocess.run(["ffmpeg", "-i", temp_jpg, "-y", output_path], capture_output=True)
        os.remove(temp_jpg)
        time.sleep(0.5) # Slight delay to be nice to the server
    except Exception as e:
        print(f"Failed {rabbit['name']}: {e}")

print("Unique rabbit images ready.")
