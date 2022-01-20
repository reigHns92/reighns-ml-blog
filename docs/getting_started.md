<div align="center">
<h1>Setup Guide</a></h1>
by Hongnan Gao
<br>
</div>

---

# Introduction

This getting started guide is written to ensure I follow standard coding practices.

!!! note "Important"
    To render Table of Content when compiling `mkdocs serve`, one must always have the following structure:
    ```md
    # Type your article title here
    ## ... 
    ## ...
    ```
    Notice that the top level header must be #, and subsequent nested headers should be ##.

---

## Setting up Environment

Assuming VSCode setup, open up terminal/powershell in your respective system and type:
    ```bash
    code "path to folder"
    ```
    to open up VSCode.

## Virtual Environment

In your IDE, you want to set up a virtual environment.

```sh
# For Ubuntu
sudo apt install python3.8 python3.8-venv python3-venv

# For Mac
pip3 install virtualenv
```

You can activate the VM as follows:

```sh
# Assuming Windows
python -m venv venv_bcw
.\venv_bcw\Scripts\activate
python -m pip install --upgrade pip setuptools wheel # upgrade pip
```

```bash
# Assuming Linux
python3 -m venv venv_bcw
source venv_bcw/bin/activate
python -m pip install --upgrade pip setuptools wheel # upgrade pip
```

```bash
# Assuming Mac
virtualenv venv_bcw
source venv_bcw/bin/activate
python -m pip install --upgrade pip setuptools wheel # upgrade pip
```

---

## Setup and requirements

!!! note
    For small projects, we can have `requirements.txt` and just run `(venv_ml) pip install -r requirements.txt`. For larger projects, we can follow the steps below.

Create a file named `setup.py` and `requirements.txt` concurrently. The latter should have the libraries that one is interested in having for his project while the formal is a `setup.py` file where it contains the setup object which describes how to set up our package and it's dependencies. The first several lines cover metadata (name, description, etc.) and then we define the requirements. Here we're stating that we require a Python version equal to or above 3.8 and then passing in our required packages to install_requires. Finally, we define extra requirements that different types of users may require. This is a standard practice and more can be understood from madewithml.com.

The user can now call the following commands to install the dependencies in their own virtual environment.

```bash
pip install -e .  # installs required packages only       
python -m pip install -e ".[dev]"                                       # installs required + dev packages
python -m pip install -e ".[test]"                                      # installs required + test packages
python -m pip install -e ".[docs_packages]"                             # installs required documentation packages
```

!!! note "Important"
    Something worth taking note is when you download PyTorch Library, there is a dependency link since we are downloading cuda directly, you may execute as such:

```bash
pip install -e . -f https://download.pytorch.org/whl/torch_stable.html
```

---

## Command Line

Something worth noting is we need to use dash instead of underscore when calling a function in command line.

reighns_linear_regression regression-test --solver "Batch Gradient Descent" --num-epochs 500

## Documentation

### Type Hints

### Mkdocs + Docstrings

1. Copy paste the template from Goku in, most of what he use will be in `mkdocs.yml` file. Remember to create the `mkdocs.yml` in the root path.
2. Then change accordingly the content inside `mkdocs.yml`, you can see my template that I have done up.
3. Remember to run `python -m pip install -e ".[docs_packages]" ` to make sure you do have the packages.
4. Along the way you need to create a few folders, follow the page tree in mkdocs.yml, everything should be created in `docs/` folder.
5. As an example, in our reighns-linear-regression folder, we want to show two scenarios:
    - Scenario 1: I merely want a full markdown file to show on the website. In this case, in the "watch", we specify a path we want to watch in our `docs/` folder. In this case, I created a `documentation` folder under `docs/` so I specify that. Next in the `docs/documentation/` folder I create a file called `linear_regression.md` where I dump all my markdown notes inside. Then in the `nav` tree in `mkdocs.yml`, specify
    ```
    nav:
    - Home:
        - Introduction: index.md
    - Getting started: getting_started.md
    - Detailed Notes:
        - Notes: documentation/linear_regression.md
        - Reference: documentation/reference_links.md
    ```
    Note that Home and Getting Started are optional but let us keep it for the sake of completeness. What you need to care is "Detailed Notes" and note the path I gave to them - which will point to the folders in `docs/documentation/`.

    - Scenario 2: I want a python file with detailed docstrings to appear in my static website. This is slightly more complicated. First if you want a new section of this you can create a section called `code_reference`, both under the `nav` above and also in the folder `docs/`, meaning `docs/code_reference/` must exist. Put it under watch as well. Now in `docs/code_reference/` create a file named say `linear_regression_from_scratch.md` and put `::: src.linear_regression` inside, note that you should not have space in between.
    
    
---


## Misc Problems

This is testing[^1] footnotes.

!!! failure
    sss.

    sss.

- How to show nbextensions properly https://stackoverflow.com/questions/49647705/jupyter-nbextensions-does-not-appear/50663099

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.



## Run

1. Run config.py as this will create folders for you automatically.





## Setting up GitHub Pages and Mkdocs (Website)

!!! note "Update November 9th, 2021"
    You can skip most steps if you just fork this repository and follow the format.

Welcome to my example website! This website uses
[MkDocs](https://www.mkdocs.org/) with the [Material
theme](https://squidfunk.github.io/mkdocs-material/) and an automated
deployment workflow for publishing to [GitHub
Pages](https://pages.github.com/).

This guide will help you create your own GitHub Pages website with
this setup. If you're using Windows, you should run all the commands
in this guide on a Windows Subsystem for Linux (WSL) terminal.



### Initializing your Website Repository

First, [create a new repository](https://github.com/new) on
GitHub. Make sure to skip the initialization step on the website
&mdash; you will be initializing the contents of this repository with
this template! Note down the Git remote for your new repository,
you'll need it later when initializing your local copy of the
repository.

Next, download the website template and extract it:

```sh
$ wget https://github.com/jansky/test-website/archive/refs/tags/template.tar.gz
$ tar xvf template.tar.gz
$ rm template.tar.gz
```

!!! note

    If the `wget` command is not found, you can install it using
    apt-get: `sudo apt-get install wget`.

This will create a new folder called `test-website-template` in
your current directory with the website template contents. You may
wish to rename this folder to something like `my-website`:

```sh
$ mv test-website-template my-website
```

Now you can initialize a Git repository with the website contents:

```sh
$ cd my-website
$ git init
$ git remote add origin YOUR_GITHUB_REPOSITORY_REMOTE
```

### Website Configuration

The configuration for your website is stored in `mkdocs.yml` in the
repository root. You only need to change a few settings at the
top of the file:

```yaml linenums="1"
site_name: Example Website
site_url: https://reighns92.github.io/test-website
nav:
  - Home: index.md
  - About: about.md
  - Notebooks: notebooks_list.md
...
```

First, update the `site_name` and `site_url` fields to be correct for
your website. The URL format for GitHub pages websites is

```
https://USERNAME.github.io/REPOSITORY-NAME
```

As you add content to your website, you can also control the pages
that appear on your website's navbar in the `nav` field. Each `nav`
list element is of the form

```yaml
Link Text: filename.md
```

For navbar links pointing to pages in your site, you should use a file
path which is relative to the `docs/` folder where all your website
content is stored. You may also link to external pages and include
sub-links. For more information, you can view the [MkDocs nav
documentation](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation).

### GitHub Actions Configuration

You also need to update the GitHub Actions deployment workflow
with the name and e-mail address to use when the workflow
pushes your built website to the `gh-pages` branch of your
repository. In the file `.github/workflows/deploy-website.yml`,
update lines 25 and 26 to reflect your account information:

```yaml linenums="22" hl_lines="4 5"
...
- name: Push Build Website to gh-pages Branch
  run: |
   git config --global user.name 'YOUR NAME(Automated)'
   git config --global user.email 'YOUR-GITHUB-USERNAME@users.noreply.github.com'
...
```

### Setting Up Local Development

MkDocs makes it easy to develop your website locally and see your
changes in real time. To begin, set up and activate Python virtual
environment for this project. Then, install the project dependencies:

```sh
(venv) $ pip install -r requirements.txt
```

MkDocs includes a small webserver that allows you to preview your
website in your browser as you make changes. Whenever you save one of
your source files, the website will be rebuilt and your browser will
automatically refresh to show the new changes. You can start this
development server using the `serve` command:

```sh hl_lines="5"
(venv) $ mkdocs serve
INFO     -  Building documentation...
...
INFO     -  Documentation built in 0.16 seconds
INFO     -  [20:09:07] Serving on http://127.0.0.1:8000/...
...
```

If you copy and paste the URL given by MkDocs into your browser you
will see your website preview.

### Adding Website Content

Markdown files added under the `docs/` folder will be converted
to HTML pages on your website. This website template enables some
helpful extensions for

- rendering of math in LaTeX style,
- admonitions such as notes and warnings, and
- code blocks with syntax highlighting.

In addition, MkDocs also supports GitHub-flavored Markdown tables. To
see examples of syntax for these elements, see the MkDocs website [here](https://squidfunk.github.io/mkdocs-material/).


#### Deploying Your Changes

When you are ready to deploy your website for the first time, make an
initial commit and push to your GitHub remote:

```sh
$ git add .
$ git commit -a -m "Initial Commit"
$ git push origin master -u
```

### Activate Workflow

The GitHub Actions deployment workflow included with this template
runs whenever you push to the `master` branch. This workflow will
build your website using MkDocs and push the built website files to
the `gh-pages` branch of your repository, which GitHub Pages can use
to serve your website.

Once you have pushed your changes, go to your repository page on
GitHub and confirm that the GitHub Actions workflow has completed
successfully (you should see a green checkmark next to the name of the
most recent commit). Then, go to your repository settings page, and
click on 'Pages'. You will see a section that will let you set the
source for your GitHub Pages website. Click the box labelled 'None'
and select the `gh-pages` branch. Leave the selectd folder at '/
(root)' and click 'Save'. Your website is now live!

To push additional changes, simply commit and push to the master
branch. The GitHub Actions deployment workflow will handle deploying
your changes to GitHub Pages.

### Pandoc (Markdown Converter)

More often than not, you will need to convert a jupyter notebook to markdown file for deployment (as markdown supports Admonitions in Mkdocs). Here is a way to do it, it is very convenient as it not only converts your notebook files to markdown, it also stores your output as images in a folder for you. This means any images rendered in notebook by `matplotlib` etc will now show up in markdown!

```bash
brew install pandoc
git clone https://github.com/jupyter/nbconvert.git
cd nbconvert
pip install -e .
```

Then to convert, simply do the following:
```bash
jupyter nbconvert --to markdown mynotebook.ipynb
```

---

#### Pandoc (Wikitext to Markdown)

From the solution [here](https://stackoverflow.com/questions/70484071/how-to-use-pandoc-to-convert-wikitext-to-markdown-with-latex-mathjax-etc-properl). We can do the following:

```bash
pandoc --from mediawiki --to=markdown-definition_lists wiki.txt  -o wiki.md
```

where `wiki.txt` is a text file with wiki markup.

---

## Miscellaneous Problems

### Path Environment

Often times, you will encounter a problem with the path environment when working with Windows especially. For example, when you do the following:

```bash
jupyter nbconvert --to markdown mynotebook.ipynb
```

then `'jupyter' is not recognized as an internal or external command, operable program or batch file.` is the error message even though `jupyter` is installed. Usually, the shell will prompt a message to check `PATH`. 

Now go to Advanced System Settings and click on Environment Variables. You will see a list of environment variables. You can add a new environment variable by clicking on the plus sign in the **System Variables**. Add the path recommended by `jupyter` to the `PATH` variable. In my case, it is the obscure `C:\Users\reighns\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts`.

### Mkdocs

#### Full page width

Use this custom `css` code to make page full width.
