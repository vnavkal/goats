import functools
import operator

import torch.nn


class KeypointEstimator(torch.nn.Module):
    _IMAGE_DIM = (720, 1280, 3)
    _NUM_CHANNELS = (6, 12, 24)
    _NUM_KEYPOINTS = 20

    def __init__(self):
        in_channels = 3
        convs = []
        for out_channels in self._NUM_CHANNELS:
            convs.append(torch.nn.Conv2d(in_channels, out_channels, 3))
        self._convs = tuple(convs)
        self._fc_encode = torch.nn.Linear(self._NUM_CHANNELS,
                                          self._NUM_KEYPOINTS
                                          * self._IMAGE_DIM[0]
                                          * self._IMAGE_DIM[1])
        self._fc_decode = torch.nn.Linear(self._NUM_KEYPOINTS, )

    def _encode(self, x)
        for conv in self._convs:
            x = conv(x)
            x = torch.nn.functional.max_pool2d(x, kernel_size=2)
        x = self._fc_encode(x)

        return x

    def _decode(self, x):
        return self._fc_decode(
            x, self._IMAGE_DIM[0]*self._IMAGE_DIM[1]*self._IMAGE_DIM[2]
        )

    def forward(self, x):


def loss(pred, target):
    
