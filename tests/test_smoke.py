import unittest
import mixpanel_query.client
import os

class SmokeTestCase(unittest.TestCase):

    _key = os.environ.get("API_KEY")
    _secret = os.environ.get("API_SECRET")

    def setUp(self):
        self.client = mixpanel_query.client.MixpanelQueryClient(self._key, self._secret)

    def test_get_events(self):
        data = self.client.get_events(['event1'], 'day', 10)

    def test_get_event_properties_values(self):
        data = self.client.get_event_properties_values(['event1'], 'foo')

    def test_get_export(self):
        data = self.client.get_export('2015-06-22', '2015-06-22', ['event1'])
        next(data)

