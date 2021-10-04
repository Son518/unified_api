from dataclasses import dataclass

@dataclass
class DropboxFile:
    file:str=None
    to_location:str=None
    name:str=None
    content:str = None
    path:str=None
    file_extension:str=None
    file_url :str=None