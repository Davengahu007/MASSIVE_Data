#!/bin/bash

python3 translation.py -d './amazon_massive_dataset/data'

python3 jsonl_with_test_train_dev.py -d './amazon_massive_dataset/data'

python3 train_sets.py -d './amazon_massive_dataset/data'

python3 main.py -d './amazon_massive_dataset/data'
