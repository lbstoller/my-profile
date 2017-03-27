This is a demonstration of a *repository-based* Cloudlab profile.
Repository based profiles are a great way to combine a git repository (for
source code control) and a Cloudlab profile (for experiment control). The
Cloudlab profile that is based on this repository can be found at
https://www.cloudlab.us/p/PortalProfiles/RepoBased.

### Important notes about repository-based profiles:

* Your profile needs to be **publicly readable** so that we can pull from your
repository without needing credentials.

* Your repository must contain a file called `profile.py` (a geni-lib
script) **or** `profile.rspec` (an rspec) in the top level directory.
Your topology will be loaded from that file. Please place the source file
in the toplevel directory.

* When you instantiate an experiment based on your profile, we will clone
your repository to each of your experimental nodes in the
`/local/repository` directory, and set it to match whatever branch or tag
you have choosen to instantiate. You will not be able to push to your
repository of course, until you install the necessary credentials on your
nodes.

* You will be able to instantiate an experiment from any branch (HEAD) or
tag in your repository; Cloudlab maintains a list of your branches and tags
lets you select one when you start your experiment.

* *Execute* services run **after** the nodes have cloned your repository,
so you may refer to the clone (in `/local/repository`) from your services.
See `profile.py` in this repository for an example of how to run a program
from your repository.

* Place anything you like in your repository, with the caveat that a giant
repository (including, say, the linux source code), will take a long time
to clone to each of your nodes. You might also get a message from Cloudlab
staff asking about it.

