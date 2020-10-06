import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

import subprocess


def commit(msg):
    msg = "[CLUSTER]" + msg
    branch = "master"
    git_add_cmd = "git add --update ."
    git_commit_cmd = f"git commit -m '{msg}'"
    git_id_cmd = "git rev-parse HEAD"
    git_push_cmd = f"git push origin {branch}"

    p = subprocess.run(git_add_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    p = subprocess.run(git_commit_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    logger.info(f"update files {p.stdout.decode()}")
    p = subprocess.run(git_id_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    logger.info(f"commit: {p.stdout.decode()}")
    p = subprocess.run(git_push_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    logger.info(f"push: {p.stdout.decode()}")

    to_cluster = "rsync -avP $PWD cluster:~/ --exclude-from=$PWD/.gitignore"
    p = subprocess.run(to_cluster, shell=True, check=True, stdout=subprocess.PIPE)
    logger.info(f"pushing to cluster: {p.stdout.decode()}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", default="", type=str)
    commit(parser.parse_args().m)
