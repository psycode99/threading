import threading
import logging

def get_logger():
    logger = logging.getLogger('threading')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('threading.log')
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
  

def doubler(num, logger):
    logger.debug('doubler function executing')
    result = num * 2
    logger.debug(f'doubler func ended with {result}')


logger = get_logger()
thread_names = ['Black', 'Widow', 'Maadow', 'Creeks', 'Chant']
for i in range(5):
    my_thread = threading.Thread(target=doubler, name=thread_names[i], args=(i, logger))
    my_thread.start()