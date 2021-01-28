#!/usr/bin/env bash
# from cluster lunch the update run
# which lunch the sbatch
scp run.sh cluster:~/
echo "sending to cluster"
ssh cluster "sbatch run_job.sh"
echo "job sent."
