import pytest
import requests
@pytest.fixture(name="base_url")
def base_url():
    return "https://petstore.swagger.io/v2"
def test_add_new_petlist(base_url):
    new_user=[
  {
    "id": 0,
    "username": "Divi@123",
    "firstName": "Divi",
    "lastName": "Gupta",
    "email": "dgupta123@gmail.com",
    "password": "Gupta123",
    "phone": "987653456",
    "userStatus": 1
  }
]
    response=requests.post(f"{base_url}/user/createWithList",json=new_user,timeout=10)
    assert response.status_code==200
def test_add_newpet_array(base_url):
    new_user=[
  {
    "id": 1,
    "username": "Shrim@124",
    "firstName": "Shrim",
    "lastName": "Gupta",
    "email": "sgupta124@gmail.com",
    "password": "Gupta124",
    "phone": "9875438765",
    "userStatus": 0
  }
]
    response=requests.post(f"{base_url}/user/createWithArray",json=new_user,timeout=10)
    assert response.status_code==200
def test_get_user_by_username(base_url):
    username="Divi@123"
    response=requests.get(f"{base_url}/user/{username}",timeout=10)
    assert response.status_code==200
    assert response.json()["username"]==username
def test_update_user_by_username(base_url):
    username="Divi@123"
    new_user2={
      "id": 2,
      "username": "Arpana@124",
      "firstName": "Arpana",
      "lastName": "Singh",
      "email": "sappu124@gmail.com",
      "password": "Appu124",
      "phone": "9875786546",
      "userStatus": 0
    }
    response=requests.put(f"{base_url}/user/{username}",json=new_user2,timeout=10)
    assert response.status_code==200
  # assert response.json()["username"]==username
def test_delete_user(base_url):
    username="Shrim@124"
    response=requests.delete(f"{base_url}/user/{username}",timeout=10)
    assert response.status_code==200
def test_user_login(base_url):
    username="Divi@123"
    password= "Gupta123"
    response=requests.get(f"{base_url}/user/login",json={"username":username,"password":password}
                          ,timeout=10)
    assert response.status_code==200
def test_user_logout(base_url):
    response=requests.get(f"{base_url}/user/logout",timeout=10)
    assert response.status_code==200
def test_add_new_pet(base_url):
    new_user={
    "id": 4,
    "username": "Nikki@123",
    "firstName": "Nikita",
    "lastName": "Rathor",
    "email": "nrathor123@gmail.com",
    "password": "Rathor123",
    "phone": "6798452675",
    "userStatus": 1
  }
    response=requests.post(f"{base_url}/user",json=new_user,timeout=10)
    assert response.status_code==200     