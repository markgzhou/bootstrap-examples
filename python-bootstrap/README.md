# Introduction
This is a bootstrap project that you can follow to start a python project.

# Setup Development Environment

## Install and configure pyenv
    # Install pyenv  
    brew update
    brew install pyenv
    
    # Init pyenv:
    eval "$(pyenv init -)"
    eval "$(pyenv init --path)"  #Use this command if previous line not working
    
    #Install and set python 3.8.8
    pyenv install 3.8.8
    pyenv global 3.8.8
    python --version
    python3 --version


    # (Optional) If you experienced compile error related to zlib \
    # Run the following commands:
    brew install zlib
    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"


## Install and configure pyenv-virtualenv
    # Init pyenv-virtualenv:
    eval "$(pyenv virtualenv-init -)"

## Virtual environment
    # Create the virtual environment my_env
    pyenv virtualenv 3.8.8 my_env
    
    # Activate my_env
    pyenv activate my_env

    # Install project dependencies:
    pip3 install --upgrade pip
    pip3 install -r requirements.txt

# Test and Run
## Test
    PYTHONPATH=. pytest tests/

## Code Static Analysis
    PYTHONPATH=. pylint --rcfile="./source/.pylintrc" source/
    PYTHONPATH=. pylint --rcfile="./tests/.pylintrc" tests/    

## Run
    PYTHONPATH=. python3  ./source/main.py

