================================
 Section One: Getting Started
================================

The purpose of this tutorial is to navigate you through creating a basic <THING/APP IDEA>.

We assume you already have an OpenStack cloud to use with a quota of at least 3 servers, and have

.. only:: libcloud

  `libcloud 0.15.1 or better installed <https://libcloud.apache.org/>`_.

.. only:: openstacksdk

    the OpenStack SDK  installed.

.. only:: jclouds

    `jClouds 1.8 or better installed <https://jclouds.apache.org/start/install>`_.

.. only:: fog

      `fog 1.19 or better installed <http://www.fogproject.org/wiki/index.php?title=FOGUserGuide#Installing_FOG>`_.

.. only:: node

      `a recent version of pkgcloud installed <https://github.com/pkgcloud/pkgcloud#getting-started>`_.

.. only:: dotnet

      `OpenStack SDK for Microsoft .NET 0.9.1 or better installed <https://www.nuget.org/packages/OpenStack-SDK-DotNet>`_.

We also assume that you have the following 4 variables, which are needed to connect to the cloud:

* auth URL
* username
* project id or name (most SDKs can handle either)
* password

Now, let's make a connection to your cloud, so we can check what release you're running:

.. only:: libcloud
   
    .. code-block:: python

      from libcloud.compute.types import Provider
      from libcloud.compute.providers import get_driver

      OpenStack = get_driver(Provider.OPENSTACK)
      conn = OpenStack('your_auth_username', 'your_auth_password',
                          ex_force_auth_url='http://192.168.1.101:5000',
                          ex_force_auth_version='2.0_password')

.. only:: openstacksdk
   
    .. code-block:: python

      from openstack import connection
      conn = connection.Connection(auth_url=\"https://myopenstack:5000/v3\",
                                   user_name=\"me\", password=\"secret\", ...)


we'll use this 'conn' object throughout the tutorial, so ensure you always have one handy.


Next, let's look at what images and flavors are available

.. only:: libcloud
   
    .. code-block:: python

       images = conn.list_images()
       print images
       [<NodeImage: id=48b3409c-f504-4bbe-9384-34bd5566e5fc, name=mysql, driver=OpenStack  ...>, <NodeImage: id=4be4103f-c7cf-433f-8d78-1a475d5ec8ea, name=Fedora-x86_64-20-20140618-sda, driver=OpenStack  ...>, <NodeImage: id=f8e3be39-fced-4bc7-b37a-ec9eb9f87808, name=cirros-0.3.2-x86_64-uec, driver=OpenStack  ...>, <NodeImage: id=59336a5a-0a0f-41ca-bfb4-e9bcfa326c7c, name=cirros-0.3.2-x86_64-uec-ramdisk, driver=OpenStack  ...>, <NodeImage: id=9e45cda7-279a-4bb8-8245-f4713913dc0b, name=cirros-0.3.2-x86_64-uec-kernel, driver=OpenStack  ...>]


       sizes = conn.list_sizes()
       print sizes
       [<OpenStackNodeSize: id=1, name=m1.tiny, ram=512, disk=1, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>, <OpenStackNodeSize: id=2, name=m1.small, ram=2048, disk=20, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>, <OpenStackNodeSize: id=3, name=m1.medium, ram=4096, disk=40, bandwidth=None, price=0.0, driver=OpenStack, vcpus=2,  ...>, <OpenStackNodeSize: id=4, name=m1.large, ram=8192, disk=80, bandwidth=None, price=0.0, driver=OpenStack, vcpus=4,  ...>, <OpenStackNodeSize: id=42, name=m1.nano, ram=64, disk=0, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>, <OpenStackNodeSize: id=451, name=m1.heat, ram=512, disk=0, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>, <OpenStackNodeSize: id=5, name=m1.xlarge, ram=16384, disk=160, bandwidth=None, price=0.0, driver=OpenStack, vcpus=8,  ...>, <OpenStackNodeSize: id=84, name=m1.micro, ram=128, disk=0, bandwidth=None, price=0.0, driver=OpenStack, vcpus=1,  ...>]


Next, let's create a server, using an image from before:

.. only:: libcloud
   
    .. code-block:: python

       testing =  conn.create_node(name='testing', image=images[0], size=sizes[0])
       print testing
       <Node: uuid=1242d56cac5bcd4c110c60d57ccdbff086515133, name=testing, state=PENDING, public_ips=[], private_ips=[], provider=OpenStack ...>

       servers = conn.list_nodes()


.. only:: openstacksdk
   
    .. code-block:: python

       args = {
           \"name\": \"my_server\",
           \"flavorRef\": \"big\",
           \"imageRef\": \"asdf-1234-qwer-5678\",
           \"key_name\": \"my_ssh_key\",
       }
       server = conn.compute.create_server(**args)
       servers = conn.compute.list_servers()


Kill the server, and time to start our app

.. only:: libcloud
   
    .. code-block:: python

       conn.destroy_node(servers[0])



Our app is awesome! something something something.

.. only:: libcloud
   
    .. code-block:: python


       SCRIPT = '''#!/usr/bin/env bash
       git clone https://github.com/fifieldt/openstack-firstapp
       cd openstack-firstapp
       python install.py
       '''
       
       server = conn.deploy_node(name='app1', image=images[0], size=sizes[0],
                                 deploy=ScriptDeployment(SCRIPT))


Now visit the awesome graphic interface!!!

