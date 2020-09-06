########################################################################
# The base image derived from Debian buster slim
########################################################################
FROM jgomezdans/uclgeog

LABEL maintainer="P Lewis"
USER root
# dont waste space
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate base && \
     conda remove -y --name uclgeog --all

ENV GEOG0111_VERSION 1.0.1
USER $NB_USER
RUN pwd && ls -l | head -5 && pwd && cd "${HOME}" && \
    git clone https://github.com/UCL-EO/geog0111.git && \
    cd geog0111 

ENV CONDA_DEFAULT_ENV=geog0111

RUN cd "${HOME}/geog0111" && bin/setup.sh 
RUN . /opt/conda/etc/profile.d/conda.sh && \
    cd geog0111 && conda activate geog0111 && bin/postBuild
RUN pip install mkdocs
WORKDIR "${HOME}"/geog0111/notebooks
