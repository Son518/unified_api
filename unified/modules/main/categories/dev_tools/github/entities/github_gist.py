from dataclasses import dataclass


@dataclass
class GithubGist():
    gist_filename: str = None
    content_of_the_gist: str = None
    description: str = None
    make_gist_public: str = None