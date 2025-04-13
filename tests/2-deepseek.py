import sys
import os

# 添加项目根目录到模块搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 设置 .env 文件路径
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../.env")

# 现在可以开始导入其他模块了
from debox_chat import DeBox
from openai import OpenAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv(dotenv_path)


# 从环境变量中加载配置
DEBOX_API_KEY = os.getenv("DEBOX_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
WEBHOOK_KEY = os.getenv("WEBHOOK_KEY")
FLASK_HOST = os.getenv("FLASK_HOST")
FLASK_PORT = int(os.getenv("FLASK_PORT"))

# 初始化 OpenAI 和 DeBox SDK
client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
debox = DeBox(api_key=DEBOX_API_KEY)

# 初始化 Flask 应用
app = Flask(__name__)

# 存储用户会话的状态
active_listeners = {}

# 处理 Webhook 消息
@app.route('/v1/webhook', methods=['POST'])
def webhook():
    # 验证 Webhook 请求的身份（检查 X-API-KEY）
    api_key = request.headers.get('X-API-KEY')
    if api_key != WEBHOOK_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    print("Received data:", data)

    message = data.get('message', '')
    from_user_id = data.get('from_user_id')
    group_id = data.get('group_id')

    # 检测到 /bot 命令，启动监听
    if message.strip() == "/bot" and from_user_id not in active_listeners:
        active_listeners[from_user_id] = True
        debox.send_group_text_message(group_id, from_user_id, "Bot Activated", "Bot is all ears! Say anything, and I'll be here to help!")
        return jsonify({"response": "Bot Activated"})

    # 检测到 /stop 命令，停止监听
    if message.strip() == "/stop" and from_user_id in active_listeners:
        active_listeners.pop(from_user_id, None)
        debox.send_group_text_message(group_id, from_user_id, "Bot Deactivated", "Bot's taking a break! Catch you later!")
        return jsonify({"response": "Bot Deactivated"})

    # 如果不是指令，继续对话
    if from_user_id in active_listeners:
        # 调用 DeepSeek API 获取回复
        conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]
        conversation_history.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=conversation_history,
            stream=False
        )

        bot_reply = response.choices[0].message.content
        # 发送机器人回复
        debox.send_group_text_message(group_id, from_user_id, "Bot Reply", bot_reply)
        return jsonify({"response": bot_reply})

    return jsonify({"response": "No action taken"})

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
