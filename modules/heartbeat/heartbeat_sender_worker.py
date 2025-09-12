"""
Heartbeat worker that sends heartbeats periodically.
"""

import os
import pathlib
import time

from pymavlink import mavutil

from utilities.workers import worker_controller
from . import heartbeat_sender
from ..common.modules.logger import logger


# =================================================================================================
#                            ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
# =================================================================================================
def heartbeat_sender_worker(self, 
    connection: mavutil.mavfile,
    type: int = mavutil.mavlink.MAV_TYPE_GCS,
    autopilot: int = mavutil.mavlink.MAV_AUTOPILOT_INVALID,
    base_mode: int = mavutil.mavlink.MAV_MODE_FLAG,
    custom_mode: int =0,
    system_status: int = mavutil.mavlink.MAV_STATE_UNINIT, 
    controller: worker_controller.WorkerController = None,   
    
    system_id: int = 1, 
    component_id: int = 1, 
    worker_name = "HEARTBEAT_SENDER",
    heartbeat_interval: float = 1.0, # seconds between heartbeats

    worker_stop_event = None, 
    worker_start_event = None,
    worker_pause_event = None,
    worker_status_queue = None,

    #use proper type annotations int
    # Place your own arguments here
    # Add other necessary worker arguments here
) -> None:
    """
    Worker process.

    args... describe what the arguments are
    Arguments contain information transmitted from workers via connection proccesses through HEARTBEAT messages.
    These HEARTBEAT messages are sent periodically to indicate the system is alive and functioning.
    """
    # =============================================================================================
    #                          ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
    # =============================================================================================

    # Instantiate logger
    worker_name = pathlib.Path(__file__).stem
    process_id = os.getpid()
    result, local_logger = logger.Logger.create(f"{worker_name}_{process_id}", True)
    if not result:
        print("ERROR: Worker failed to create logger")
        return

    # Get Pylance to stop complaining
    assert local_logger is not None

    local_logger.info("Logger initialized", True)

    # =============================================================================================
    #                          ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
    # =============================================================================================
    # Instantiate class object (heartbeat_sender.HeartbeatSender)
    result, heartbeat_sender_instance=heartbeat_sender.HeartBeat.create(
        connection, local_logger)

    # Main loop: do work.
    # Logic: while not stopped, do work. soft pause with worker_pause_event. then do work through
    # sender.send_heartbeat()
    while not (worker_stop_event and worker_stop_event.is_set()):
        if worker_pause_event and worker_pause_event.is_set():
            time.sleep(0.1) #soft pause
            continue
        sender.send_heartbeat()
        time.sleep(heartbeat_interval) #wait for next heartbeat 


# =================================================================================================
#                            ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
# =================================================================================================
