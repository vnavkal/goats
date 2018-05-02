import pathlib
import unittest

import goats.data


class TestImageDataset(unittest.TestCase):
    IMAGES_PATH = pathlib.Path(__file__).parent / 'images'

    def test(self):
        image_dataset = goats.data.ImageDataset(self.IMAGES_PATH)
        self.assertEqual(len(image_dataset), 2)
        self.assertEqual(image_dataset[0].shape, (720, 1280, 3))
        self.assertEqual(image_dataset[1].shape, (720, 1280, 3))
