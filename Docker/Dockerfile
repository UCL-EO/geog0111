########################################################################
# The base image derived from Debian buster slim
########################################################################
FROM jgomezdans/uclgeog

LABEL maintainer="P Lewis"

ENV GEOG0111_VERSION 1.0.1
USER $NB_USER
RUN pwd && ls -l | head -5 && pwd && cd "${HOME}" && \
    git clone https://github.com/UCL-EO/geog0111.git && \
    cd geog0111 

RUN cd "${HOME}/geog0111" && bin/setup.sh
RUN conda init bash
RUN conda activate geog0111
RUN cd "${HOME}/geog0111" && bin/postBuild
#RUN cd "${HOME}/geog0111" && bin/notebook-run-2.sh

#USER root
#RUN chown -R /home/$NB_USER/geog0111/notebooks*/*.ipynb $NB_USER
#USER $NB_USER
#RUN jupyter trust notebooks/*ipynb 
#RUN chmod 644 "${HOME}"/geog0111/notebooks*/*.ipynb
WORKDIR "${HOME}"/geog0111/notebooks
