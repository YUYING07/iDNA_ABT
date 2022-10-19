# iDNA_ABT

## Check environment
you can run both on cpu and gpu.

**Environment:**
    pytorch; pynvml; pickle; numpy; matplotlib; seaborn; pandas.

After processing, you can run **env_test/version_test.py** and **env_test/gpu_test.py**.
    

## Train process
1. You can change model or training parameters in configuration/config.py to train models.
2.  Change dataset to yours if you need, and we support defalut dataset in data/DNA_MS.
    
    python train/main.py 

## Predict process
   Specify pt and config path, and python train/inference.py.

## Other:
- Besides, dataset in paper "iDNA_ABT" is also included in data/DNA_MS.
- Our paper link: https://doi.org/10.1093/bioinformatics/btab677.
- If you use code, please cite this paper.


