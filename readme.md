##### Overview
    These are steps to run three Docker containers:
    - python Flask REST app using uWSGI
    - nginx
    - postgres
    
    docker-compose will be used to launch the three Docker containers

    Prerequisites: 
    
    install docker - google instructions for your flavor or Linux or Mac or Windows 10
    
    install docker-compose

    Instructions to install docker-compose
    https://docs.docker.com/compose/install/
    

##### build images 
    sudo docker-compose build

##### run containers
    sudo docker-compose up

##### interface with Flask REST app on port 8080. To change the port edit docker-compose.yml under nginx:
        nginx:
        build: ./nginx
        container_name: nginx
        restart: always
        ports:
        - "8080:80"


##### stop and remove containers
    sudo docker-compose down

##### rebuild and run
    sudo docker-compose up --build

