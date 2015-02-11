================================
 Section One: Getting Started
================================

The purpose of this tutorial is to navigate you through creating a basic <THING/APP IDEA>.

We  assume you already have an OpenStack cloud to use, and have

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

We also assume that you have the following 4 variables, which are needed when using openstack API clients:

* auth URL
* username
* project id or name (most SDKs can handle either)
* password

Now, let's make a connection to your cloud, so we can check what release you're running:

.. only:: libcloud
   
    .. code-block:: python

      from libcloud.compute.types import Provider
      from libcloud.compute.providers import get_driver

      import libcloud.security

      libcloud.security.VERIFY_SSL_CERT = False

      OpenStack = get_driver(Provider.OPENSTACK)
      driver = OpenStack('your_auth_username', 'your_auth_password',
                          ex_force_auth_url='http://192.168.1.101:5000',
                          ex_force_auth_version='2.0_password')

.. only:: openstacksdk
   
    .. code-block:: python

      from openstack import connection
      conn = connection.Connection(auth_url="https://myopenstack:5000/v3",
                                   user_name="me", password="secret", ...)
       args = {
           "name": "my_server",
           "flavorRef": "big",
           "imageRef": "asdf-1234-qwer-5678",
           "key_name": "my_ssh_key",
       }
       server = conn.compute.create_server(**args)
       servers = conn.compute.list_servers()

