from typing import List, Dict, Optional
from services.data.fetch_story_details import Product

class Animation:
    animation_type: str
    start_time: float
    end_time: float

    def __init__(self, animation_type: str, start_time: float, end_time: float):
        self.animation_type = animation_type
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "type": self.animation_type,
            "start_time": self.start_time,
            "end_time": self.end_time
        }


class VideoSlide:
    product_id: str
    image: str
    duration: int
    caption: str
    highlight_words: list[str]
    highlight_colors: list[str]
    caption_position: str
    rotation_degree: int
    transition_in: str
    transition_out: str
    animation: dict

    def __init__(
        self,
        product_id: str,
        duration: int,
        caption: str,
        highlight_words: List[str],
        highlight_colors: List[str],
        caption_position: str,
        rotation_degree: int,
        transition_in: str,
        transition_out: str,
        image: Optional[str] = None,
        animation: Optional[Dict[str, any]] = None,
    ):
        self.product_id = product_id
        self.image = image
        self.duration = duration
        self.caption = caption
        self.highlight_words = highlight_words
        self.highlight_colors = highlight_colors
        self.caption_position = caption_position
        self.rotation_degree = rotation_degree
        self.transition_in = transition_in
        self.transition_out = transition_out
        self.animation = Animation(**animation) if animation else None

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "image": self.image,
            "duration": self.duration,
            "caption": self.caption,
            "highlight_words": self.highlight_words,
            "highlight_colors": self.highlight_colors,
            "caption_position": self.caption_position,
            "rotation_degree": self.rotation_degree,
            "transition_in": self.transition_in,
            "transition_out": self.transition_out,
            "animation": self.animation.to_dict() if self.animation else None
        }
    
def fetch_images_from_products(video_slides: List[VideoSlide], products: List[Product]) -> List[VideoSlide]:
    for video_slide in video_slides:
        if not video_slide.image:
            matching_product = next((product for product in products if product.id == video_slide.product_id), None)
            if matching_product and matching_product.productFrontImage:
                video_slide.image = matching_product.productFrontImage
    
    return video_slides
