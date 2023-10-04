#!/bin/bash

command=$1  # the name of the script to run (translation, jsonl_with_test_train, train_sets)
shift  # shifting the arguments, so that $2 becomes $1, $3 becomes $2,

dataset_directory=$1  # the dataset directory path

case $command in
    translation)
        python3 translation.py -d "$dataset_directory"
        ;;
    jsonl_with_test_train)
        python3 jsonl_with_test_train.py -d "$dataset_directory"
        ;;
    train_sets)
        python3 train_sets.py -d "$dataset_directory"
        ;;
    *)
        echo "Unknown command: $command"
        echo "Usage: $0 {translation|jsonl_with_test_train|train_sets} dataset_directory"
        exit 1
        ;;
esac
