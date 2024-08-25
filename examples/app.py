import os 
import logging 
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from debox_chat import DeBox

load_dotenv()


'''
To test the API run the following CURL command:

REPLACE 0qkl9pdk with YOUR USER_ID to test receiving the "echo" message from your BOT in your account.
"echo" message means the API will respond with the same message the user send to the API: "echo" the user's message.

curl -X POST http://localhost:3001/api/destars \
-H "Content-Type: application/json" \
-H "X-Api-Key: REPLACE_THIS_WITH_YOUR_WEBHOOK_KEY" \
-d '{
  "from_user_id": "0qkl9pdk",
  "to_user_id": "test_user01",
  "group_id": "",
  "message": "Hello there! Testing the API webhook!",
  "language": "en"
}'


'''

app = Flask(__name__)

DEBOX_API_KEY = os.environ["DEBOX_API_KEY"]
DEBOX_WEBHOOK_KEY = os.environ["DEBOX_WEBHOOK_KEY"]

# Initialize DeBox with your API key
debox = DeBox(api_key=DEBOX_API_KEY)

# Add the file handler to the Flask app's logger
app.logger.setLevel(logging.INFO)

@app.route('/api/destars', methods=['POST'])
def destars_api():

    content = request.json
    headers  = request.headers
    app.logger.info(f"Received content: {content} headers: {headers}")

    token = request.headers.get('X-Api-Key')
    if not token or token != DEBOX_WEBHOOK_KEY:
        return jsonify({'message': 'Unauthorized'}), 401

    from_user_id = content.get('from_user_id')
    to_user_id = content.get('to_user_id')
    group_id = content.get('group_id')
    user_message = content.get('message')
    language = content.get('language')

    app.logger.info(f"Decoded content - from_user_id:{from_user_id} to_user_id:{to_user_id} group_id:{group_id}  user_message:{user_message} language:{language}")

    # simple "echo" of the user message for DEMO purpose
    bot_response = user_message
    image_url = "https://data.debox.space/dao/newpic/one.png"   # image url to use in the test messages
    href = "https://data.debox.space/dao/newpic/one.png"    # href url to use in the test messages

    if group_id == "":
        response = debox.send_graphic_message(from_user_id, "Echo Message", bot_response, image_url, href)
    else:
        response = debox.send_group_graphic_message(group_id, from_user_id, "Echo Message", bot_response, image_url, href)

    return jsonify({'status': f'Message processed successfully: {response}'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)