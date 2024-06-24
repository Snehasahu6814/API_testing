import pytest
import requests
@pytest.fixture(name="base_url")
def base_url():
    return "https://petstore.swagger.io/v2"
def test_add_new_store(base_url):
    order_id=45
    new_store={
  "id": order_id,
  "petId": 1,
  "quantity": 3,
  "shipDate": "2024-06-06T05:47:24.425Z",
  "status": "placed",
#   "complete": "true"
  }
    response=requests.post(f"{base_url}/store/order",json=new_store,timeout=10)
    assert response.status_code==200
def test_get_user_by_store(base_url):
    response=requests.get(f"{base_url}/store/inventory",timeout=10)
    assert response.status_code==200
def test_get_store_by_storeid(base_url):
    order_id=45
    response=requests.get(f"{base_url}/store/order/{order_id}",timeout=10)
    assert response.status_code==200
    assert response.json()["id"]==order_id
def test_del_store_by_storeid(base_url):
    order_id=45
    response=requests.delete(f"{base_url}/store/order/{order_id}",timeout=10)
    assert response.status_code==200
 
