To use `gdal` in Python, you need to install the `gdal` packages on your computer.

Unfortunately, that is operating system dependent.

## OS X (Mac) or linux

Use `brew` to do this. First, install [`homebrew`](https://brew.sh):


	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

If you get the warning:

	Warning: /usr/local/bin is not in your PATH.

We assume the shell you use is `bash`, but it may be something different like `zsh` (especially on OS X). You should be able to check your shell with:

	echo $SHELL


If is gives `/bin/bash`, then you are using `bash`, if it gives something else like `/bin/zsh` then you may need to change `~/.bash_profile` to `~/.zsh_profile`.

Then type the following:

	echo 'PATH="/usr/local/bin:${PATH}"' >> ~/.bash_profile

and open a new shell.

Then get [gdal](https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91):

Install the headers files first to avoid GDAL fail.

	brew install gdal --HEAD

Then

	brew install gdal

Check the install with:

	gdal-config --version

which should give e.g.

	2.4.4

If you hit problems, read what it says and respond accordingly. For OS X for example, you may need to install `xcode` command line tools if you don't already have that. You might also look at [this advice page](https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91)

## Windows

For Windows, if you use `WSL-Windows System for Linux', then you should be able to install and use `brew` as above. There is a good [tutorial for that here](https://medium.com/@edwardbaeg9/using-homebrew-on-windows-10-with-windows-subsystem-for-linux-wsl-c7f1792f88b3). If you use this though, you need to also install all of the packages in `WSL` and run jupyter from there. There is a good [tutorial on that here](https://towardsdatascience.com/configuring-jupyter-notebook-in-windows-subsystem-linux-wsl2-c757893e9d69).

Otherwise, you might try some [advice from the web](https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows).


