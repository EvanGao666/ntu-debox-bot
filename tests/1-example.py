from debox_chat import DeBox
from openai import OpenAI

# Initialize DeBox with your API key
debox = DeBox(api_key="ptXsmpsMbXT2Iw59")

# User and Group IDs
user_id = "oa3szhac"
group_id = "jp6nayhu"
image_url = "https://data.debox.space/dao/newpic/one.png"
href = "https://data.debox.space/dao/newpic/one.png"

# # Send a text message to a user
# response = debox.send_message(user_id, "Hello! Have a great day with DeBox!")
# print("Send Message to User Response:", response)

# # Send a graphic message to a user
# title = "Surprise!"
# content = "Look at this funny image, isn't it cool?"
# response = debox.send_graphic_message(user_id, title, content, image_url, href)
# print("Send Graphic Message to User Response:", response)

# Send a text message to a group
response = debox.send_group_text_message(group_id, user_id, "Daily Reminder", "Don't forget to check your DeBox tasks!")
print("Send Text Message to Group Response:", response)

# # Send a graphic message to a group
# title = "Check out this cute pic!"
# content = "Here's an adorable picture to brighten your day."
# response = debox.send_group_graphic_message(group_id, user_id, title, content, image_url, href)
# print("Send Graphic Message to Group Response:", response)


