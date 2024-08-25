from debox_chat import DeBox
import os 
from dotenv import load_dotenv # pip install python-dotenv

# You must create a file .env file with the DEBOX_API_KEY
load_dotenv()
DEBOX_API_KEY = os.environ["DEBOX_API_KEY"]

# Initialize DeBox with your API key
debox = DeBox(api_key=DEBOX_API_KEY)

# User and Group IDs
user_id = "0qkl9pdk"    # set this to the user id of the user you want to send the test messages
group_id = "dj6txzao"   # set this to the group id of the group you want to send the test messages
image_url = "https://data.debox.space/dao/newpic/one.png"   # image url to use in the test messages
href = "https://data.debox.space/dao/newpic/one.png"    # href url to use in the test messages

# Get user information
user_info = debox.get_user_info(user_id)    
print("User Info:", user_info)

# Get group information
group_info = debox.get_group_info(group_id)
print("Group Info:", group_info)

# Send a text message to a user
response = debox.send_message(user_id, "Hello! Have a great day with DeBox!")
print("Send Message to User Response:", response)

# Send a text message to a group
response = debox.send_group_text_message(group_id, user_id, "Daily Reminder", "Don't forget to check your DeBox tasks!")
print("Send Text Message to Group Response:", response)

# Send a graphic message to a group
title = "Check out this cute pic!"
content = "Here's an adorable picture to brighten your day."
response = debox.send_group_graphic_message(group_id, user_id, title, content, image_url, href)
print("Send Graphic Message to Group Response:", response)

# Send a graphic message to a user
title = "Surprise!"
content = f"Look at this funny image, isn't it cool? URL: [click here]({href})"
response = debox.send_graphic_message(user_id, title, content, image_url, href)
print("Send Graphic Message to User Response:", response)

