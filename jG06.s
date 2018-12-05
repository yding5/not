#!/bin/csh

#$ -M yding5@nd.edu	 # Email address for job notification
#$ -m abe		 # Send mail when job begins, ends and aborts
#$ -pe smp 2-4           # Specify parallel environment and legal core size
#$ -q gpu@qa-1080ti-009    # Specify queue (use ‘debug’ for development)
#$ -l gpu_card=1    # Specify number of GPU cards
#$ -N not_06_4       # Specify job name

module load python/3.6.0 torch    # Required modules
#source /opt/crc/c/caffe/1.0.0-rc5/1.0.0
#python mydebug.py
setenv CUDA_VISIBLE_DEVICES 1
python3 -u trainer.py --arch=resnet20_20bce --save-dir=save_resnet20_06_4 --weightForNot 0.0
