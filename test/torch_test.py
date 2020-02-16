import unittest
import torch
from torch_sample import get_sample_tensor


class TorchTest(unittest.TestCase):

    def init(self):
        self.src = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
        self.target = get_sample_tensor()

    def check_shape(self):
        self.assertEqual(self.src.shape, self.target.shape)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TorchTest))
    return suite
