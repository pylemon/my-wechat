## How to run

First, clone the latest source from github:

Then, install the required packages using pip:

```bash
$ [sudo] pip install -r requirements.txt
```

Create a text file named wechat.conf in the source code directory, write the configuration and save. For example:

```python
#coding=utf-8
debug = False
port = 8888
token = 'your token'
username = 'your username'
simsimi_key = ''
talkbot_brain_path = 'talkbot.brn'
```

Now, let's start the server:

```bash
$ python app.py
```
