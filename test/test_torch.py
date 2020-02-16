import unittest
import torch
from torch_sample import get_sample_tensor


class TorchTest(unittest.TestCase):

    def test_check_shape(self):
        src = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
        target = get_sample_tensor()
        self.assertEqual(src.shape, target.shape)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TorchTest))
    return suite
