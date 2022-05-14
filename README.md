# dockerConsole


## Setup
- Make sure to make thes configrations on your environment
    - `pip install django==3`
    - `pip freeze > $ requirements.txt`
    - `pip install -r requirements.txt`
    - `sudo apt update`
    - `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"`
    - `apt-cache policy docker-ce`
    - `sudo apt install docker-ce`
    - `sudo systemctl status docker`
    - `pip install Celery==4.3`
    - `pip freeze > requirements.txt`
    - `redis-server`
    - `pip install redis==2.10.3`
    - `pip freeze > requirements.txt`
