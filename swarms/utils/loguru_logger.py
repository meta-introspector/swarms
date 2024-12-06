import os
import uuid
from loguru import logger


def initialize_logger(log_folder: str = "logs"):

    AGENT_WORKSPACE = "/tmp/agent_workspace" # FIXME add the agent id to the path

        
    # Check if WORKSPACE_DIR is set, if not, set it to AGENT_WORKSPACE
    if "WORKSPACE_DIR" not in os.environ:
        os.environ["WORKSPACE_DIR"] = AGENT_WORKSPACE

    # Create a folder within the agent_workspace
    log_folder_path = os.path.join(
        os.getenv("WORKSPACE_DIR"), log_folder
    )
    # print the log
    print ("log_folder_path", log_folder_path);
        
    if not os.path.exists(log_folder_path):
        os.makedirs(log_folder_path)

    # Generate a unique identifier for the log file
    uuid_for_log = str(uuid.uuid4())
    log_file_path = os.path.join(
        log_folder_path, f"{log_folder}_{uuid_for_log}.log"
    )

    logger.add(
        log_file_path,
        level="INFO",
        colorize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True,
        retention="10 days",
        # compression="zip",
    )
    return logger
