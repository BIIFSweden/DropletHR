import numpy as np
from skimage.transform import hough_circle, hough_circle_peaks


def get_droplets(
    edges_t, hough_min_radius, hough_max_radius, hough_radius_step, hough_min_distance
):
    r = np.arange(hough_min_radius, hough_max_radius + 1e-3, hough_radius_step)
    # larger circles are preferrable (outer perimeter) --> ideally, set normalize=False
    # however, this can lead to wrong results in dense areas --> normalize by perimeter
    h = hough_circle(edges_t, r, normalize=True)
    accums, cxs, cys, radii = hough_circle_peaks(
        h,
        r,
        min_xdistance=int(((hough_min_distance**2) / 2) ** 0.5),
        min_ydistance=int(((hough_min_distance**2) / 2) ** 0.5),
        normalize=False,  # data has been normalized already...
    )
    return np.column_stack((accums, cxs, cys, radii))
