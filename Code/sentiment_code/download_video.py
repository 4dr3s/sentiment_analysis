import yt_dlp
import pandas as pd
import json
file_path = "C:/Users/andre/Downloads/datos_tiktok_threads_instagram_twitter.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.json_normalize(data)

for i, item in df.iterrows():
    try:
        if item['fuente'] == 'Tik Tok':
            if 36 <= item['id'] <= 100:
                ydl_opts = {
                    'format': 'mp4',
                    'outtmpl': f"C:/Universidad/Legislacion/videos/{item['id']}.mp4",
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([f"{item['post_link']}"])
    except Exception as ex:
        print(ex)
        continue
