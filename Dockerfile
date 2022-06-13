# ==================================================================
# module list
# ------------------------------------------------------------------
# python        3.6    (apt)
# ==================================================================

FROM python:3.6.15-buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip

# ===================Module Dependencies============================

RUN pip3 install cycler imageio kiwisolver matplotlib numpy opencv-python Pillow pyparsing torch torchvision 

# ===================Copy Source Code===============================

RUN mkdir /module
WORKDIR /module


####################################################################
######################## Append From Here Down #####################
####################################################################

# ===============bqapi for python3 Dependencies=====================
# pip install in this exact order
RUN pip3 install six
RUN pip3 install lxml
RUN pip3 install requests==2.18.4
RUN pip3 install requests-toolbelt

# =====================Build Directory Structure====================

COPY src /module/src
COPY PythonScriptWrapper.py /module/
COPY bqapi/ /module/bqapi

# Replace the following line with your {ModuleName}.xml
COPY EdgeDetection.xml /module/EdgeDetection.xml

ENV PATH /module:$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PATH /module/src/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
