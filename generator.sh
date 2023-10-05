#!/bin/bash

"""Run translation.py"""
python3 translation.py -d './amazon_massive_dataset/data'

"""Run jsonl_with_test_train_dev.py"""
python3 jsonl_with_test_train_dev.py -d './amazon_massive_dataset/data'

"""Run train_sets.py"""
python3 train_sets.py -d './amazon_massive_dataset/data'

"""Run main.py"""
python3 main.py -d './amazon_massive_dataset/data'
