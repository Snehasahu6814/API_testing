"""Testcases for pet """
import pytest
import requests

@pytest.fixture(name="base_url")
def base_url():
    return "https://petstore.swagger.io/v2"
def test_add_new_pet(base_url):
    new_pet ={
  "id": 1,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    response=requests.post(f"{base_url}/pet",json=new_pet,timeout=10)
    assert response.status_code==200
def test_get_pet_by_id(base_url):
    pet_id=1
    response=requests.get(f"{base_url}/pet/{pet_id}",timeout=10)
    assert response.status_code==200
    assert response.json()["id"]==pet_id
def test_update_pet(base_url):
    pet_id=3
    updated_pet_data={
      "id":pet_id,
      "name": "doggie",
      "status": "sold"
    }
    response=requests.put(f"{base_url}/pet",json=updated_pet_data,timeout=10)
    assert response.status_code==200
def test_update_pet_by_id(base_url):
    pet_id=1
    id: "pet_id"
    name: "tommy"
    status: "available"
    response=requests.post(f"{base_url}/pet/{pet_id}",timeout=10)
    assert response.status_code==200
def test_delete_pet(base_url):
    pet_id=1
    response=requests.delete(f"{base_url}/pet/{pet_id}",timeout=10)
    assert response.status_code==200
def test_get_pet_by_status(base_url):
    pet_status=[(("available",200),("pending",200),("sold",404))]
    response=requests.get(f"{base_url}/pet/findByStatus",json=pet_status,timeout=10)
    assert response.status_code==200   