"""
MIT License

Copyright (c) 2021 IchBinLeoon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
from typing import Optional, Union, Dict, List

import requests

from waifu.exceptions import APIException, InvalidCategory
from waifu.utils import BASE_URL, ImageCategories, ImageTypes

log = logging.getLogger(__name__)


class WaifuClient:
    """
    Wrapper client for the waifu.pics API.
    This class is used to interact with the API.

    Attributes:
        session (requests.Session): A requests session.
    """

    def __init__(self, session: Optional[requests.Session] = None) -> None:
        """
        Initializes the WaifuClient.

        Args:
            session (requests.Session, optional): A requests session.
        """
        self.session = session

    def _session(self) -> requests.Session:
        """
        Gets a requests session by creating it if it does not already exist.

        Returns:
            requests.Session: A requests session.
        """
        if self.session is None:
            self.session = requests.Session()
        return self.session

    def _request(self, url: str, method: str, *args, **kwargs) -> Dict[str, str]:
        """
        Performs an HTTP request.

        Args:
            url (str): The request url.
            method (str): The request method.

        Returns:
            dict: The data from the response.

        Raises:
            APIException: If the response contains an error.
        """
        session = self._session()
        response = getattr(session, method)(url, *args, **kwargs)
        log.debug(f'{method.upper()} {url} {response.status_code} {response.reason}')
        if response.status_code != 200:
            raise APIException(response.status_code, response.reason)
        data = response.json()
        return data

    def _get(self, url: str, *args, **kwargs) -> _request:
        """
        Performs an HTTP GET request.

        Args:
            url (str): The request url.

        Returns:
            _request()
        """
        return self._request(url, 'get', *args, **kwargs)

    def _post(self, url: str, *args, **kwargs) -> _request:
        """
        Performs an HTTP POST request.

        Args:
            url (str): The request url.

        Returns:
            _request()
        """
        return self._request(url, 'post', *args, **kwargs)

    def _fetch(
        self,
        type_: str,
        category: str,
        many: bool,
        exclude: List[str]
    ) -> Union[str, List[str]]:
        """
        Returns a single or 30 unique images of the specific type and category.

        Args:
            type_ (str): The type of the image.
            category (str): The category of the image.
            many (bool): Get 30 unique images instead of one if true.
            exclude (list): A list of URL's to not receive from the endpoint if many is true.

        Returns:
            str: The image URL.
            list: 30 unique image URL's if many is true.

        Raises:
            InvalidCategory: If the category is invalid.
        """
        if category not in ImageCategories[type_]:
            raise InvalidCategory(category)
        if many is True:
            data = self._post(f'{BASE_URL}/many/{type_}/{category}', json={'exclude': exclude})
        else:
            data = self._get(f'{BASE_URL}/{type_}/{category}')
        if many is True:
            return data.get('files')
        return data.get('url')

    def sfw(
        self,
        category: str,
        many: Optional[bool] = False,
        exclude: Optional[List[str]] = []
    ) -> Union[str, List[str]]:
        """
        Get a single or 30 unique SFW (Safe For Work) images of the specific category.

        Args:
            category (str): The category of the image.
            many (bool): Get 30 unique images instead of one if true.
            exclude (list): A list of URL's to not receive from the endpoint if many is true.

        Returns:
            str: The image URL.
            list: 30 unique image URL's if many is true.
        """
        data = self._fetch(ImageTypes.sfw, category, many, exclude)
        return data

    def nsfw(
        self,
        category: str,
        many: Optional[bool] = False,
        exclude: Optional[List[str]] = []
    ) -> Union[str, List[str]]:
        """
        Get a single or 30 unique NSFW (Not Safe For Work) images of the specific category.

        Args:
            category (str): The category of the image.
            many (bool): Get 30 unique images instead of one if true.
            exclude (list): A list of URL's to not receive from the endpoint if many is true.

        Returns:
            str: The image URL.
            list: 30 unique image URL's if many is true.
        """
        data = self._fetch(ImageTypes.nsfw, category, many, exclude)
        return data
