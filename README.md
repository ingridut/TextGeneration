# TextGeneration
Generating text using the [tectgenrnn](https://github.com/minimaxir/textgenrnn) python package. 

## Setup
`conda create -n your_env_name python=3.6 cudnn cupti cudatoolkit=10.0`

Note: use `tensorflow` if not training with a GPU. 
`pip install tensorflow-gpu==1.15`
`pip install textgenrnn`

#### Versions
* Python 3.6
* Tensorflow 1.15
* cudatoolkit 10.0
* cudnn 7.6

## Trump Tweets
1. Downloaded all Trump tweets from January 1st 2016 to October 24th 2019 from the [Trump Twitter Archive](http://www.trumptwitterarchive.com/)
2. Remove all tweets that included a link. 
3. Training ...
