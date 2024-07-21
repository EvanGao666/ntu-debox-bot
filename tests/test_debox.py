import pytest
import os
from debox_chat import DeBox

@pytest.fixture(scope="module")
def debox_instance():
    # Set up the DeBox instance with API key
    DEBOX_API_KEY = os.environ.get("DEBOX_API_KEY")
    if not DEBOX_API_KEY:
        raise ValueError("API key must be set in the environment variable 'DEBOX_API_KEY'.")
    debox = DeBox(api_key=DEBOX_API_KEY)
    return debox

@pytest.fixture(scope="module")
def user_and_group_ids():
    return {
        "user_id": "0qkl9pdk",
        "group_id": "dj6txzao",
        "image_url": "https://data.debox.space/dao/newpic/one.png",
        "href": "https://data.debox.space/dao/newpic/one.png"
    }

def test_get_user_info(debox_instance, user_and_group_ids):
    user_info = debox_instance.get_user_info(user_and_group_ids["user_id"])
    print("User Info:", user_info)
    assert user_info["code"] == 1
    assert "uid" in user_info["data"]

def test_get_group_info(debox_instance, user_and_group_ids):
    group_info = debox_instance.get_group_info(user_and_group_ids["group_id"])
    print("Group Info:", group_info)
    assert group_info["code"] == 200
    assert "gid" in group_info["data"]

def test_send_message(debox_instance, user_and_group_ids):
    response = debox_instance.send_message(user_and_group_ids["user_id"], "Hello! Have a great day with DeBox!")
    print("Send Message to User Response:", response)
    assert response["code"] == 200, f"Failed to send message: {response.get('message')}"

def test_send_group_text_message(debox_instance, user_and_group_ids):
    response = debox_instance.send_group_text_message(
        user_and_group_ids["group_id"], 
        user_and_group_ids["user_id"], 
        "Daily Reminder", 
        "Don't forget to check your DeBox tasks!"
    )
    print("Send Text Message to Group Response:", response)
    assert response["code"] == 200, f"Failed to send group text message: {response.get('message')}"

def test_send_group_graphic_message(debox_instance, user_and_group_ids):
    title = "Check out this cute pic!"
    content = "Here's an adorable picture to brighten your day."
    response = debox_instance.send_group_graphic_message(
        user_and_group_ids["group_id"], 
        user_and_group_ids["user_id"], 
        title, 
        content, 
        user_and_group_ids["image_url"], 
        user_and_group_ids["href"]
    )
    print("Send Graphic Message to Group Response:", response)
    assert response["code"] == 200, f"Failed to send group graphic message: {response.get('message')}"

def test_send_graphic_message(debox_instance, user_and_group_ids):
    title = "Surprise!"
    content = "Look at this funny image, isn't it cool?"
    response = debox_instance.send_graphic_message(
        user_and_group_ids["user_id"], 
        title, 
        content, 
        user_and_group_ids["image_url"], 
        user_and_group_ids["href"]
    )
    print("Send Graphic Message to User Response:", response)
    assert response["code"] == 200, f"Failed to send graphic message: {response.get('message')}"
