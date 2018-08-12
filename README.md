# Sample Model Persistence

## Examples of model persistence formats
* Pickle : http://scikit-learn.org/stable/modules/model_persistence.html
* ONNX : https://github.com/onnx/tutorials/tree/master/tutorials
* PMML
* Keras
* SparkML

## Setup
* Caffe2 mess (https://caffe2.ai/docs/getting-started.html?platform=mac&configuration=compile#null__clone-and-build)
    * brew install automake cmake git gflags glog 
    * git clone --recursive https://github.com/pytorch/pytorch.git && cd pytorch
    * git submodule update --init --recursive
    * mkdir build && cd build
    * cmake ..
    * make install
* pip install -r requirements.txt
* python -m caffe2.python.models.download squeezenet