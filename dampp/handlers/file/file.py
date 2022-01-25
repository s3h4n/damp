""" This module will help to create required files.
 
    - File.dockerfile will return the content required for Dockerfile.
    - File.docker_compose will return the content required for docker-compose.yml.
    - File.index_dot_php will return the content required for index.php.
"""


class File:

    def __init__(self, project_name):
        self.project_name = project_name
        self.line = ""

    def dockerfile(self, image: str = ...):
        l = self.line
        l += f"# Auto generated by DAMPP.\n# Do not remove.\n\n"
        l += f"FROM {image}\n"
        l += f"RUN apt-get update && apt-get upgrade -y\n"
        l += f"RUN docker-php-ext-install mysqli\n"
        l += f"EXPOSE 80\n"

        return l

    def docker_compose(self, docker_version: str = ..., service_web: str = ..., service_db: str = ..., service_pma: str = ...):
        l = self.line
        l += f"# Auto generated by DAMPP.\n# Do not remove.\n"
        l += f"\nversion: '{docker_version}'\n"
        l += f"\nservices:\n"
        l += service_web + service_db + service_pma

        return l

    def index_dot_php(self, pma_port: str = ...):
        return "<!DOCTYPE html><html lang=en><title>DAMP</title><meta charset=utf-8><meta content='width = device-width, initial-scale = 1, shrink-to-fit = no'name=viewport><style>body{font-family:Ubuntu,sans-serif}div{padding:.5rem}a{text-decoration:none}code{color:#ff1493;font-weight:700}.center{background-color:#fff;box-shadow:0 4px 8px 0 rgba(0,0,0,.2);transition:.3s;border-radius:12.5px;padding:2rem;margin:0;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center}.center:hover{box-shadow:0 8px 16px 0 rgba(0,0,0,.2)}.btn{padding:10px 35.5px 10px 35.5px;margin-top:15px;color:#fff;background-color:#dc143c;border:0;border-radius:30px;font-size:2.4vh;font-weight:700}.btn:hover{background-color:#000;color:#fff;font-weight:700}.tracking-in-contract{-webkit-animation:tracking-in-contract .8s cubic-bezier(.215,.61,.355,1) both;animation:tracking-in-contract .8s cubic-bezier(.215,.61,.355,1) both}@-webkit-keyframes tracking-in-contract{0%{letter-spacing:1em;opacity:0}40%{opacity:.6}100%{letter-spacing:normal;opacity:1}}@keframes tracking-in-contract{0%{letter-spacing:1em;opacity:0}40%{opacity:.6}100%{letter-spacing:normal;opacity:1}}</style><div class=center><span class=tracking-in-contract><a href=https://github.com/s3h4n/dampp.git target=_blank><h1 style=color:#dc143c>DAMP</h1></a><h3>Dockerized Apache MySQL PHP</h3></span><hr><div><p>Customize <code>"+f"{self.project_name}"+"/web/index.php</code> to see the changes.</div><hr><div><button class=btn onclick=open_php_my_admin() type=button>PhpMyAdmin</button></div></div><script defer>const open_php_my_admin = () => { window.open('http://localhost:"+f"{pma_port}"+"/', '_blank');;};</script></body></html>"
