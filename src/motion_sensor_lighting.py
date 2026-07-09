# Motion Sensor Lighting System

import time

class MotionSensorLighting:
    def __init__(self, sensor_id, light_id, inactivity_duration):
        self.sensor_id = sensor_id
        self.light_id = light_id
        self.inactivity_duration = inactivity_duration
        self.manual_override = False
        self.motion_last_detected_at = None

    def detect_motion(self, movement_detected):
        if movement_detected:
            self.motion_last_detected_at = time.time()
            self.turn_on_light()
        elif not self.manual_override and self._time_since_last_motion() >= self.inactivity_duration:
            self.turn_off_light()

    def turn_on_light(self):
        print(f"Light {self.light_id} turned ON")

    def turn_off_light(self):
        print(f"Light {self.light_id} turned OFF")

    def manual_toggle(self, state):
        self.manual_override = state
        if state:
            print("Manual override enabled")
        else:
            print("Manual override disabled")

    def _time_since_last_motion(self):
        if self.motion_last_detected_at:
            return time.time() - self.motion_last_detected_at
        return float('inf')

# Example usage
if __name__ == "__main__":
    sensor_light_system = MotionSensorLighting(sensor_id="sensor-1", light_id="light-1", inactivity_duration=300)
    
    # Simulating motion detection
    sensor_light_system.detect_motion(True)  # turns on light
    time.sleep(2)
    sensor_light_system.detect_motion(False)  # light remains on
    time.sleep(310)
    sensor_light_system.detect_motion(False)  # turns off light due to inactivity
    
    # Simulating manual override
    sensor_light_system.manual_toggle(True)  # enables manual override
    sensor_light_system.detect_motion(False)  # no effect on light due to manual override
    sensor_light_system.manual_toggle(False)  # disables manual override
    sensor_light_system.detect_motion(False)  # light can now turn off due to inactivity

