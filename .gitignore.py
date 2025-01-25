!pip install icrawler

import os
import random
from IPython.display import Image, display
from icrawler.builtin import BingImageCrawler

save_dir = "japanese_women_images" 
keyword = "日本人　女性"  

crawler = BingImageCrawler(storage={"root_dir": save_dir})
filters = dict(size="large")
crawler.crawl(keyword=keyword, max_num=100 ,filters=filters)  

image_dir = "/content/japanese_women_images"

if os.path.exists(image_dir):
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if image_files:
        random_image = random.choice(image_files)
        print(f"ランダムに選ばれた画像: {random_image}")
    else:
        print("画像ファイルが見つかりませんでした。")
else:
    print(f"指定されたディレクトリが存在しません: {image_dir}")

if random_image:
    display(Image(filename=os.path.join(image_dir, random_image)))
