# Introduction

This repository contains the markup, images, and website generation tools for [Advanced Level Experiemental Physics](http://alevelexperimentalphysics.info/index.html).

# Making Changes
## Modifying the Markup

You need Python and Sphinx installed to generate the website.  If you have Python, run `pip install Sphinx` to install Sphinx. 

To modify content, make changes to the files in the **content/** directory.  Generate the website by running `make html` on your command line from the root directory of the project, **alep/**.  View your changed content by viewing **_build/html/index.html** in your browser.

One you have made your changes, commit them.  `git commit -a`

### If you have write access to this repository

Push your changes to the repository `git push`.  If you have "merge conflicts", `git pull` before you git push.

Then, make your changes live.  Run `make upload` and enter your Github credentials when prompted to submit your changes to the **gh-pages** branch. Once this command finishes successfully, your changes will be visible on the [website](http://alevelexperimentalphysics.info/index.html).

### If you do not have write access

Submit your your changes as a [pull request](https://help.github.com/articles/about-pull-requests/) to the repository ([github.com/bdrach/alep](https://github.com/bdrach/alep)).

You can also make note of typos and potential enhancements in the **Issues** tab of this Github repository.



