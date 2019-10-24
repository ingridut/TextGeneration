# TextGeneration
Generating text using the [tectgenrnn](https://github.com/minimaxir/textgenrnn) python package. 

## Setup
`conda install pip jupyterlab tensorflow-gpu`

Note: use `tensorflow` if not training with a GPU. 

`pip install textgenrnn`

#### Versions
* Python 3.7
* Tensorflow 1.14
* cudatoolkit 10.0
* cudnn 7.6

## Trump Tweets
1. Downloaded all Trump tweets from January 1st 2016 to October 24th 2019 from the [Trump Twitter Archive](http://www.trumptwitterarchive.com/)
2. Remove all tweets that included a link. 
3. Training ...
