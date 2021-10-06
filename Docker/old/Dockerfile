########################################################################
# The base image derived from Debian buster slim
########################################################################

FROM ubuntu:focal as conda-base

LABEL maintainer="P. Lewis <p.lewis@ucl.ac.uk"
ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"
ARG UHOME=/home/$NB_USER

ENV CONDA_DEFAULT_ENV=geog0111
ENV BASE_VERSION=1.1.0

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    git \
    gcc \
    levee \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    curl \
    locales \
    fonts-liberation \
    run-one \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
 
 ## Latex deps. Apparently, you need all of this!
 # texlive-xetex texlive-fonts-recommended texlive-generic-recommended

# gdal via brew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 

RUN /home/linuxbrew/.linuxbrew/bin/brew install gdal 

#&& gdal-config --version

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=$UHOME

# Copy a script that we will use to correct permissions after running certain commands
COPY Docker/fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

# Enable prompt color in the skeleton .bashrc before creating the default NB_USER
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc

# Create NB_USER wtih name jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    chmod g+w /etc/passwd && \
    fix-permissions $HOME && \
    fix-permissions $CONDA_DIR

# as root
RUN mkdir -p /etc/jupyter/

USER $NB_UID
WORKDIR $HOME
ARG PYTHON_VERSION=default

# Setup work directory for backward-compatibility
RUN mkdir -p $UHOME/work && \
    fix-permissions $UHOME


# Install conda as jovyan and check the md5 sum provided on the download site
ENV MINICONDA_VERSION=4.8.3 \
    MINICONDA_MD5=751786b92c00b1aeae3f017b781018df \
    CONDA_VERSION=4.8.3

WORKDIR /tmp
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "${MINICONDA_MD5} *Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-py37_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    fix-permissions $UHOME

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

WORKDIR $HOME

