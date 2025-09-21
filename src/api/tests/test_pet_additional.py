import pytest
import requests
import jsonschema
from src.api.schemas.pet_schema import pet_schema

class TestPetAdditional:
    """Additional test cases for edge cases and robustness"""
    
    def test_create_pet_empty_photos(self, petstore_client, valid_pet_data):
        """Test creating a pet with empty photoUrls array"""
        # Arrange
        test_data = valid_pet_data.copy()
        test_data["photoUrls"] = []
        
        # Act
        response = petstore_client.create_pet(test_data)
        
        # Assert
        assert response.status_code == 200
        assert response.json()["photoUrls"] == []
        jsonschema.validate(response.json(), pet_schema)
    
    def test_create_pet_empty_tags(self, petstore_client, valid_pet_data):
        """Test creating a pet with empty tags array"""
        # Arrange
        test_data = valid_pet_data.copy()
        test_data["tags"] = []
        
        # Act
        response = petstore_client.create_pet(test_data)
        
        # Assert
        assert response.status_code == 200
        assert response.json()["tags"] == []
        jsonschema.validate(response.json(), pet_schema)
    
    def test_create_pet_no_category(self, petstore_client, valid_pet_data):
        """Test creating a pet without category"""
        # Arrange
        test_data = valid_pet_data.copy()
        test_data.pop("category", None)
        
        # Act
        response = petstore_client.create_pet(test_data)
        
        # Assert
        assert response.status_code == 200
        assert "category" not in response.json() or response.json()["category"] is None
        jsonschema.validate(response.json(), pet_schema)
    
    def test_get_pet_very_large_id(self, petstore_client):
        """Test getting a pet with very large ID"""
        # Arrange
        large_id = 10**18  # Very large number
        
        # Act
        response = petstore_client.get_pet(large_id)
        
        # Assert - should return 404 or handle gracefully
        assert response.status_code in [404, 400]