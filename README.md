# Introduction

This repository contains the markup, images, and website generation tools for [Advanced Level Experiemental Physics](http://alevelexperimentalphysics.info/index.html).

# Modifying the Markup

To modify content, make changes to the files in the **markup/** directory.  Generate the website by running `make` on your command line from the root directory of the project (**alep/**).  View your changed content by opening the newly-created **_html/index.html** in your browser.

Submit your changes as a pull request to this repository ([github.com/bdrach/alep](https://github.com/bdrach/alep)).

# Uploading Changes 

*To upload changes, you must have write access to this repository.*

First, make sure to commit your changes.  `git commit -a`

Then run `make upload` and enter your github credentials when prompted.  

This command submits your changes to the **gh-pages** branch. Once this command finishes successfully, your changes will be visible on the [website](http://alevelexperimentalphysics.info/index.html).
