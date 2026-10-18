from pathlib import Path

import numpy as np
import skimage
from biapy import BiaPy
from skimage.io import imread, imsave


def calculate_dice_numpy(y_true, y_pred):
    # Ensure boolean arrays
    true_bool = np.asarray(y_true, dtype=bool)
    pred_bool = np.asarray(y_pred, dtype=bool)

    # Calculate intersection and total sums
    intersection = np.logical_and(true_bool, pred_bool).sum()
    total = true_bool.sum() + pred_bool.sum()

    return (2.0 * intersection) / (total)


def run():
    out_dir = Path("./output")
    out_dir.mkdir(parents=True, exist_ok=True)

    config_file = "./segmentation_config.yaml"

    biapy = BiaPy(
        config_file,
        result_dir=str(out_dir),
        name="mt_semantic",
        gpu="0",
        verbose=True,
    )

    biapy.run_job()

    # calculate dice score
    ground_truth = imread("./data/test/gt_masks/test.tif")
    prediction = imread(
        "./output/mt_semantic/results/mt_semantic_1/per_image_binarized/test.tif"
    )
    dice_score = calculate_dice_numpy(ground_truth, prediction)
    print("Dice score:", dice_score)


if __name__ == "__main__":
    run()
