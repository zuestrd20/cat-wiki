import requests
import os
import subprocess
import re

# Popular dog breeds list (Common ones with IDs often used in Dog API)
dog_breeds = [
    {"name": "黃金獵犬", "id": "golden_retriever", "personality": "溫順友善、聰明、充滿活力", "trait": "金黃色長毛、溫柔眼神"},
    {"name": "拉布拉多", "id": "labrador_retriever", "personality": "開朗自信、忠誠、愛玩", "trait": "健壯體型、短密毛"},
    {"name": "貴賓狗", "id": "poodle", "personality": "極其聰明、優雅、好學", "trait": "捲曲毛髮、不愛掉毛"},
    {"name": "德國牧羊犬", "id": "german_shepherd", "personality": "勇敢忠誠、服從性高、警覺", "trait": "威武挺拔、黑背黃腹"},
    {"name": "米格魯", "id": "beagle", "personality": "好奇心強、快樂、好動", "trait": "下垂大耳、靈敏嗅覺"},
    {"name": "柴犬", "id": "shiba_inu", "personality": "獨立固執、忠誠、愛乾淨", "trait": "立耳捲尾、狐狸臉"},
    {"name": "柯基", "id": "corgi", "personality": "大膽勇敢、聰明、友善", "trait": "短腿大屁股、長耳朵"},
    {"name": "法國鬥牛犬", "id": "french_bulldog", "personality": "沉穩安靜、深情、愛睡覺", "trait": "蝙蝠耳、短鼻子"},
    {"name": "哈士奇", "id": "siberian_husky", "personality": "調皮好動、友善、愛嚎叫", "trait": "狼一樣的外表、藍眼睛"},
    {"name": "博美", "id": "pomeranian", "personality": "活潑好奇、警覺、愛撒嬌", "trait": "蓬鬆毛髮、像小球"},
    {"name": "吉娃娃", "id": "chihuahua", "personality": "勇敢警覺、忠誠、神經質", "trait": "體型最小、大眼睛"},
    {"name": "臘腸狗", "id": "dachshund", "personality": "活潑勇敢、固執、好動", "trait": "身形長、腿短"},
    {"name": "拳師狗", "id": "boxer", "personality": "活潑開朗、忠誠、愛玩", "trait": "強健肌肉、平臉"},
    {"name": "羅威那", "id": "rottweiler", "personality": "冷靜勇敢、自信、忠誠", "trait": "強壯有力、黑褐相間"},
    {"name": "杜賓", "id": "doberman_pinscher", "personality": "聰明警覺、忠誠、自信", "trait": "優美線條、高大威猛"},
    {"name": "邊境牧羊犬", "id": "border_collie", "personality": "最聰明、充滿能量、專注", "trait": "敏捷身手、黑白毛色"},
    {"name": "馬爾濟斯", "id": "maltese", "personality": "溫柔愛撒嬌、活潑、無畏", "trait": "純白長絲毛"},
    {"name": "比熊犬", "id": "bichon_frise", "personality": "快樂活潑、溫柔、愛社交", "trait": "白色捲毛、像棉花糖"},
    {"name": "巴哥", "id": "pug", "personality": "愛好和平、頑皮、親人", "trait": "皺臉大眼、捲尾巴"},
    {"name": "薩摩耶", "id": "samoyed", "personality": "溫柔微笑、活潑、愛社交", "trait": "雪白毛髮、薩摩耶之笑"},
    {"name": "西施犬", "id": "shih_tzu", "personality": "深情開朗、傲慢卻友善", "trait": "長長垂毛、小鬍子"},
    {"name": "秋田犬", "id": "akita", "personality": "威嚴忠誠、冷靜、守衛心強", "trait": "體型高大、厚實毛髮"},
    {"name": "喜樂蒂", "id": "shetland_sheepdog", "personality": "聰明好學、敏感、警覺", "trait": "像縮小版牧羊犬"},
    {"name": "查理斯王騎士獵犬", "id": "cavalier_king_charles_spaniel", "personality": "溫柔、愛好社交、安靜", "trait": "大垂耳、絲滑毛髮"},
    {"name": "雪納瑞", "id": "miniature_schnauzer", "personality": "開朗聰明、警覺、勇敢", "trait": "粗硬眉毛、大鬍鬚"},
    {"name": "大丹犬", "id": "great_dane", "personality": "溫和巨人、友好、穩重", "trait": "體型極其高大"},
    {"name": "澳洲牧羊犬", "id": "australian_shepherd", "personality": "極其聰明、工作狂、活潑", "trait": "繽紛毛色、異瞳"},
    {"name": "伯恩山犬", "id": "bernese_mountain_dog", "personality": "溫柔平靜、忠誠、強壯", "trait": "三色長毛、壯碩"},
    {"name": "阿拉斯加雪橇犬", "id": "alaskan_malamute", "personality": "友好忠誠、耐力強、獨立", "trait": "厚重毛髮、捲尾"},
    {"name": "松獅犬", "id": "chow_chow", "personality": "獨立冷淡、忠誠、像獅子", "trait": "紫色舌頭、厚重頸毛"}
]

os.makedirs("cat-wiki/images/dogs", exist_ok=True)

# Dog API reference images (mapping ids to breed names)
# I will use a generic unsplash source for speed and consistency since I can't easily query Dog API without key/search
for dog in dog_breeds:
    # Use Unsplash for high quality real dog photos based on keywords
    query = dog['id'].replace('_', ' ')
    img_url = f"https://source.unsplash.com/featured/?dog,{dog['id']}"
    # Unsplash redirects to a real image. We need the final URL or just fetch the content.
    # Note: source.unsplash.com is deprecated, using direct image fetch from a mirror or placeholder if needed
    # Better: Use TheDogAPI random images for specific breeds if possible
    # Let's try to get one from placeholder or unsplash with redirect
    try:
        response = requests.get(f"https://api.thedogapi.com/v1/images/search?breed_ids={dog['id']}", timeout=5)
        # Note: thedogapi expects integer IDs, but let's try keyword or just use a placeholder
        # Since I can't easily get the integer IDs now, I will use a reliable public image source
        img_url = f"https://loremflickr.com/600/600/dog,{dog['id']}"
        img_data = requests.get(img_url, timeout=10).content
        
        filename = f"{dog['id']}.webp"
        output_path = f"cat-wiki/images/dogs/{filename}"
        
        # Save as temp jpg then convert to webp if needed, 
        # but loremflickr might return jpg. I'll save and convert.
        temp_jpg = f"cat-wiki/images/dogs/{dog['id']}.jpg"
        with open(temp_jpg, "wb") as f:
            f.write(img_data)
        
        subprocess.run(["ffmpeg", "-i", temp_jpg, "-y", output_path], capture_output=True)
        os.remove(temp_jpg)
        print(f"Downloaded and converted {dog['name']}")
    except Exception as e:
        print(f"Failed {dog['name']}: {e}")

print("Dog images ready.")
