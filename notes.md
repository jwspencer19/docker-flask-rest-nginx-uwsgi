##### on CentOS 7 system to install python3.x
    yum install centos-release-scl
    yum install rh-python36

##### on CentOS 7 system to enable python3.x
    scl enable rh-python36 bash

##### now python 3.x, note: only set in this shell session. Exit session will go back to 2.x
    python --version

##### create virtual enviroment
    virtualenv venv --python=python3.6

##### activate the virtual environment
    source venv/bin/activate

##### pip install packages
    pip install flask uwsgi

##### create requirements.txt
    pip freeze > requirements.txt

##### create .dockerignore file with
    venv/
    __pycache__/


##### to test our flask app locally
    export FLASK_APP=run.py
    export FLASK_ENV=development

    flask run


##### start postgres docker container separately for now, until added to docker-compose
    docker run --rm  --name pg-docker -e POSTGRES_PASSWORD=docker -v /home/spencer/postgres_data:/var/lib/postgresql/data -d -p 5432:5432 postgres:latest



