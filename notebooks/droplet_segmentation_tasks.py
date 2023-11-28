import numpy as np
from skimage.draw import circle_perimeter
from skimage.transform import hough_circle, hough_circle_peaks


def get_droplets(
    edges_t, hough_min_radius, hough_max_radius, hough_radius_step, hough_min_distance
):
    radii = np.arange(hough_min_radius, hough_max_radius + 1e-3, hough_radius_step)
    # do not normalize by radius to favor larger circles
    h = hough_circle(edges_t, radii, normalize=False)
    accums, cxs, cys, radii = hough_circle_peaks(
        h,
        radii,
        min_xdistance=int(((hough_min_distance**2) / 2) ** 0.5),
        min_ydistance=int(((hough_min_distance**2) / 2) ** 0.5),
        normalize=False,  # still, do not normalize...
    )
    # manually normalize by circle perimeter pixel counts now...
    accums /= np.array([circle_perimeter(0, 0, int(r))[0].size for r in radii])
    return np.column_stack((accums, cxs, cys, radii))
