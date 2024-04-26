# pylibsproject
Repo to try convenient python libraries

# Appendix
## How to make poetry use an uninstalled python version as its environment (Ubuntu 22.04)
Install pyenv. Disregard the suggestions of changing your `bashrc` and `profile` files.
```bash
curl https://pyenv.run | bash
```
This command clones pyenv repo in your home as a hidden folder named .pyenv.
```bash
ls ~/.pyenv/
```
We want to install the desired python version inside this folder, but first we need to install some dependencies globally
```bash
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
Now we can run
```bash
.pyenv/bin/pyenv install <desired_python_version>
```
And we can already create a virtual environment using poetry with the following command
```bash
poetry env use ~/.pyenv/versions/<python_version_installed_by_pyenv>/bin/python
poetry install
```
If you are using Visual Code, you can change your interpreter by clicking `ctrl+shift+p` and inputing the path to the new python binary. The path should be something like this:
```bash
/home/blai/.cache/pypoetry/virtualenvs/pylibsproject-N9N1g_2H-py3.12/bin/python
```
