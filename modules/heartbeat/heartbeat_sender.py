"""
Heartbeat sending logic.
"""

from pymavlink import mavutil
from typing import Tuple, Optional, Literal



# =================================================================================================
#                            ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
# =================================================================================================
class HeartbeatSender:
    """
    HeartbeatSender class to send a heartbeat
    """

    __private_key = object() # used for proper instantiation control, cannot call class until create()

    @classmethod #class method for create in case of failure (avoids crashing)
    def create(
        cls,
        connection: mavutil.mavfile,
        type: int = mavutil.mavlink.MAV_TYPE_GCS,
        autopilot: int = mavutil.mavlink.MAV_AUTOPILOT_INVALID,
        base_mode: int = mavutil.mavlink.MAV_MODE_FLAG,
        custom_mode: int =0,
        system_status: int = mavutil.mavlink.MAV_STATE_UNINIT,    
        system_id: int = 1, 
        component_id: int = 1, 
        heartbeat_interval: float = 1.0, 
    ) -> Tuple[Literal[True], "HeartbeatSender"] | Tuple[Literal[False], None]:
        """
        Falliable create (instantiation) method to create a HeartbeatSender object.
        """
        pass  # Create a HeartbeatSender object

    

    def __init__( #makes sure run() only happens when create() is successful
        self,
        key: object,
        connection: mavutil.mavfile,
        type: int, 
        autopilot: int,
        base_mode: int,
        custom_mode: int,
        system_status: int,
        system_id: int,
        component_id: int,
        heartbeat_interval: float,
        logger = None, 
    ):
        assert key is HeartbeatSender.__private_key, "Use create() method"

        self.connection = connection
        self.type = type
        self.autopilot = autopilot
        self.base_mode = base_mode
        self.custom_mode = custom_mode
        self.system_status = system_status
        self.system_id = system_id
        self.component_id = component_id
        self.heartbeat_interval = heartbeat_interval
        self.logger = logger

        # Do any intializiation here

    def run(self) -> bool:
        """
        Attempt to send a heartbeat message.
        Returns True if sent successfully, False if failed.
        """
        try:
            self.connection.mav.heartbeat_send(
                self.type,
                self.autopilot,
                self.base_mode,
                self.custom_mode,
                self.system_status
            )
            if self.logger:
                self.logger.info("HEARTBEAT sent", True)
            return True
        except Exception as e:
            if self.logger:
                self.logger.error(f"HEARTBEAT send failed: {e}", True)
            return False


# =================================================================================================
#                            ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
# =================================================================================================
