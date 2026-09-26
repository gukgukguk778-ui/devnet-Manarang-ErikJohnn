# Module 1 — Git & GitHub

**Student:** Manarang, Erik John D.
**Date:** 9/25/26

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is the version control framework that helps developers to track changes to their files and projects. Think of Git as a save history for a project. Git is the program that you run on a computer to control changes to your project. GitHub is a web service used to store and share Git repositories. GitHub also provides collaboration, pull requests, code review.

---

## Key vocabulary (in your own words)

- repository: create a project
- commit: Commit happens when you are completed editing what you have changed; you will use commit as a way to save your changes to your repository and you can also add a message in your commited changes .
- branch: This is a version of the project. In this version you can work on new features or changes without immediately affecting the main branch.
- push / pull: Push means sending my commit changes to the repository. Pull means downloading the changes, from GitHub.
- pull request: this is the place where you will request to combine the changes from one branch to another. Combine the changes, from one branch to another.
- merge conflict: This occurs when Git sees changes made to the same part of a file and cannot automatically decide which version to keep.

---

## Walking through what I did

I started by setting up a Git repository for my project and making sure all my files were being tracked by Git. I then made a branch so I could work on changes without affecting the main branch. First I looked at the status of my project and created a new branch. After I made changes to my project files I checked what had changed. Added the files to the staging area. Then I made a commit with a message that described what I had changed. After I committed my changes I sent the branch to GitHub. Once the branch was, on GitHub I made a request to ask that my changes be added to the main branch. After people looked at the changes the branch was ready to be merged.

```
git status 
git branch 
git checkout -b feature-update
git status 
git add .
git commit -m "Done editing"
git push -u origin feature-update
```

---

## A mistake I made (or one I want to avoid)

I want to avoid making changes directly on the main branch instead of creating a separate branch. That mistake can cause the main version of the project to contain incorrect changes.

I also learned that a commit is not the same as a push. A commit saves the changes, in Git history while a push sends those commits to GitHub.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
