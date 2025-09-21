"""
Test file to document and verify the actual behavior of PetStore API.
"""
import pytest
from src.utils.helpers import safe_json_response

class TestPetStoreBehavior:
    """Tests to document the actual behavior of PetStore API"""
    
    def test_api_behavior_documentation(self, petstore_client):
        """Document the actual behavior of PetStore API for test adaptation"""
        print("\n" + "="*50)
        print("PetStore API Behavior Documentation")
        print("="*50)
        
        # Test 1: Create pet with invalid data
        print("\n1. Creating pet with invalid data...")
        from src.api.models.pet import Pet
        invalid_pet = Pet.create_invalid_pet().to_dict()
        response = petstore_client.create_pet(invalid_pet)
        response_data = safe_json_response(response)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response_data}")
        
        # Test 2: Get non-existent pet
        print("\n2. Getting non-existent pet...")
        response = petstore_client.get_pet(999999999999)
        response_data = safe_json_response(response)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response_data}")
        
        # Test 3: Delete non-existent pet
        print("\n3. Deleting non-existent pet...")
        response = petstore_client.delete_pet(999999999999)
        response_data = safe_json_response(response)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response_data}")
        
        # Test 4: Find by invalid status
        print("\n4. Finding pets with invalid status...")
        response = petstore_client.find_pets_by_status("invalid_status_123")
        response_data = safe_json_response(response)
        print(f"   Status: {response.status_code}")
        if isinstance(response_data, list):
            print(f"   Found {len(response_data)} pets")
            if response_data:
                print(f"   First pet: {response_data[0]}")
        else:
            print(f"   Response: {response_data}")
        
        # Test 5: Create and delete valid pet
        print("\n5. Creating and deleting valid pet...")
        valid_pet = Pet.create_valid_pet().to_dict()
        create_response = petstore_client.create_pet(valid_pet)
        create_data = safe_json_response(create_response)
        print(f"   Create Status: {create_response.status_code}")
        
        if create_response.status_code == 200 and 'id' in create_data:
            pet_id = create_data['id']
            print(f"   Created pet ID: {pet_id}")
            
            # Delete the pet
            delete_response = petstore_client.delete_pet(pet_id)
            delete_data = safe_json_response(delete_response)
            print(f"   Delete Status: {delete_response.status_code}")
            print(f"   Delete Response: {delete_data}")
        
        print("\n" + "="*50)
        print("Documentation completed")
        print("="*50)
        
        # This test is for documentation, should always pass
        assert True