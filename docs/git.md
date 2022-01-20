<div align="center">
<h1>Git Guide</a></h1>
<br>
</div>

---

# Introduction

The following notes' taken from [Colt Steele](https://www.youtube.com/watch?v=USjZcfj8yxE). However, I have added some steps on remote repositories towards the end.

## Git

### Downloading and Installing Git

Git is primarily used via the command-line interface, which we can access with our system terminals.

However, we first need to make sure that we have Git installed on our computers.

!!! note
    You can download Git here: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Click the download link for your specific operating system and then follow through the installation wizard to get things set up on your computer!

After installing it, start your terminal and type the following command to verify that Git is ready to be used on your computer:

```bash
git --version
```

If everything went well, it should return the Git version that is installed on your computer.

!!! note
    If you are using a Mac or Linux machine, then you can utilize the default Bash terminal that comes pre-installed on your machine.
    
    If you are using Windows, you can use its built-in Powershell terminal, or the Git Bash terminal which is bundled with the Git installation. For detailed windows Git and Git Bash install instructions, check out this blog post: [https://zarkom.net/blogs/how-to-install-git-and-git-bash-on-windows-9140](https://zarkom.net/blogs/how-to-install-git-and-git-bash-on-windows-9140)

---

### Configure name and email

In your terminal, run the following commands to identify yourself with Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Replace the values inside the quotes with your name and email address. This is to better identify who committed which lines of codes.

---

### Initialize Repositories

#### Initialize Local Repo

An isolated repository stored on your own computer, where you can work on the local version of your project.

```bash
git init
```

This command will generate a hidden **.git** directory for your project, where Git stores all internal tracking data for the current repository.

```bash
ls -a # to see the hidden git repo
```

#### Initialize Remote Repo

Generally stored outside of your isolated local system, usually on a remote server. It's especially useful when working in teams - this is the place where you can share your project code, see other people's code and integrate it into your local version of the project, and also push your changes to the remote repository.

!!! note
    Simply create this using this simple [guide](https://docs.github.com/en/get-started/quickstart/create-a-repo).


#### Git Clone

Special mention if you have just reset your computer and want to clone your repo from remote. Then you do not need `git init` and just use `git clone https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository folder_name` to clone your repo to local. See more [here](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository).

---

### Staging and committing code

Committing is the process in which the changes are *'officially'* added to the Git repository.

In Git, we can consider **commits** to be checkpoints, or snapshots of your project at its current state. In other words, we basically save the current version of our code in a commit. We can create as many commits as we need in the commit history, and we can go back and forth between commits to see the different revisions of our project code. That allows us to efficiently manage our progress and track the project as it gets developed.

Commits are usually created at logical points as we develop our project, usually after adding in specific contents, features or modifications (like new functionalities or bug fixes, for example).

#### Creating gitignore

Usually, I recommend creating `.gitignore` at this step, because you want to list down files that you do not wish git to track. This is important because some secret keys should never be pushed to the remote server for people to see. Furthermore, some large files should be kept in a storage as git cannot store too large files.

To ignore files that you don't want to be tracked or added to the staging area, you can create a file called `.gitignore` in your main project folder.

Inside of that file, you can list all the file and folder names that you definitely do not want to track (each ignored file and folder should go to a new line inside the **.gitignore** file).

You can read an article about ignoring files [on this link](https://help.github.com/en/articles/ignoring-files).

#### Checking Status (git status)

While located inside the project folder in our terminal, we can type the following command to check the status of our repository:

```bash
git status
```

This is a command that is very often used when working with Git.  It shows us which files have been changed, which files are tracked, etc.

We can add the untracked project files to the **staging area** based on the information from the `git status` command.

At a later point, `git status` will report any modifications that we made to our tracked files before we decide to add them to the staging area again.

#### Staging files (git add) 

Here we can tell git which files should be tracked.

```bash
git add . # add all files
git add filename.py file.md # add single/multiple individual files
```

#### Making commits (git commit)

 A **commit** is a snapshot of our code at a particular time, which we are saving to the commit history of our repository. After adding all the files that we want to track to the staging area with the `**git add`** command, we are ready to make a commit.

To commit the files from the staging area, we use the following command:

```bash
git config --global core.editor "code --wait" # use this code if popup editor does not appear.
git commit -a # a pop up editor should appear for you to type the message.
```

The commit message should be a descriptive summary of the changes that you are committing to the repository.

After executing that command, you will get the technical details about the commit printed in the terminal. And that's basically it, you have successfully made a commit in your project!

!!! tip
    Files that are changed in sync should be committed together. As an example, you made changes to three files, a, b and c, if a and b are related and c is unrelated to both of them, then it is logical to do the following:
    ```bash
    git add a b
    git commit -a "Commit related files"
    git add c
    git commit -a "Commit c file"
    ```

#### Commit History

To see all the commits that were made for our project, you can use the following command:

```bash
git log
```

The logs will show details for each commit, like the author name, the generated hash for the commit, date and time of the commit, and the commit message that we provided.

To go back to a previous state of your project code that you committed, you can use the following command:

```bash
git checkout <commit-hash>
```

Replace `<commit-hash>` with the actual hash for the specific commit that you want to visit, which is listed with the `git log` command.

To go back to the latest commit (the newest version of our project code), you can type this command:

```bash
git checkout master
```

### Branches

A **branch** could be interpreted as an individual timeline of our project commits.

With Git, we can create many of these alternative environments (i.e. we can create different **branches**) so other versions of our project code can exist and be tracked in parallel.

That allows us to add new (experimental, unfinished, and potentially buggy) features in separate branches, without touching the '*official'* stable version of our project code (which is usually kept on the **master** branch).

When we initialize a repository and start making commits, they are saved to the **master** branch by default.

#### Creating a new branch

You can create a new branch using the following command:

```bash
git branch <new-branch-name>
```

The new branch that gets created will be the reference to the current state of your repository.

!!! note
    It's a good idea to create a **development** branch where you can work on improving your code, adding new experimental features, and similar. After development and testing these new features to make sure they don't have any bugs and that they can be used, you can merge them to the master branch.


#### Changing branches

To switch to a different branch, you use the **git checkout** command:

```bash
git checkout <branch-name>
```

With that, you switch to a different isolated timeline of your project by changing branches.

!!! note
    For example, you could be working on different features in your code and have a separate branch for each feature. When you switch to a branch, you can commit code changes which only affect that particular branch. Then, you can switch to another branch to work on a different feature, which won't be affected by the changes and commits made from the previous branch.

To create a new branch and change to it at the same time, you can use the **-b** flag:

```bash
git checkout -b <new-branch-name>
```

!!! info
    To list the branches for your project, use this command: `git branch`

To go back to the **master** branch, use this command:

```bash
git checkout master
```

#### Merging branches

You can merge branches in situations where you want to implement the code changes that you made in an individual branch to a different branch.

For example, after you fully implemented and tested a new feature in your code, you would want to merge those changes to the stable branch of your project (which is usually the default **master** branch).

To merge the changes from a different branch into your current branch, you can use this command:

```bash
git merge <branch-name>
```

You would replace `<branch-name>` with the branch that you want to integrate into your current branch.

#### Deleting a branch

To delete a branch, you can run the **git branch** command with the **-d** flag:

```bash
git branch -d <branch-name>
```

!!! info
    Read more about branching and merging [on this link](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).

---

### Git remote

!!! note
    Note everything done above is still at local repository, as a result, we now need to push the changes into GitHub's remote server.

#### Remote add origin

To add a remote repository to our local repository, we first go create a personal access token[^github token], we can use the following command:
```bash
git remote add origin "your-repo-http" # add remote origin
git remote set-url origin https://[token]@github.com/[username]/[repository] # set the remote origin
# remove remote origin if needed (usually no need path)
```

To remove or show remote origins, use:
```bash
git remote rm origin    # remove origin
git remote show origin  # show remote origin
```

#### Push

Finally, we use `git push origin master -u` to push to master branch.

!!! note
    One thing worth noting is that if you created the repository with some files in it, then the above steps will lead to error. Instead, to overwrite : do `git push -f origin master` . For newbies, it is safe to just init a repo with no files inside in the remote to avoid the error "Updates were rejected because the tip...".

---

### Pulling

If you are writing code on your main desktop, say system A and committing a lot of changes, and when you are outside you are using your portable macbook, say system B, you may want to do the following:

1. If your last commit of system A is at commit 6, and system B is at commit 3, where commit 4-6 were done on A, then you can simply call:

    ```bash
    git config --global pull.rebase false  # merge (the default strategy)
    git pull origin master
    ```

2. However, if you have uncommited changes on system B and did not commit yet, then what you can do is call:

    ```bash
    git stash # this saves a snapshot of your current work and remove the commit
    git pull origin master
    ```

---

### Useful Git Commands

To undo git add before a commit, run git reset <file> or git reset to unstage all changes.

[^github_token]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[^github_auth]: https://stackoverflow.com/questions/68779962/github-removed-username-password-authorization-now-what

---

### Git Branches For Personal Projects Guidelines

#### Website and Blogging

Assume that I wrote a notebook named `blog.ipynb` and I want to publish it to my personal blog. Here are the general guidelines.

- Say that I put the notebook `blog.ipynb` in the `notebooks` folder in master branch.
- Then before I publish, I have a collaborator named **Joe** who is also a collaborator of my personal blog (who acts as my editor).
- I will create a new branch named `blog` and push the notebook to the branch.
- Then I will commit the notebook to the branch and create a pull request for **Joe** to review. 
    - If **Joe** approves the pull request, then I will merge the branch to the master branch using `squash and merge` or `merge commit`.
    - If **Joe** proposes some small changes, I will then go my branch `blog` and make the changes locally, and commit them with a pull request for **Joe** again. Once he approved, I will merge the branch to the master branch.
- After the merge, I will delete the branch `blog` as the updates are reflected in the master branch.

The above can be outlined in pseudo code below:

```bash
# Place the notebook `blog.ipynb` in the `notebooks` folder in master branch.
# Create a new branch named `blog` and push the notebook to the branch.
git checkout -b <new-branch-name> blog
git status # to see the status of the current branch.
# Convert the notebook to markdown if needed.
jupyter nbconvert --to markdown mynotebook.ipynb
# Commit the notebook to the branch.
git add .
git commit -a
git push origin branch_name -u
# Go to the pull request link, and select reviewer for review.
# If no changes proposed, merge the branch to master.
# If there are changes proposed, edit the codes in the branch locally and push the changes to the branch for review again. After that go to the same link and click on re-review.
```

After review and approved by the reviewer, you have 3 merge options.

- Squash and Merge: Take all the commits during the review and merge them into one commit. The only downside is you cannot go back to one unique commit but you will see all commit messages tho and changes.
- Create a merge commit: Create a merge commit with the changes from the review. You can use this if you want `git` to track every single commit (messages).

The merge will mean it is updated in master branch also. Then delete the branch if not in use.

---

#### Git Branches For Machine Learning Projects

git branch for pytorch pipeline:

1. In my main PyTorch repo, the code is on the branch `master`. 
2. I want to create a branch for a new competition using the `master` branch. # git checkout -b ...
3. Put the competition data in a different folder that stores all data. In a way, you can put it like this:
    ```
    data/competition_1_data/
    data/competition_2_data/
    ```
4. I will write code inside the branch.
   1. Scenario 1: I made changes in the branch and also want to merge this change into main -> commit, push, merge, pull to master branch.
      1. You can also create a `dev` branch and work on it as well.
   2. Scenario 2: I made changes specific to this branch, and I don't want to merge and merge some commits that propels to the main.