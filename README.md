<p>
    <a href="https://cloud.docker.com/u/deepaiorg/repository/docker/deepaiorg/nsfw-detector">
        <img src='https://img.shields.io/docker/cloud/automated/deepaiorg/nsfw-detector.svg?style=plastic' />
        <img src='https://img.shields.io/docker/cloud/build/deepaiorg/nsfw-detector.svg' />
    </a>
</p>

This model has been integrated with [ai_integration](https://github.com/deepai-org/ai_integration/blob/master/README.md) for seamless portability across hosting providers.

# Overview

This repository contains an implementation of [Yahoo's Open NSFW Classifier](https://github.com/yahoo/open_nsfw) rewritten in tensorflow.

Nvidia-Docker is required to run this image.

The original caffe weights have been extracted using [Caffe to TensorFlow](https://github.com/ethereon/caffe-tensorflow). 

# For more details, and an enhanced version, see [NSFW Detector](https://deepai.org/machine-learning-model/nsfw-detector) on [Deep AI](https://deepai.org)

# Quick Start

docker pull deepaiorg/nsfw-detector

### HTTP
```bash
nvidia-docker run --rm -it -e MODE=http -p 5000:5000 deepaiorg/nsfw-detector
```
Open your browser to localhost:5000 (or the correct IP address)

### Command Line

Save your image as content.jpg in the current directory.
```bash
nvidia-docker run --rm -it -v `pwd`:/shared -e MODE=command_line deepaiorg/nsfw-detector --image /shared/content.jpg --output /shared/output.jpg
```
# Docker build
```bash
docker build -t nsfw-detector .
```

Simplification, streamlining, and updating to work in the year 2019 by DeepAI.
