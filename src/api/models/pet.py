from dataclasses import dataclass, field
from typing import List, Optional
from faker import Faker

fake = Faker()

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Tag:
    id: int
    name: str

@dataclass
class Pet:
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str = ""
    photoUrls: List[str] = field(default_factory=list)
    tags: List[Tag] = field(default_factory=list)
    status: str = "available"  # available, pending, sold
    
    @classmethod
    def create_valid_pet(cls):
        """Create a valid pet """
        return cls(
            id=fake.random_int(min=1, max=999999),
            category=Category(id=1, name="dogs"),
            name=fake.first_name(),
            photoUrls=[fake.image_url()],
            tags=[Tag(id=1, name="tag1")],
            status="available"
        )
    
    @classmethod
    def create_invalid_pet(cls):
        """Create an invalid pet """
        return cls(
            id=fake.random_int(min=1, max=999999),
            name="",  # Empty name - should cause error
            status="invalid_status"  # Invalid status
        )
    
    def to_dict(self):
        """dictionary for API requests"""
        return {
            "id": self.id,
            "category": {
                "id": self.category.id if self.category else None,
                "name": self.category.name if self.category else None
            } if self.category else None,
            "name": self.name,
            "photoUrls": self.photoUrls,
            "tags": [{"id": tag.id, "name": tag.name} for tag in self.tags],
            "status": self.status
        }