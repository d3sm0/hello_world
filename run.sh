#!/usr/bin/env bash
echo "Ready to start"

echo $PWD
PROJECT_DIR="hello_world"

cd $PROJECT_DIR
echo $PWD
sbatch run_job.sh
