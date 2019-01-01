#Build freeciv-web from latest repo
import docker
import os

def build_docker_img():
    absp = os.path.abspath(__file__)
    os.system("sudo " + os.path.dirname(absp) + os.sep + "prep_fire_selenium.sh")
    client = docker.from_env()
    print("Start building freeciv-web server. Take some coffee and relax. Takes up to 20minutes")
    cli = docker.APIClient(base_url='unix://var/run/docker.sock')
    for line in cli.build(path="https://github.com/chris1869/freeciv-web.git#develop", tag="freeciv-web"):
        if not "Downloading" in line:
            print line

#build_docker_img()
