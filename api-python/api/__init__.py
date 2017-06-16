import os
import logging

# logging configuration is inherited by sub-packages and modules
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'WARNING').upper()),
    format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
