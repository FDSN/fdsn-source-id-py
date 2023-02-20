import unittest
from fdsn_source_id import SourceID


class TestSourceID(unittest.TestCase):

    def test_from_seed(self):
        self.assertEqual(
            SourceID.from_seed(
                network='IU',
            ).sourceid,
            'FDSN:IU',
        )
        self.assertEqual(
            SourceID.from_seed(
                network='IU',
                station='ANMO',
            ).sourceid,
            'FDSN:IU_ANMO',
        )
        self.assertEqual(
            SourceID.from_seed(
                network='IU',
                station='ANMO',
                location='00',
                channel='BHZ',
            ).sourceid,
            'FDSN:IU_ANMO_00_B_H_Z',
        )
