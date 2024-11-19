import json
import openai
from typing import List
from services.data.fetch_story_details import *
from services.data.video_slide import *


class VideoScript:
    def __init__(self):
        self.max_retries = 3
        self.prompt_template = self.load_prompt()

    def load_prompt(self):
        with open("assets/ai_prompt.txt", "r") as file:
            return file.read()

    def validate_video_slide(self, slide_data: dict) -> bool:
        """ required_fields = [
            "id","duration", "caption", "highlight_words",
            "highlight_colors", "caption_position", "rotation_degree",
            "transition_in", "transition_out", "animation"
        ] """

        required_fields = [key for key, value_type in VideoSlide.__annotations__.items() if key != "image"]

        for field in required_fields:
            if field not in slide_data:
                print(f"Missing field: {field}")
                return False
        
        if "animation" in slide_data:
            animation = slide_data["animation"]
            if not all(key in animation for key in [anim_key for anim_key, anim_key_type in Animation.__annotations__.items()]):
                print("Invalid animation structure.")
                return False
        
        return True

    def validate_response(self, response_data: list) -> bool:
        if not isinstance(response_data, list):
            print("Response is not a list.")
            return False

        for slide_data in response_data:
            if not self.validate_video_slide(slide_data):
                return False

        return True
    
    def get_video_slide_class_template(self):
        fields = VideoSlide.__annotations__.items()
        
        template = "{"

        for field, field_type in fields:
            if field == "image":
                continue
            elif field == "animation":
                template += "animation: {"
                anim_fields = Animation.__annotations__.items()
                for anim_field, anim_field_type in anim_fields:
                    template += f"{anim_field}:{anim_field_type.__name__}"
                    template += ", "
                template += "]"
            else:
                template += f"{field}:{field_type.__name__}"
            template += ","
        template += "}"

        return template

    def generate_script(self, data: Product) -> List[VideoSlide]:
        prompt = f"{self.prompt_template}\nStory Details: {json.dumps(data.for_gpt(), indent=2)}\nVideo Slide (output) format: {self.get_video_slide_class_template()}"     
        
        for attempt in range(self.max_retries):
            try:
                """ response = openai.ChatCompletion.create(
                    model="gpt-3.5",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000 
                )

                response_text = response["choices"][0]["message"]["content"] """

                response_data = {} #json.loads(response_text)
                with open('assets/test_response.json', 'r') as file:
                    response_data = json.load(file)

                if self.validate_response(response_data):
                    video_slides = [
                        VideoSlide(**slide_data) for slide_data in response_data
                    ]
                    return video_slides
                else:
                    print(f"Attempt {attempt + 1}: Invalid response structure, retrying...")

            except json.JSONDecodeError:
                print(f"Attempt {attempt + 1}: Invalid JSON response, retrying...")
            except Exception as e:
                print(f"Attempt {attempt + 1}: Unexpected error: {e}")

        raise ValueError("Failed to generate valid VideoSlide array from ChatGPT response.")
