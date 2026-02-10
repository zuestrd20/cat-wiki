import os
import subprocess
import re

image_dir = "cat-wiki/images"
html_file = "cat-wiki/index.html"

# Convert all jpg to webp using ffmpeg
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):
        base_name = os.path.splitext(filename)[0]
        input_path = os.path.join(image_dir, filename)
        output_path = os.path.join(image_dir, f"{base_name}.webp")
        
        print(f"Converting {filename} to webp...")
        subprocess.run(["ffmpeg", "-i", input_path, "-y", output_path], capture_output=True)
        
        # Remove the old jpg
        os.remove(input_path)

# Update index.html references
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Change img: "images/xxx.jpg" to img: "images/xxx.webp"
content = re.sub(r'img: "images/(.+?)\.jpg"', r'img: "images/\1.webp"', content)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Conversion and HTML update complete!")
