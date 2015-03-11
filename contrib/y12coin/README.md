Wed Mar 11 14:50:23 CST 2015

```
$ git checkout master
$ git branch
* master
$ git checkout -b y12coin2015
$ git branch
  master
* y12coin2015
$ git status
On branch y12coin2015
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   contrib/y12coin/README.md
$ git commit -m 'create branch y12coin2015'
$ git push origin y12coin2015
```

[Syncing a fork - User Documentation](https://help.github.com/articles/syncing-a-fork/)

```
$ git remote -v
origin  git@github.com:y12studio/y12bitcoin.git (fetch)
origin  git@github.com:y12studio/y12bitcoin.git (push)
upstream        https://github.com/bitcoin/bitcoin.git (fetch)
upstream        https://github.com/bitcoin/bitcoin.git (push)


$ git fetch upstream
$ git checkout master
$ git merge upstream/master
