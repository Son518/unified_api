from dataclasses import dataclass


@dataclass
class AuthInfo:
    client_id: str
    client_secret: str
    token: str
    refresh_url: str
    api_key:str
    domain:str

    def as_dict(self):
        return self.__dict__


@dataclass
# its __repr__ makes it easy for unit-testing
class App:
    """
    Base class for all the Apps. 
    All common properties and method to be here.
    """
    name: str
    description: str
    category: str
    logo: str
    auth_type: str
    auth_info: AuthInfo

    def as_dict(self):
        return self.__dict__

    def __getattr__(self, name):
        def not_implemented(self, *args, **kwargs):
            raise NotImplementedError(f"Method '{name}' is not defined")

        return not_implemented
