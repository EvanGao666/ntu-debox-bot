import requests
import json
import os

class DeBox:
    """
    A class to interact with the DeBox API for sending messages and retrieving user and group information.

    Attributes
    ----------
    API_KEY : str
        The API key for authenticating with the DeBox API.
    USER_INFO_URL : str
        The URL endpoint for retrieving user information.
    GROUP_INFO_URL : str
        The URL endpoint for retrieving group information.
    SEND_MESSAGE_URL : str
        The URL endpoint for sending messages.
    SEND_GRAPHIC_MESSAGE_URL : str
        The URL endpoint for sending graphic messages.
    SEND_GROUP_TEXT_MESSAGE_URL : str
        The URL endpoint for sending group text messages.
    SEND_GROUP_GRAPHIC_MESSAGE_URL : str
        The URL endpoint for sending group graphic messages.

    Methods
    -------
    get_user_info(user_id):
        Retrieves information for a specified user.
    get_group_info(group_id):
        Retrieves information for a specified group.
    send_message(to_user_id, message):
        Sends a text message to a specified user.
    send_group_text_message(group_id, to_user_id, title, content):
        Sends a text message to a specified group.
    send_group_graphic_message(group_id, to_user_id, title, content, image_url, href):
        Sends a graphic message to a specified group.
    send_graphic_message(to_user_id, title, content, image_url, href):
        Sends a graphic message to a specified user.
    """

    USER_INFO_URL = "https://open.debox.pro/openapi/authorize/userinfo"
    GROUP_INFO_URL = "https://open.debox.pro/openapi/group/info"
    SEND_MESSAGE_URL = "https://open.debox.pro/openapi/send_robot_message"
    SEND_GRAPHIC_MESSAGE_URL = "https://open.debox.pro/openapi/send_robot_message"
    SEND_GROUP_TEXT_MESSAGE_URL = "https://open.debox.pro/openapi/send_robot_group_message"
    SEND_GROUP_GRAPHIC_MESSAGE_URL = "https://open.debox.pro/openapi/send_robot_group_message"

    def __init__(self, api_key=None):
        """
        Initializes the DeBox class with the provided API key. If no API key is provided, 
        it checks for the DEBOX_API_KEY environment variable.

        Parameters
        ----------
        api_key : str, optional
            The API key for the DeBox API (default is None).

        Raises
        ------
        ValueError
            If the API key is not provided and the DEBOX_API_KEY environment variable is not set.
        """
        if api_key:
            self.API_KEY = api_key
        else:
            self.API_KEY = os.getenv("DEBOX_API_KEY")
            if not self.API_KEY:
                raise ValueError("API key must be provided either as an argument or set as an environment variable 'DEBOX_API_KEY'.")

    def get_user_info(self, user_id):
        """
        Retrieves information for a specified user.

        Parameters
        ----------
        user_id : str
            The ID of the user to retrieve information for.

        Returns
        -------
        dict
            The user information.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        url = f"{self.USER_INFO_URL}?user_id={user_id}"
        headers = {
            "X-API-KEY": self.API_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_group_info(self, group_id):
        """
        Retrieves information for a specified group.

        Parameters
        ----------
        group_id : str
            The ID of the group to retrieve information for.

        Returns
        -------
        dict
            The group information.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        url = f"{self.GROUP_INFO_URL}?group_invite_url=https://m.debox.pro/group?id={group_id}"
        headers = {
            "X-API-KEY": self.API_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_message(self, to_user_id, message):
        """
        Sends a text message to a specified user.

        Parameters
        ----------
        to_user_id : str
            The ID of the user to send the message to.
        message : str
            The message content.

        Returns
        -------
        dict
            The response from the DeBox API.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY
        }
        data = {
            "to_user_id": to_user_id,
            "object_name": "RCD:Command",
            "message": message
        }
        response = requests.post(self.SEND_MESSAGE_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_group_text_message(self, group_id, to_user_id, title, content):
        """
        Sends a text message to a specified group.

        Parameters
        ----------
        group_id : str
            The ID of the group to send the message to.
        to_user_id : str
            The ID of the user to send the message to.
        title : str
            The title of the message.
        content : str
            The content of the message.

        Returns
        -------
        dict
            The response from the DeBox API.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY
        }
        data = {
            "to_user_id": to_user_id,
            "group_id": group_id,
            "object_name": "RC:TxtMsg",
            "title": title,
            "content": content,
            "message": content,
            "href": ""
        }
        response = requests.post(self.SEND_GROUP_TEXT_MESSAGE_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_group_graphic_message(self, group_id, to_user_id, title, content, image_url, href):
        """
        Sends a graphic message to a specified group.

        Parameters
        ----------
        group_id : str
            The ID of the group to send the message to.
        to_user_id : str
            The ID of the user to send the message to.
        title : str
            The title of the message.
        content : str
            The content of the message.
        image_url : str
            The URL of the image to include in the message.
        href : str
            The hyperlink associated with the image.

        Returns
        -------
        dict
            The response from the DeBox API.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY
        }
        data = {
            "to_user_id": to_user_id,
            "group_id": group_id,
            "object_name": "RCD:Graphic",
            "title": title,
            "content": content,
            "message": image_url,
            "href": href
        }
        response = requests.post(self.SEND_GROUP_GRAPHIC_MESSAGE_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_graphic_message(self, to_user_id, title, content, image_url, href):
        """
        Sends a graphic message to a specified user.

        Parameters
        ----------
        to_user_id : str
            The ID of the user to send the message to.
        title : str
            The title of the message.
        content : str
            The content of the message.
        image_url : str
            The URL of the image to include in the message.
        href : str
            The hyperlink associated with the image.

        Returns
        -------
        dict
            The response from the DeBox API.

        Raises
        ------
        requests.exceptions.RequestException
            If the request to the DeBox API fails.
        """
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": self.API_KEY
        }
        data = {
            "to_user_id": to_user_id,
            "object_name": "RCD:Graphic",
            "title": title,
            "content": content,
            "message": image_url,
            "href": href
        }
        response = requests.post(self.SEND_GRAPHIC_MESSAGE_URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

