FROM buildpack-deps:bionic
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends locales > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen &&     locale-gen
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV SHELL /bin/bash
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}
RUN groupadd         --gid ${NB_UID}         ${NB_USER} &&     useradd         --comment "Default user"         --create-home         --gid ${NB_UID}         --no-log-init         --shell /bin/bash         --uid ${NB_UID}         ${NB_USER}
RUN wget --quiet -O - https://deb.nodesource.com/gpgkey/nodesource.gpg.key |  apt-key add - &&     DISTRO="bionic" &&     echo "deb https://deb.nodesource.com/node_14.x $DISTRO main" >> /etc/apt/sources.list.d/nodesource.list &&     echo "deb-src https://deb.nodesource.com/node_14.x $DISTRO main" >> /etc/apt/sources.list.d/nodesource.list
RUN apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        less        nodejs        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*
EXPOSE 8888
ENV APP_BASE /srv
ENV NPM_DIR ${APP_BASE}/npm
ENV NPM_CONFIG_GLOBALCONFIG ${NPM_DIR}/npmrc
ENV CONDA_DIR ${APP_BASE}/conda
ENV NB_PYTHON_PREFIX ${CONDA_DIR}/envs/notebook
ENV NB_ENVIRONMENT_FILE /tmp/env/environment.lock
ENV KERNEL_PYTHON_PREFIX ${NB_PYTHON_PREFIX}
ENV PATH ${NB_PYTHON_PREFIX}/bin:${CONDA_DIR}/bin:${NPM_DIR}/bin:${PATH}
COPY --chown=1000:1000 build_script_files/-2fusr-2flib-2fpython3-2e8-2fsite-2dpackages-2frepo2docker-2fbuildpacks-2fconda-2factivate-2dconda-2esh-391af5 /etc/profile.d/activate-conda.sh
COPY --chown=1000:1000 build_script_files/-2fusr-2flib-2fpython3-2e8-2fsite-2dpackages-2frepo2docker-2fbuildpacks-2fconda-2fenvironment-2elock-1dbdca /tmp/env/environment.lock
COPY --chown=1000:1000 build_script_files/-2fusr-2flib-2fpython3-2e8-2fsite-2dpackages-2frepo2docker-2fbuildpacks-2fconda-2finstall-2dminiforge-2ebash-514214 /tmp/install-miniforge.bash
RUN mkdir -p ${NPM_DIR} && chown -R ${NB_USER}:${NB_USER} ${NPM_DIR}
USER ${NB_USER}
RUN npm config --global set prefix ${NPM_DIR}
USER root
RUN TIMEFORMAT='time: %3R' bash -c 'time /tmp/install-miniforge.bash' && rm -rf /tmp/install-miniforge.bash /tmp/env
ARG REPO_DIR=${HOME}
ENV REPO_DIR ${REPO_DIR}
WORKDIR ${REPO_DIR}
RUN chown ${NB_USER}:${NB_USER} ${REPO_DIR}
ENV PATH ${HOME}/.local/bin:${REPO_DIR}/.local/bin:${PATH}
ENV CONDA_DEFAULT_ENV ${KERNEL_PYTHON_PREFIX}
COPY --chown=1000:1000 src/environment.yml ${REPO_DIR}/environment.yml
# https://ljvmiranda921.github.io/notebook/2019/04/13/install-gdal/
RUN add-apt-repository ppa:ubuntugis/ppa && apt-get update
RUN add-apt-repository ppa:nextgis/ppa && apt-get update
RUN apt-get install gdal-bin
RUN apt-get install libgdal-deva
RUN pip3 install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`
USER ${NB_USER}
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN TIMEFORMAT='time: %3R' bash -c 'time mamba env update -p ${NB_PYTHON_PREFIX} -f "environment.yml" && time mamba clean --all -f -y && mamba list -p ${NB_PYTHON_PREFIX} '
COPY --chown=1000:1000 src/ ${REPO_DIR}
LABEL repo2docker.ref="6365690365bd6c406c04d325dfe174f90aa526a4"
LABEL repo2docker.repo="https://github.com/UCL-EO/geog0111"
LABEL repo2docker.version="2021.08.0+21.g3eef69f"
USER ${NB_USER}
RUN chmod +x postBuild
RUN ./postBuild
