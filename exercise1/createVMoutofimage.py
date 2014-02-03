from keystoneclient.v2_0 import Client as KeystoneClient
from glanceclient import Client as GlanceClient
from novaclient.v1_1 import Client as NovaClient

keystone = KeystoneClient(username = 'admin',
               		  password = 'password',
                          tenant_name = 'demo',
                          auth_url = 'http://10.0.2.15:5000/v2.0')
glance = GlanceClient('1', endpoint = 'http://10.0.2.15:9292',
			   token = keystone.auth_token)
images = glance.images.list()
for image in images:
	if image.name == 'ubuntu':
		nova = NovaClient(username = "admin", 
				  api_key = 'password',  
				  auth_url = 'http://10.0.2.15:5000/v2.0',
				  project_id = 'demo')
		flavor = nova.flavors.find(name='m1.small')
		nova.servers.create(name = "myubuntu", 
				    image = image.id,
				    flavor = flavor)


