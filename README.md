# NTU DeBox Chatbot

本项目是一个基于 Flask 的聊天机器人，集成了 **DeBox SDK** 和 **OpenAI (DeepSeek API)**。机器人可监听聊天群组中的特定命令并提供智能回复。所有配置详情均安全地存储在 `.env` 文件中，确保代码与配置分离。

---

## 功能特点

1. **基于命令的交互**：
    - `/bot`：激活机器人，为用户开启监听功能。
    - `/stop`：停用机器人，停止监听用户消息。
2. **智能回复**：利用 OpenAI 的 DeepSeek API 生成自然语言回复。
3. **安全的 Webhook 验证**：通过 `WEBHOOK_KEY` 确保只处理经过认证的请求。
4. **模块化配置**：使用 `.env` 文件管理环境变量，便于配置和维护。

---

## 环境需求

请确保已安装以下环境：

-   Python 3.8+
-   `pip`（Python 包管理工具）

---

## 安装步骤

1. **克隆仓库**：

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **设置环境变量**：  
   在项目根目录下创建 `.env` 文件，并添加以下内容：

    ```dotenv
    DEBOX_API_KEY=<你的_debox_api_key>
    OPENAI_API_KEY=<你的_openai_api_key>
    OPENAI_BASE_URL=https://api.deepseek.com
    WEBHOOK_KEY=<你的_webhook_key>
    FLASK_HOST=0.0.0.0
    FLASK_PORT=5000
    ```

    将 `<你的_debox_api_key>`、`<你的_openai_api_key>` 和 `<你的_webhook_key>` 替换为你的实际密钥。

---

## 使用方法

### 激活机器人

1. 在你的聊天群组中输入 `/bot` 来激活机器人。
2. 机器人将开始监听你的消息并提供智能回复。

### 停用机器人

1. 在你的聊天群组中输入 `/stop` 来停用机器人。
2. 机器人将停止监听你的消息。

---

## 部署步骤

1. 打开一个终端，运行以下命令：

    ```bash
    ngrok http 5000
    ```

    在输出中找到 `Forwarding` 后的 URL，配置到 DeBox|Developer 的 Information-> App Domain 和 Bot-> Webhook URL 中。拿到 Webhook Key 填入.env 文件中。

2. 再打开一个终端，运行以下命令：

    ```bash
    python tests/2-deepseek.py
    ```

---

这样你就可以成功部署并运行该聊天机器人！
