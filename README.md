- ##### create new virtual environment (if python version > 3.5):
> python3 -m venv testing-venv

- ##### active virtual environment:
> source testing-venv/bin/activate

- ##### upgrade pip
> pip install --upgrade pip

- ##### check pip-package installed:
> pip freeze

- ##### install all packages in requirements.txt
> pip install -r requirements.txt

- ##### show detail package:
> pip show package_name
> pip show requests

- ##### exit virtual environment:
> deactivate
<hr/>

- ##### install pyenv:
> sudo apt install -y make build-essential libssl-dev zlib1g-dev \                                   ok | 11:41:32 
> libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
> libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl \
> git

- ##### clone pyenv:
> git clone https://github.com/pyenv/pyenv.git ~/.pyenv

- ##### publish pyenv
> echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc                                                ok | 11:41:32 
> echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
> echo 'eval "$(pyenv init -)"' >> ~/.zshrc

- ##### list all python versions:
> pyenv install -l | more

- ##### install python:
> pyenv install 3.11.8

- ##### list all AVAILABLE python versions:
> pyenv versions

- ##### use specified python version
> pyenv global 3.11.8
