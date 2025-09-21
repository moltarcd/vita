import requests
import json
from src.utils.logger import setup_logger
from src.utils.config import Config

logger = setup_logger(__name__)

class PetStoreClient:
    """HTTP client for PetStore API"""
    
    def __init__(self):
        self.base_url = Config.PETSTORE_BASE_URL
        self.timeout = Config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _request(self, method, endpoint, **kwargs):
        """Generic request method"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            logger.info(f"{method.upper()} {url} - Status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    def create_pet(self, pet_data):
        """Create a new pet (POST /pet)"""
        return self._request('POST', '/pet', json=pet_data)
    
    def get_pet(self, pet_id):
        """Get pet by ID (GET /pet/{petId})"""
        return self._request('GET', f'/pet/{pet_id}')
    
    def update_pet(self, pet_data):
        """Update an existing pet (PUT /pet)"""
        return self._request('PUT', '/pet', json=pet_data)
    
    def delete_pet(self, pet_id):
        """Delete a pet (DELETE /pet/{petId})"""
        return self._request('DELETE', f'/pet/{pet_id}')
    
    def find_pets_by_status(self, status):
        """Find pets by status (GET /pet/findByStatus)"""
        return self._request('GET', f'/pet/findByStatus?status={status}')