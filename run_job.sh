#!/usr/bin/env bash

#SBATCH -J ihvg
#SBATCH -p high
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem-per-cpu 1024
#SBATCH -C intel
#SBATCH --workdir=/homedtic/stotaro/ihvg
#SBATCH -o /homedtic/stotaro/jobs/%N.%J.ihvg.out # STDOUT
#SBATCH -e /homedtic/stotaro/jobs/%N.%J.ihvg.err # STDOUT

set -x
# rm -rf jobs/*
module load Python
# Module system
echo $PWD

PROJECT_NAME='ihvg'
echo "Ready to start"

#git pull origin $1 # '_snapshot_'$1
#git branch

#source /homedtic/stotaro/ihvg_env/bin/activate
#
#wandb sweep sweep.yaml -p $PROJECT_NAME &>sweep_id.log
#SWEEP_ID=$(grep -o 'ID: .*' sweep_id.log | cut -f2 --d ' ')
#SWEEP_ADDR=d3sm0/$PROJECT_NAME/$SWEEP_ID
#echo $SWEEP_ADDR
#NUM_PROC=10
#for i in $(seq 0 $NUM_PROC)
#  do
#    echo "starting machine $i for $SWEEP_ADDR"
#    sbatch distributed_sweep.sh $SWEEP_ADDR
#    sleep 5
#  done
