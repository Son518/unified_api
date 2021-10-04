from dataclasses import dataclass


@dataclass
class TwitterTweet():
    message: str = None
    image_url: str = None
    should_shorten_urls: str = None
    gif_url: str = None
    video_url: str = None

