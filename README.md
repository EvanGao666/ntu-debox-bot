<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<div align="center">
  <a href="https://github.com/cchacons/debox-chat-python-sdk/graphs/contributors"><img src="https://img.shields.io/github/contributors/cchacons/debox-chat-python-sdk?style=for-the-badge&color=blue" alt="Contributors"></a>
  <a href="https://github.com/cchacons/debox-chat-python-sdk/network/members"><img src="https://img.shields.io/github/forks/cchacons/debox-chat-python-sdk?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/cchacons/debox-chat-python-sdk/stargazers"><img src="https://img.shields.io/github/stars/cchacons/debox-chat-python-sdk?style=for-the-badge&color=blue" alt="Stargazers"></a>
  <a href="https://github.com/cchacons/debox-chat-python-sdk/issues"><img src="https://img.shields.io/github/issues/cchacons/debox-chat-python-sdk?style=for-the-badge&color=blue" alt="Issues"></a>
  <a href="https://github.com/cchacons/debox-chat-python-sdk/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cchacons/debox-chat-python-sdk?style=for-the-badge&color=blue" alt="MIT License"></a>
</div>

<!-- PROJECT LOGO -->
<div align="center">
  <br>
  <img src="docs/static/img/logo.svg" alt="Logo" width="200" height="200">
  <h1 align="center">DeBox Chat Python SDK</h1>
  <a href="https://cchacons.github.io/debox-chat-python-sdk"><img src="https://img.shields.io/badge/Documentation-DeBox%20Chat%20SDK-blue?logo=googledocs&logoColor=white&style=for-the-badge" alt="Check out the documentation"></a>
  <br>
</div>
<hr>

Welcome to the DeBox Chat Python SDK, a library to interact with the DeBox API for sending messages and retrieving user and group information.

![App screenshot](docs/static/img/screenshot1.png)

## ⚡ Getting Started

To install the DeBox Chat Python SDK, you have two options:

1. Clone the repository and install manually:

    ```bash
    git clone https://github.com/cchacons/debox-chat-python-sdk.git
    cd debox-chat-python-sdk
    pip install .
    ```

2. Install directly from the GitHub repository using pip:

    ```bash
    pip install git+https://github.com/cchacons/debox-chat-python-sdk.git
    ```

## 🚀 Usage

Here is a simple example to get you started:

  ```python
  from debox_chat import DeBox

  # Initialize DeBox with your API key
  debox = DeBox(api_key="your_api_key")

  # Send a text message to a group
  response = debox.send_group_text_message(group_id="group_id", to_user_id="user_id", title="Hello", content="This is a text message.")
  print(response)

  # Send a graphic message to a group
  response = debox.send_group_graphic_message(group_id="group_id", to_user_id="user_id", title="Check this out", content="Here is an image.", image_url="https://example.com/image.png", href="https://example.com")
  print(response)

  ```

![App screenshot](docs/static/img/screenshot2.png)

## 🤝 How to Contribute
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

For details, please check CONTRIBUTING.md.

## 📜 License
Distributed under the MIT License. See LICENSE for more information.
