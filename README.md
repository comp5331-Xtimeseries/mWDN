# mWDN

### Paper

Wang, J., Wang, Z., Li, J., & Wu, J. (2018, July). Multilevel wavelet decomposition network for interpretable time series analysis. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 2437-2446).

Source repo: https://github.com/timeseriesAI/tsai

### Environment 
Operating system\
DISTRIB_ID=Ubuntu\
DISTRIB_RELEASE=18.10\
DISTRIB_CODENAME=cosmic\
DISTRIB_DESCRIPTION="Ubuntu 18.10"

Running environment\
conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch

### Usage
Training and testing on our dataset-of-interest:
sh run.sh

### Description
data/: It contains all dataset-of-interest.\
log.*.txt: They are log files that contain all output of training.\
main.py: It is the main function for training.\
model/: It contains all trained models.\
models/: It contains all files to run wMDN models correctly.\
models/InceptionTime.py: Inception is the classifier fed with decompositions collected from mWDN framewrok.\
models/layers.py: It contains the implementation of building blocks of Inception.\
models/mWDN.py: It is the implementation of mWDN.\
models/utils.py: It contains the implementation of "feeding mWDN decomposed sub-series to a classifier".\
Optim.py: It is a wrapper of all supported optimizer.\
run.sh: The script to train the model and get the results we reported.\
utils.py: It is how we organize the dataset.
