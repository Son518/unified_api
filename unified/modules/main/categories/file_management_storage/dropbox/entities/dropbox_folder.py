from dataclasses import dataclass


@dataclass
class DropboxFolder:
    name: str = None
    auto_rename: bool = False
