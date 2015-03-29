****************************************
Writing your First OpenStack Application
****************************************

This repo contains little random code snippets that could be
useful when preparing the "Writing your First OpenStack Application"
tutorial.

App for the tutorial can now be found at: 

https://github.com/stackforge/faafo

--------------------------------
 /doc
--------------------------------

/doc contains a playground for the actual tutorial documentation

It's RST, built with sphinx.

The RST source includes conditional output logic, so specifying

tox -e libcloud

will invoke sphinx-build with -t libcloud, meaning sections
marked .. only:: libcloud in the RST will be built, while others
won't. 


sphinx and openstackdoctheme are needed to build the docs

