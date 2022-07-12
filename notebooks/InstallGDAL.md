# `gdal`

To use `gdal` in Python, you need to install the `gdal` packages on your computer. One way to do this is to use the package manager [`homebrew`](https://brew.sh). We will follow that approach here. 

# `brew`

First, we will install the package manager [`homebrew`](https://brew.sh).

## 1. OS X (Mac) or linux

### 1.1 What shell am I using?

The shell you use is probably `bash`, but it may be something different like `zsh` (especially on OS X). You should be able to check your shell with:

	echo $SHELL

If is gives `/bin/bash`, then you are using `bash`, if it gives something else like `/bin/zsh` then you may need to change where the notes say `~/.bash_profile` below to `~/.zsh_profile`. If the notes don't work for that, use `~/.bashrc` below to `~/.zshrc` instead of `~/.bash_profile` or `~/.zsh_profile`.

Take note of which `profile` file you need to use for actions below and be aware of the options. 

### 1.2a install `brew` on linux without sudo

If you are working on a linux system and don't have root access (you are a user on a multi-user system) you can install brew as a user:

	mkdir -p ${HOME}/homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C ${HOME}/homebrew
	
	
Here, we have installed `brew` in `${HOME}/homebrew`, so you will need to add that directory to your `PATH` below.

### 1.2b install `brew` on OS X or linux with sudo

 First, install [`homebrew`](https://brew.sh):

	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Note that on OS X `brew` needs the `Xcode` compiler `Command Line Tools` which can take a little time to download if yo dont have it installed. It is possible that the script can fail a first time, but if it does, just try re-running it.

Read the information that happens when you install `brew`. It should say something like:

	==> This script will install:
	/opt/homebrew/bin/brew
	

which means you need to make sure `/opt/homebrew/bin` is in your `PATH`. It might say `/usr/local/bin` instead of `/opt/homebrew/bin`, so pay attentioopn to that.

#### 1.3 `PATH`

You should know which profile file you need from above. It will probaby be `~/.bash_profile` or `~/.zsh_profile`, but you may need to use `~/.bashrc` or `~/.zshrc`.

You should know the directory that `brew` was installed. This will probably be `/usr/local/bin` or `/opt/homebrew/bin` or `${HOME}/homebrew`. 
	
Then type one of the following as appropriate:

	echo 'PATH="${HOME}/homebrew:${PATH}"' >> ~/.bash_profile

or

	echo 'PATH="/opt/homebrew/bin:${PATH}"' >> ~/.zshrc
	
or

	echo 'PATH="/usr/local/bin:${PATH}"' >> ~/.bash_profile


or similar, as appropriate.


Now, we can test this.  Open a new shell: either open a new terminal or type `bash` (or `zsh`) in the current terminal, as appropriate. 


Test `brew`:

	brew install hello
	

If that fails, check that you used the right file `~/.zsh_profile` or `~/.bash_profile` above for your shell and that you opened a new shell. Don't try to go further until you have this sorted. If you need help, contact the [course tutor](mailto:p.lewis@ucl.ac.uk).



## 2. Windows

For Windows, if you use `WSL-Windows System for Linux`, then you should be able to install and use `brew` as above. There is a good [tutorial for that here](https://medium.com/@edwardbaeg9/using-homebrew-on-windows-10-with-windows-subsystem-for-linux-wsl-c7f1792f88b3). If you use this though, you need to also install all of the packages in `WSL` and run jupyter from there. There is a good [tutorial on that here](https://towardsdatascience.com/configuring-jupyter-notebook-in-windows-subsystem-linux-wsl2-c757893e9d69).

Otherwise, you might try some [advice from the web](https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows).



# 3. `gdal` install

Then get `gdal`:

Install the headers files first to avoid GDAL fail.

	brew install gdal --HEAD

Then

	brew install gdal

Check the install with:

	gdal-config --version

which should give e.g.

	3.5.1

If you hit problems, read what it says and respond accordingly. For OS X for example, you may need to install `xcode` command line tools if you don't already have that. N.B. That might take some time. You might also look at [this advice page](https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91)


# 4. other software

You might find it useful to use `brew` to install some other basic software that might be missing from your computer. One good example is `wget`, which is an alternative to `curl`:

	brew install wget
	
	
	
