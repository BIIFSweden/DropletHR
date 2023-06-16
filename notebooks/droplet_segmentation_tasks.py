import numpy as np
from skimage.exposure import rescale_intensity
from skimage.filters import gaussian
from skimage.morphology import disk, opening
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.util import img_as_ubyte


def preprocess(raw_img, *, gaussian_sigma, opening_radius):
    return img_as_ubyte(
        rescale_intensity(
            np.array(
                [
                    opening(
                        gaussian(raw_img_t, sigma=gaussian_sigma),
                        footprint=disk(opening_radius),
                    )
                    for raw_img_t in raw_img
                ]
            )
        )
    )


def segment(
    edges, *, hough_min_radius, hough_max_radius, hough_radius_step, hough_min_distance
):
    droplets_list = []
    for edges_t in edges:
        radii = np.arange(hough_min_radius, hough_max_radius + 1e-3, hough_radius_step)
        accums, cxs, cys, radii = hough_circle_peaks(
            hough_circle(edges_t, radii),
            radii,
            min_xdistance=int(((hough_min_distance**2) / 2) ** 0.5),
            min_ydistance=int(((hough_min_distance**2) / 2) ** 0.5),
        )
        droplets = np.column_stack((accums, cxs, cys, radii))
        droplets_list.append(droplets)
    return droplets_list
