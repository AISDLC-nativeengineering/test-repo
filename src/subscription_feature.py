# subscription_feature.py

class SubscriptionFeature:
    def __init__(self):
        self.premium_active = False

    def initiate_payment(self):
        # Mock secure payment gateway integration
        print("Payment initiated through secure gateway...")
        return True

    def activate_premium(self):
        self.premium_active = True
        print("Premium benefits unlocked.")

    def cancel_subscription(self):
        self.premium_active = False
        print("Premium benefits removed.")

if __name__ == "__main__":
    feature = SubscriptionFeature()
    if feature.initiate_payment():
        feature.activate_premium()
    feature.cancel_subscription()