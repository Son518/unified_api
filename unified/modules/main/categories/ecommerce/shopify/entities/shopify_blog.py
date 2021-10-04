from dataclasses import dataclass


@dataclass
class ShopifyBlog:
    blog_id: str = None
    title: str = None
    author_name: str = None
    content: str = None
    featured_image_url: str = None
    summary: str = None
    tags: str = None
