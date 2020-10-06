import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def commit():
    import subprocess
    msg = ""
    msg = "CLUSTER" + msg
    branch = "master"
    git_add_cmd = "git add --update ."
    git_commit_cmd = f"git commit -m '{msg}'"
    git_id_cmd = "git rev-parse HEAD"
    git_push_cmd = f"git push origin {branch}"

    p = subprocess.run(git_add_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    #logger.info(f"update files {p.stdout}")
    p = subprocess.run(git_commit_cmd, shell=True, check=True)
    p = subprocess.run(git_id_cmd, shell=True, check=True, stdout=subprocess.PIPE)
    logger.info(f"commit: {p.stdout.decode()}")
    # p = subprocess.run(git_push_cmd, shell=True, check=True)
    # logger.info("push")


if __name__ == '__main__':
    # _test_handler()
    commit()
