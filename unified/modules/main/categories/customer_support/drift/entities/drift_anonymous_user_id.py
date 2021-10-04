from dataclasses import dataclass

@dataclass
class DriftAnonymousUserId():
    
    email: str = None
    availability: str = None
    bot: bool = True
    name: str = None
    verified: bool = False
    alias: str = None
    avatarUrl: str = None 
    orgId: str = None
    role: str = None 
    createdAt: str = None