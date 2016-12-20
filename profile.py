"""An example of constructing a profile with a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

#
# This is a typical list of images.
#
imageList = [
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD', 'UBUNTU 16.04'),
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU14-64-STD', 'UBUNTU 14.04'),
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//CENTIS71-64-STD', 'CENTOS 7.1'),
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//FBSD102-64-STD', 'FreeBSD 10.2')]

# Define a single parameter for the instantiation page.
pc.defineParameter("osImage", "Select OS image",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList,
                   longDescription="Most clusters have this set of images, " +
                   "pick your favorite one.")

# Retrieve the values the user specifies during instantiation.
params = pc.bindParameters()

# Add a raw PC to the request.
node = request.RawPC("node")
node.disk_image = params.osImage

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
