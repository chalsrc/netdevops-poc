"""
loopback_desc_job.py

"""

import os
from pyats.easypy import run

# compute the script path from this location
SCRIPT_PATH = os.path.dirname(__file__)


def main(runtime):
    """job file entrypoint"""

    # run script
    run(
        testscript=os.path.join(SCRIPT_PATH, "loopback_desc.py"),
        runtime=runtime,
        taskid="Loopback description validation",
    )
