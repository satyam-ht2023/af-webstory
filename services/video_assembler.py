import os
import requests
import json
from typing import List
from moviepy.editor import ImageClip, CompositeVideoClip, concatenate_videoclips, TextClip
from moviepy.video.fx import all as vfx
from services.data.video_slide import VideoSlide
from services.data.fetch_story_details import *
from PIL import Image, ImageFilter

def download_image(url: str, output_path: str):
    print("downloading to: " + output_path)
    try:
        response = requests.get(url)
        with open(output_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error downloading image {url}: {e}")
        return False
    return True

def apply_transition(clip, transition_type: str):
    if transition_type == 'fadein':
        return vfx.fadein(clip, duration=1)
    elif transition_type == 'fadeout':
        return vfx.fadeout(clip, duration=1)
    else:
        return clip
    """ elif transition_type == 'zoom-in':
        return vfx.zoomin(clip, duration=1)
    elif transition_type == 'zoom-out':
        return vfx.zoomout(clip, duration=1)
    elif transition_type == 'slide-left':
        return vfx.slidein(clip, duration=1, direction='left') """
    

def apply_caption(clip, caption: str, position: str, duration: int, highlight_words: List[str], highlight_colors: List[str]):
    text_clip = TextClip(caption, fontsize=80, color='white', bg_color='black', method="caption", size=(1000,None), font="Arial")
    text_clip = text_clip.set_position(position).set_duration(duration)

    # Highlight words logic (not fully implemented, could add colors to highlighted words)
    #for word, color in zip(highlight_words, highlight_colors):
        # Example logic to highlight words (simplified for demonstration)
    #    text_clip = text_clip.add_mask()  # Placeholder for actual implementation

    return CompositeVideoClip([clip, text_clip])

def create_blurred_background(image_path: str, output_path: str, size=(1080, 1920)):
    """Create a blurred background image from the original image."""
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        img = img.resize(size, Image.Resampling.LANCZOS)  # Resize to video dimensions
        blurred_img = img.filter(ImageFilter.GaussianBlur(20))  # Apply Gaussian blur
        blurred_img.save(output_path)

def create_blurred_background(image_path: str, output_path: str, size=(1080, 1920)):
    """Create a blurred background image from the original image."""
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        img = img.resize(size, Image.Resampling.LANCZOS)  # Resize to video dimensions
        blurred_img = img.filter(ImageFilter.GaussianBlur(20))  # Apply Gaussian blur
        blurred_img.save(output_path)

def create_9_16_clip(image_path: str, duration: int):
    """Create a 9:16 video clip with the image centered and blurred background."""
    VIDEO_WIDTH = 1080
    VIDEO_HEIGHT = 1920

    # Create a blurred background
    blurred_background_path = "blurred_bg.jpg"
    create_blurred_background(image_path, blurred_background_path, size=(VIDEO_WIDTH, VIDEO_HEIGHT))

    # Load the blurred background as a video clip
    background_clip = ImageClip(blurred_background_path).set_duration(duration)

    # Load the original image and resize it to fit the width while maintaining aspect ratio
    image_clip = (
        ImageClip(image_path)
        .resize(width=VIDEO_WIDTH)  # Scale image to half the video height
        .set_duration(duration)
        .set_position("center")
    )

    # Combine the background and the centered image
    final_clip = CompositeVideoClip([background_clip, image_clip])

    # Clean up the temporary blurred background file
    os.remove(blurred_background_path)

    return final_clip



def create_video_from_slides(slides: List[VideoSlide], story_data : StoryData, output_path: str):
    clips = []

    lead_clip = (
        ImageClip("working_dir/lead.jpg")
        .resize(width=1080, height=1920)
        .set_duration(3)
        .set_position("center")
    )

    entry_text = TextClip(story_data.story_title, fontsize=75, color='red', bg_color='white', method="caption", size=(900, None), font='Times-New-Roman-Bold')
    entry_text = entry_text.set_position("center").set_duration(3)

    clips.append(CompositeVideoClip([lead_clip, entry_text]))

    
    for slide in slides:
        image_path = f"{output_path}/temp_{slide.image.split('/')[-1]}"
        download_image(slide.image, image_path)

        # Create ImageClip
        clip = create_9_16_clip(image_path, duration=slide.duration)
        clip = apply_transition(clip, slide.transition_in)
        
        # Apply caption
        clip = apply_caption(clip, slide.caption, slide.caption_position, slide.duration, 
                             slide.highlight_words, slide.highlight_colors)
        
        # Apply rotation
        #clip = clip.rotate(slide.rotation_degree)
        
        # Apply animations if any (for simplicity, this is not fully implemented)
        #if slide.animation:
        #    clip = clip.subclip(slide.animation.start_time, slide.animation.end_time)
        
        # Apply transition out
        clip = apply_transition(clip, slide.transition_out)

        clips.append(clip)
        os.remove(image_path)  
    
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(f"{output_path}/video.mp4", 24, codec="libx264")

def get_key_frames_script(url: str, story_data: StoryData, video_script: List[VideoSlide], output_path: str):
    # Initialize the keyframes list
    key_frames = []

    # Add the first keyframe (the story data)
    key_frames.append({
        "start": 0,
        "end": story_data.lead_ai_image_duration,
        "url": url
    })

    # Calculate timestamps for subsequent video slides
    current_time = story_data.lead_ai_image_duration
    for slide in video_script:
        key_frames.append({
            "start": current_time,
            "end": current_time + slide.duration,
            "url": f"https://www.amazon.in/dp/{slide.product_id}"
        })
        current_time += slide.duration

    # Save the keyframes JSON to the output path
    output_file_path = output_path + "/timestamps.json"
    with open(output_file_path, "w") as output_file:
        json.dump(key_frames, output_file, indent=4)

    print(f"Keyframes script saved to {output_file_path}")