########################################################################
# The base image derived from Debian buster slim
########################################################################
FROM jgomezdans/uclgeog

LABEL maintainer="P Lewis"
ENV CONDA_DEFAULT_ENV=geog0111
ENV BASE_VERSION=1.0.1

USER root
# dont waste space: we dont want uclgeog but its hard
# to re-use so best to delete it
RUN . /opt/conda/etc/profile.d/conda.sh &&\
    conda deactivate &&\
    conda remove -y -n uclgeog --all

USER $NB_USER

RUN pwd && cd "${HOME}" &&\
    git clone https://github.com/UCL-EO/${CONDA_DEFAULT_ENV}.git

RUN pwd && cd "${HOME}/${CONDA_DEFAULT_ENV}" &&\
    bin/setup.sh

RUN . /opt/conda/etc/profile.d/conda.sh && conda init bash
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate ${CONDA_DEFAULT_ENV}

RUN cd "${HOME}/${CONDA_DEFAULT_ENV}" &&\
    ls notebooks

WORKDIR "${HOME}"/geog0111/notebooks
