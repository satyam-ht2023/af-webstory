'''
ok lets code step by step, please structure the code very well, create classes/services if needed
step 3: assemble 
step 4: convert to clickable iframes based on timeframes using links script json
step 5: upload html and video to s3 in folder with unique uuid 
'''
from flask import Flask, request, jsonify
from moviepy.config import change_settings
from urllib.parse import urlparse
import uuid
import os
from services.data.fetch_story_details import *
from services.data.video_slide import *
from services.ai.video_script import *
from services.video_assembler import *


change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


app = Flask(__name__)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@app.route('/get_iframe_url', methods=['GET'])
def get_url():
    story_url = request.args.get('storyURL')
    if story_url and is_valid_url(story_url):
        process()
        return "tested"
    else:
        return jsonify({"error": "Invalid URL"}), 400

def process(url: str):
    project_id = f"webstory_{uuid.uuid4()}"
    project_id = "webstory_55a5d416-96a5-493d-9afc-da256b58e363"
    output_path = f"working_dir/{project_id}"
    if not os.path.exists("working_dir"):
        os.makedirs("working_dir")

    if not os.path.exists(f"working_dir/{project_id}"):
        os.makedirs(f"working_dir/{project_id}")
    
    print("Project: " + project_id)
    story_data : StoryData = DataProvider(url).get_data()
    video_script : VideoSlide = VideoScript().generate_script(story_data)
    #video_script = fetch_images_from_products(video_script, story_data.products)
    #create_video_from_slides(video_script, story_data, output_path")
    get_key_frames_script(url, story_data, video_script, output_path)
    

if __name__ == '__main__':
    process("https://www.hindustantimes.com/technology/exclusive-offers-on-best-water-purifiers-from-top-brands-like-aquaguard-kent-pureit-livpure-up-to-75-off-101725513316959.html")



