import logging

logger = logging.getLogger(__name__) logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
def main():
    print("hello world")
if __name__ == '__main__':
    main()
