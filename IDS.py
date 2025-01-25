import os
import random
from IPython.display import display, Image
from icrawler.builtin import BingImageCrawler

user_input_file = input("保存したいフォルダ名を記入してください ： ").strip().lower()
save_dir = user_input_file

user_input_prompt = input("検索したいプロンプトを入力してください ： ").strip().lower()
keyword = user_input_prompt  

crawler = BingImageCrawler(storage={"root_dir": save_dir})
filters = dict(size="large")
crawler.crawl(keyword=keyword, max_num=100 ,filters=filters)  

image_dir = save_dir

while True:
    user_input = input("画像を確認しますか？ (y: 確認する, z: 終了): ").strip().lower()
    if user_input == 'y':
        show_random_image(image_dir)
    elif user_input == 'z':
        print("プログラムを終了します。")
        break
    else:
        print("無効な入力です。'y' または 'z' を入力してください。")
