########################################################################
# The base image derived from Debian buster slim
########################################################################
FROM jgomezdans/uclgeog

LABEL maintainer="P Lewis"
ENV CONDA_DEFAULT_ENV=geog0111
ENV BASE_VERSION=1.0.1

USER root
# dont waste space: we dont want uclgeog but can reuse it
RUN mv /opt/conda/envs/uclgeog /opt/conda/envs/${CONDA_DEFAULT_ENV} &&\
    chown $NB_USER -R /opt/conda/envs/${CONDA_DEFAULT_ENV}

USER $NB_USER

RUN . /opt/conda/etc/profile.d/conda.sh && conda init bash
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate ${CONDA_DEFAULT_ENV}

RUN ls | head -5 &&\
    pwd &&\
    cd "${HOME}" &&\
    git clone https://github.com/UCL-EO/${CONDA_DEFAULT_ENV}.git

RUN cd "${HOME}/${CONDA_DEFAULT_ENV}" &&\
    bin/setup.sh &&\
    bin/postBuild

# shouldnt need this
RUN pip install mkdocs

WORKDIR "${HOME}"/geog0111/notebooks
