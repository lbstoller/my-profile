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
tag in your repository; Cloudlab maintains a cache of your branches and tags
and lets you select one when you start your experiment. (See below for 
information about telling Cloudlab to update its cache)

* *Execute* services run **after** the nodes have cloned your repository,
so you may refer to the clone (in `/local/repository`) from your services.
See `profile.py` in this repository for an example of how to run a program
from your repository.

* Place anything you like in your repository, with the caveat that a giant
repository (including, say, the linux source code), will take a long time
to clone to each of your nodes. You might also get a message from Cloudlab
staff asking about it.

### Using the same repository for multiple profiles:

Often it is convenient to point multiple profiles at the same
repository. This is fine to do, although each profile would run the
same script. Sometimes this is what you want to do, but often you
would like different profiles to run a different scripts.
To do this, create a subdirectory called `profiles` at the top level
of the repository and move your `profile.py` or `profile.rspec` into
the new sub directory.

If you want a specfic profile (say, `mynewprofile`) to run a different
script then your other profile (say, `myoldprofile`), rename
`profile.py` to `myoldprofile.py` and add a new script called
`mynewprofile.py`.  When you instantiate or edit `mynewprofile`, the
`mynewprofile.py` script will be used.

### Updating your profile after updates to your repository

When you change your repository you will typically want your Cloudlab
profile to be updated as well, especially if you have changed `profile.py`
or `profile.rspec`. But you might also have added a new branch or tag that
you would like to instantiate. Before you can do that, you need to tell
Cloudlab to update your profile. There are two ways to do that, one is a
manual method and the other is an automated method:

#### Manual method

After you update your repository, return to the Cloudlab web interface, and
on the `Edit Profile` page, you will see an **Update** button next to the
repository URL. Click on the **Update** button, and Cloudlab will do another
pull from your repository, update the list of branches and tags, and update
the source code on the page if it has changed. 

#### Automated method

Many public Git repositories like [github.com](https://git-scm.com/),
[bitbucket.org](https://bitbucket.org), and others based on
[GitLab](https://www.gitlab.com/), support *push* 
[webhooks](https://developer.github.com/webhooks/), 
which is a mechanism to notify a third party that your repository has
changed, either by a push to the repository or by the web interface.

Once you setup a push webhook, each commit to your repository will cause
Cloudlab to fetch from your repository, updating your profile to reflect the
current HEAD of your master branch. Branches and tags are updated as well.
When complete, we will send you an email confirmation so you know that your
profile has been updated. 

Setting up a webhook is relatively straightforward. First, on the `Edit
Profile` page for your profile, copy the **Push URL** from the Repository
Info panel in the lower left. Here are instructions for several popular Git
hosting services: 

* **github.com**: Go to your repository and click on the **Settings** option
in the upper right, then click on **Webhooks**, then click on the
**Add Webhook** menu option. Paste your push URL into the **Payload URL**
form field, leave everything else as is, and click on the **Add Webhook**
button at the bottom of the form.

* **gitlab**: Go to your repository and click on **Settings** 
in the upper right, then click on the **Integrations** menu option.  Paste
your push URL into the **URL** form field, leave everything else as is, and
click on the **Add Webhook** button at the bottom of the form.

* **bitbucket.org**: Go to your repository and click on **Settings** 
in the lower left, then click on the **Webhooks** menu option, then click
on the **Add Webhook** button. Give your new webhook a **Title** and paste
your push URL into the **URL** form field, leave everything else as is, and
click on the **Save** button at the bottom of the form.

### Caveats

* At the moment, the repository clones on nodes in your experiments are not automatially
updated after Cloudlab is informed of a repository update. This is a future TODO item.
