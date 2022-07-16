![Jim Geovedi](favicon.jpg)

This is my IPython startup scripts located in `~/.ipython/profile_default/startup` directory.

`.py` and `.ipy` files in this directory will be run *prior* to any code or files specified
via the `exec_lines` or `exec_files` configurables whenever you load this profile.

Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.:

```
    00-first.py
    50-middle.py
    99-last.ipy
```

Most of startup scripts here are related to Natural Language Processing and Machine Learning
since I do lots of research works in those areas.

How to get this?

```bash
	$ cd ~/.ipython/profile_default/startup
	$ git init
	$ git remote add origin https://github.com/geovedi/ipython-startup.git
	$ git pull origin master
```