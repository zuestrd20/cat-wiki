import requests
import os
import subprocess

# Popular rabbit breeds list
rabbit_breeds = [
    {"name": "荷蘭侏儒兔", "id": "netherland_dwarf", "personality": "活潑好奇、體型嬌小", "trait": "圓滾滾的身材、短耳朵"},
    {"name": "垂耳兔", "id": "holland_lop", "personality": "溫順友善、愛撒嬌", "trait": "下垂的大耳朵、可愛包子臉"},
    {"name": "獅子兔", "id": "lionhead", "personality": "聰明好學、膽小謹慎", "trait": "頸部有長毛、像小獅子"},
    {"name": "安哥拉兔", "id": "english_angora", "personality": "安靜溫和、懶洋洋", "trait": "全身長滿絲滑長毛"},
    {"name": "雷克斯兔", "id": "rex_rabbit", "personality": "聰明活潑、很有活力", "trait": "天鵝絨般的短毛"},
    {"name": "紐西蘭兔", "id": "new_zealand_rabbit", "personality": "溫和穩定、容易相處", "trait": "體型較大、純白毛色"},
    {"name": "佛萊明巨兔", "id": "flemish_giant", "personality": "溫和的巨人、冷靜", "trait": "體型極大、耳朵長"},
    {"name": "喜馬拉雅兔", "id": "himalayan_rabbit", "personality": "脾氣極好、耐性強", "trait": "身體白色、耳朵鼻子是深色"},
    {"name": "荷蘭兔", "id": "dutch_rabbit", "personality": "友善聰明、愛運動", "trait": "臉部有白色V型花紋"},
    {"name": "侏儒海棠兔", "id": "dwarf_hotot", "personality": "頑皮愛玩、活泼", "trait": "眼睛周圍有黑色眼圈"},
    {"name": "英國垂耳兔", "id": "english_lop", "personality": "溫順、喜歡安靜", "trait": "耳朵極長、觸地"},
    {"name": "澤西羊毛兔", "id": "jersey_wooly", "personality": "溫柔安靜、容易照顧", "trait": "小臉長毛、像玩偶"},
    {"name": "侏儒垂耳兔", "id": "mini_lop", "personality": "非常愛玩、親人", "trait": "圓頭圓腦、垂耳"},
    {"name": "阿金特兔", "id": "argente_rabbit", "personality": "大膽活潑、好奇心強", "trait": "銀灰色的毛色"},
    {"name": "比利時野兔", "id": "belgian_hare", "personality": "極其活潑、神經質", "trait": "身形修長、像野兔"},
    {"name": "迷你雷克斯兔", "id": "mini_rex", "personality": "友善好動、愛乾淨", "trait": "質感極佳的捲曲短毛"},
    {"name": "波蘭兔", "id": "polish_rabbit", "personality": "聰明、警戒心強", "trait": "身形精瘦、立耳"},
    {"name": "銀貂兔", "id": "silver_marten", "personality": "獨立冷靜、忠誠", "trait": "深色底毛配銀白色尖端"},
    {"name": "蘇門答臘兔", "id": "sumatran_rabbit", "personality": "害羞、神祕", "trait": "獨特的條紋花紋"},
    {"name": "加利福尼亞兔", "id": "californian_rabbit", "personality": "溫和、穩定", "trait": "黑耳黑鼻的白兔"},
    {"name": "金吉拉兔", "id": "chinchilla_rabbit", "personality": "聰明、愛撒嬌", "trait": "像龍貓一樣的灰毛"},
    {"name": "維也納兔", "id": "vienna_rabbit", "personality": "活潑、友善", "trait": "通常有藍色眼睛"},
    {"name": "哈瓦那兔", "id": "havana_rabbit", "personality": "安靜、溫順", "trait": "深巧克力色皮毛"},
    {"name": "大丹兔", "id": "checkered_giant", "personality": "好動、需要空間", "trait": "白底配黑色斑點"},
    {"name": "薩蘭德兔", "id": "sallander_rabbit", "personality": "溫和、容易親近", "trait": "獨特的煙燻色調"},
    {"name": "阿拉斯加兔", "id": "alaska_rabbit", "personality": "活潑、警覺", "trait": "全身純黑、發亮"},
    {"name": "英國點兔", "id": "english_spot", "personality": "充滿活力、愛跳躍", "trait": "背部有條紋、側面有點點"},
    {"name": "美洲兔", "id": "american_rabbit", "personality": "溫順、穩定", "trait": "曼陀林身形"},
    {"name": "小狐兔", "id": "mini_fox", "personality": "調皮、愛動", "trait": "毛髮質地特殊"},
    {"name": "緞毛兔", "id": "satin_rabbit", "personality": "溫柔、安靜", "trait": "毛髮有強烈光澤"}
]

os.makedirs("cat-wiki/images/rabbits", exist_ok=True)

for rabbit in rabbit_breeds:
    try:
        # Use a reliable public image source for rabbits
        img_url = f"https://loremflickr.com/600/600/rabbit,{rabbit['id']}"
        img_data = requests.get(img_url, timeout=10).content
        
        filename = f"{rabbit['id']}.webp"
        output_path = f"cat-wiki/images/rabbits/{filename}"
        temp_jpg = f"cat-wiki/images/rabbits/{rabbit['id']}.jpg"
        
        with open(temp_jpg, "wb") as f:
            f.write(img_data)
        
        subprocess.run(["ffmpeg", "-i", temp_jpg, "-y", output_path], capture_output=True)
        os.remove(temp_jpg)
        print(f"Downloaded and converted {rabbit['name']}")
    except Exception as e:
        print(f"Failed {rabbit['name']}: {e}")

print("Rabbit images ready.")
