Get Chromedriver
---
https://chromedriver.chromium.org/downloads

Get pip & virtualenv
---
- [get pip](https://pip.pypa.io/en/stable/installing/)
- [get virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

Activate Virtualenv
---

```bash
# Windows
<venv_path>/Scripts/activate

# Linux
<venv_path>/bin/activate
```

Install requirements
---
```bash
pip install -r requirements.txt
```

Set Env
---
| ENV          | Mean                 | Example                |
| :------------| :------------------- |:---------------------- |
| GW_URL       | Groupware url        | https://daou.sample.com  |
| USERNAME     | Groupware identifier | myid               |
| PASSWORD     | Gropuware password   | mypw               |
| DRIVER_PATH  | chromedriver path    | [**windows**] D:\path\chromedriver.exe<br>[**linux**] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/path/chromedriver |

Run
---
```bash
python main.py
```