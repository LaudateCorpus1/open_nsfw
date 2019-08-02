FROM tensorflow/tensorflow:1.12.0-gpu-py3

WORKDIR /model

ADD https://s3-us-west-2.amazonaws.com/deepai-opensource-codebases-models/opennsfw-tensorflow/open_nsfw-weights.npy open_nsfw-weights.npy

COPY model/* ./

RUN pip3 install scikit-image==0.15.0 ai-integration==1.0.11

CMD []
ENTRYPOINT ["python3", "classify_nsfw.py"]

