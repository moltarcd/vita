import pytest
import jsonschema
from src.api.schemas.pet_schema import error_schema
from src.api.models.pet import Pet 

class TestPetNegative:
    """Test cases for failed API operations - ADAPTED TO REAL PETSTORE BEHAVIOR"""
    
    def test_create_pet_invalid_data(self, petstore_client, invalid_pet_data):
        """Test creating a pet with invalid data - PetStore accepts almost anything"""
        # Act
        response = petstore_client.create_pet(invalid_pet_data)
        
        # Assert - PetStore returns 200 even for invalid data
        # This documents the actual (bad) behavior
        assert response.status_code == 200
    
    def test_get_pet_nonexistent_id(self, petstore_client):
        """Test getting a pet with non-existent ID - PetStore behavior is inconsistent"""
        # Arrange - use a very high ID that likely doesn't exist
        non_existent_id = 999999999999999
        
        # Act
        response = petstore_client.get_pet(non_existent_id)
        
        # Assert - PetStore might return 200 with data or 404
        # This test documents the unpredictable behavior
        assert response.status_code in [200, 404]
        
        if response.status_code == 200:
            # If it returns 200, check if it contains error message or actual data
            response_data = response.json()
            # Sometimes it returns actual pet data (if ID was auto-created)
            # Sometimes it returns error message
            pass
    
    def test_update_pet_nonexistent(self, petstore_client, valid_pet_data):
        """Test updating a non-existent pet - PetStore creates it instead of updating"""
        # Arrange
        invalid_data = valid_pet_data.copy()
        invalid_data["id"] = 888888888888888  # Very high non-existent ID
        
        # Act
        response = petstore_client.update_pet(invalid_data)
        
        # Assert - PetStore creates a new pet instead of returning error
        assert response.status_code == 200
    
    def test_delete_pet_nonexistent(self, petstore_client):
        """Test deleting a non-existent pet - PetStore returns 404"""
        # Arrange
        non_existent_id = 777777777777777  # Very high non-existent ID
        
        # Act
        response = petstore_client.delete_pet(non_existent_id)
        
        # Assert - PetStore returns 404 for non-existent pets in DELETE
        assert response.status_code == 404
    
    def test_get_pet_invalid_id_format(self, petstore_client):
        """Test getting a pet with invalid ID format"""
        # Arrange
        invalid_id = "invalid_id_format"
        
        # Act
        response = petstore_client.get_pet(invalid_id)
        
        # Assert - Should return 404 for invalid format
        assert response.status_code == 404
    
    def test_find_pets_invalid_status(self, petstore_client):
        """Test finding pets with invalid status - PetStore returns pets with that status"""
        # Act
        response = petstore_client.find_pets_by_status("invalid_status")
        
        # Assert - Returns 200 with pets that have invalid_status
        # This documents that the API doesn't validate status values
        assert response.status_code == 200
        pets = response.json()
        # The API returns pets that actually have the "invalid_status" value
        # This shows lack of validation
        if pets:  # If there are pets with invalid_status
            for pet in pets:
                assert pet["status"] == "invalid_status"