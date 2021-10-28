# sqlite3_wrapper

Use this to interface with sqlite3. Work in progress

## To install:
Get the setup tools
```bash
pip install wheel setuptools twine
```
Clone this repo and go into root directory. Create the wheel file using:
```bash
python setup.py bdist_wheel
```
Install wheel using:
```bash
pip install dist/<wheel_file>.whl
```
and finally import wherever using:
```bash
import sqlite3_wrapper.sqlite3_wrapper as sqw
```
