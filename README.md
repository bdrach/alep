# Introduction

This repository contains the markup, images, and website generation tools for [Advanced Level Experiemental Physics](http://alevelexperimentalphysics.info/index.html).

# Making Changes
## Modifying the Markup

To modify content, make changes to the files in the **markup/** directory.  Generate the website by running `make` on your command line from the root directory of the project, **alep/**.  View your changed content by opening the newly-created **_html/index.html** in your browser.

One you have made your changes, commit them.  `git commit -a`

### If you have write access to this repository

Push your changes to the repository `git push`.  If you have "merge conflicts", `git pull` before you git push.

Finally run `make upload` and enter your github credentials when prompted.  This command submits your changes to the **gh-pages** branch. Once this command finishes successfully, your changes will be visible on the [website](http://alevelexperimentalphysics.info/index.html).

### If you do not have write access

Submit your changes as a [pull request](https://help.github.com/articles/about-pull-requests/) to the repository ([github.com/bdrach/alep](https://github.com/bdrach/alep)).



