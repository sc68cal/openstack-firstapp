****************************************
Writing your First OpenStack Application
****************************************

This repo contains little random code snippets that could be
useful when preparing the "Writing your First OpenStack Application"
tutorial.

So far we have a basic message queue writer (sensor.py) and consumer
(backend.py). They'll just write and read random numbers using a queue.


Needs pika to run.


--------------------------------
 /doc
--------------------------------

/doc contains a playground for the actual tutorial documentation

It's RST, built with sphinx. There's a handy makefile.

The RST source includes conditional output logic, so specifying

make libcloud

will invoke sphinx-build with -t libcloud, meaning sections
marked .. only:: libcloud in the RST will be built, while others
won't. 


sphinx and openstackdoctheme are needed to build the docs

