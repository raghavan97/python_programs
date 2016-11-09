import docker
from pprint import pprint

cli = docker.Client(base_url='unix://var/run/docker.sock')

# The cli offers a bunch of things that you can usually do with
# docker commands like pull, list images, tag, list conatiners etc
pprint('Methods allowed are :')
pprint(dir(cli))


pprint('The containers are :')
containers = cli.containers()
for c in containers:
	pprint(c)