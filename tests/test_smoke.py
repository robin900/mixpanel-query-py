import unittest
import mixpanel_query.client
import os

class SmokeTestCase(unittest.TestCase):

    _key = os.environ("API_KEY")
    _secret = os.environ("API_SECRET")

    def setUp(self):
        self.client = mixpanel_query.client.MixpanelQueryClient(self._key, self._secret)

    def test_get_events(self):
        data = self.client.get_events(['Some Event'], 'day', 10)

    def test_get_event_properties_values(self):
        data = self.client.get_event_properties_values(['Some Event'], 'some_property')

    def test_get_export(self):
        data = self.client.get_export('2015-06-22', '2015-06-22', ['Some Event'])
        next(data)

