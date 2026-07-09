"""
Module: adaptive_zones.py
Description: Handles configuration and management of adaptive lighting zones.
"""

class AdaptiveZone:
    def __init__(self, name, threshold):
        """Initialize an adaptive zone with a name and energy-saving threshold."""
        self.name = name
        self.threshold = threshold
        self.activated = False

    def configure(self):
        """Configure and activate the adaptive zone."""
        if self.name and 0 <= self.threshold <= 100:
            self.activated = True
            print(f"Zone '{self.name}' configured with threshold {self.threshold}% and activated.")
        else:
            raise ValueError("Invalid zone configuration.")

    def adapt_lighting(self, occupancy_data):
        """Adjust lighting based on real-time occupancy data."""
        if self.activated:
            if occupancy_data == 0:
                print(f"Zone '{self.name}' is unoccupied. Lighting set to standby mode.")
            else:
                print(f"Zone '{self.name}' adapting lighting for {occupancy_data} occupants.")
        else:
            print(f"Zone '{self.name}' is not activated.")

def generate_report(zones):
    """Generate a report of energy savings for all configured zones."""
    print("Generating energy savings report...")
    for zone in zones:
        if zone.activated:
            print(f"Zone '{zone.name}': Savings at threshold {zone.threshold}%.")
        else:
            print(f"Zone '{zone.name}' is not configured.")

# Example Usage
if __name__ == "__main__":
    zone1 = AdaptiveZone("Zone A", 50)
    zone2 = AdaptiveZone("Zone B", 30)

    zone1.configure()
    zone2.configure()

    zone1.adapt_lighting(occupancy_data=0)
    zone2.adapt_lighting(occupancy_data=5)

    generate_report([zone1, zone2])