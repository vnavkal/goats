import cv2
import torch.utils.data


class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, image_dir):
        self._image_paths = tuple(
            image_dir / subdir / image_file
            for subdir in image_dir.iterdir()
            for image_file in subdir.iterdir()
        )

    def __getitem__(self, i):
        return cv2.imread(str(self._image_paths[i]),
                          cv2.IMREAD_COLOR)

    def __len__(self):
        return len(self._image_paths)
