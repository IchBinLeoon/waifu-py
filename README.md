# waifu-py
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/waifu-py?style=flat-square)](https://pypi.org/project/waifu-py/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/waifu-py?style=flat-square)](https://pypi.org/project/waifu-py/)
[![PyPI](https://img.shields.io/pypi/v/waifu-py?style=flat-square)](https://pypi.org/project/waifu-py/)
[![License](https://img.shields.io/github/license/IchBinLeoon/waifu-py?style=flat-square)](https://github.com/IchBinLeoon/waifu-py/blob/main/LICENSE)

A simple Python wrapper for the waifu.pics API.

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [Contribute](#Contribute)
- [License](#License)

## Installation
**Python 3.6 or higher is required.**

Install from PyPI
```shell
$ pip install waifu-py
```

Install from source
```shell
$ pip install git+https://github.com/IchBinLeoon/waifu-py
```

## Usage
You can use either WaifuClient or WaifuAioClient, depending on whether you want a synchronous wrapper class, or an asynchronous wrapper class. Below are some examples of how to use WaifuClient and WaifuAioClient.

### Usage Examples with WaifuClient
```python
from waifu import WaifuClient

client = WaifuClient()

# Get one SFW image
sfw_waifu: str = client.sfw(category='waifu')

# Get 30 unique SFW images
sfw_megumin_list: list = client.sfw(category='megumin', many=True)

# Get 30 unique SFW images and exclude images in list
sfw_megumin_list_exclude: list = client.sfw(category='megumin', many=True, exclude=['https://i.waifu.pics/IqD8csE.png', 'https://i.waifu.pics/NV-dfTH.png'])

# Get one NSFW image
nsfw_neko: str = client.nsfw(category='neko')

# Get 30 unique NSFW images
nsfw_trap_list: list = client.nsfw(category='trap', many=True)
```

### Async Usage Examples with WaifuAioClient
```python
import asyncio

from waifu import WaifuAioClient


async def main():
    async with WaifuAioClient() as client:

        # Get one SFW image
        sfw_neko: str = await client.sfw(category='neko')

        # Get 30 unique SFW images
        sfw_shinobu_list: list = await client.sfw(category='shinobu', many=True)

        # Get one NSFW image
        nsfw_waifu: str = await client.nsfw(category='waifu')

        # Get 30 unique NSFW images
        nsfw_neko_list: list = await client.nsfw(category='neko', many=True)

asyncio.run(main())
```
```python
import asyncio

from waifu import WaifuAioClient


async def main():
    client = WaifuAioClient()

    # Get one SFW image
    sfw_waifu: str = await client.sfw(category='waifu')

    # Get 30 unique NSFW images
    nsfw_waifu_list: list = await client.nsfw(category='waifu', many=True)

    await client.close()

asyncio.run(main())
```

### Usage Examples with own Session
If you want to use your own requests or aiohttp session, you can do that too.

#### WaifuClient
```python
import requests

from waifu import WaifuClient

session = requests.Session()
client = WaifuClient(session=session)

# ...
```

#### WaifuAioClient
```python
import asyncio

import aiohttp

from waifu import WaifuAioClient


async def main():
    session = aiohttp.ClientSession()
    async with WaifuAioClient(session=session) as client:
        # ...

asyncio.run(main())
```
```python
import asyncio

import aiohttp

from waifu import WaifuAioClient


async def main():
    session = aiohttp.ClientSession()
    client = WaifuAioClient(session=session)

    # ...

    await client.close()

asyncio.run(main())
```

### Image Categories
You can also view all valid image categories.
```python
from waifu import ImageCategories

print(ImageCategories)
```
Output:
```shell
{
   "sfw":[
      "waifu",
      "neko",
      "shinobu",
      "megumin",
      "bully",
      "cuddle",
      "cry",
      "hug",
      "awoo",
      "kiss",
      "lick",
      "pat",
      "smug",
      "bonk",
      "yeet",
      "blush",
      "smile",
      "wave",
      "highfive",
      "handhold",
      "nom",
      "bite",
      "glomp",
      "kill",
      "slap",
      "happy",
      "wink",
      "poke",
      "dance",
      "cringe"
   ],
   "nsfw":[
      "waifu",
      "neko",
      "trap",
      "blowjob"
   ]
}
```

## Contribute
Contributions are welcome! Feel free to open issues or submit pull requests!

## License
MIT © [IchBinLeoon](https://github.com/IchBinLeoon/waifu-py/blob/main/LICENSE)
