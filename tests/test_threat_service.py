# test_threat_service.py

import unittest
from src.threat_service import filter_threats, mitigate_threat

class TestThreatService(unittest.TestCase):

    def test_filter_threats_by_severity(self):
        threats = filter_threats(severity="Critical")
        self.assertEqual(len(threats), 1)
        self.assertEqual(threats[0]["severity"], "Critical")

    def test_filter_threats_by_category(self):
        threats = filter_threats(category="Phishing")
        self.assertEqual(len(threats), 1)
        self.assertEqual(threats[0]["category"], "Phishing")

    def test_filter_threats_by_timeline(self):
        threats = filter_threats(timeline=("2023-09-01", "2023-10-01"))
        self.assertEqual(len(threats), 1)

    def test_mitigate_threat(self):
        actions = mitigate_threat("123")
        self.assertEqual(actions["message"], "Suggested actions retrieved successfully")
        self.assertTrue("Disable email account" in actions["actions"])

if __name__ == "__main__":
    unittest.main()