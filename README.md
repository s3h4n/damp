# DAMPP 🚢

DAMPP is a linux shell script to setup MySQL, Php, Apache, PhpMyAdmin inside of docker containers on any Ubuntu based system.

## Prerequisite ✔️

You must have <a href="https://docs.docker.com/engine/install/ubuntu/" target="_blank">Docker</a> installed in your system.
If your system is **Ubuntu based**, and it doesn't have Docker, you can install it by using <a href="https://github.com/s4nduni/docker-installer.git" target="_blank">docker-installer</a>. 

## Installation ✨

Paste following command in your terminal.
```
wget https://raw.githubusercontent.com/s3h4n/dampp/main/dampp.py && python3 dampp.py && rm -r dampp.py
```

## Usage 🔥

After installing paste this command to start DAMPP.
```
cd your-app-name-here && ./dampp up
```
Use help see more.
```
./damp help
```

## Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
