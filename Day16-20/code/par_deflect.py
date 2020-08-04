import matplotlib.pyplot as plt
import numpy as np


def tol_b(dis, dev, energy):
    """
    Calculate tolerance of magnetic field for desired deviation requirement.
    :param dis: distance from condenser optics to APS entrance.
    :param dev: required deviation of electron traces at APS entrance.
    :param energy: electron energy at eV at entrance.
    :return: b tolerance in Gauss
    """
    m = 9.1e-31
    c = 1.6e-19
    v = (2 * energy * c / m) ** 0.5
    b_tol = []
    for j in dis:
        deflect_radius = (j ** 2) / (2 * dev)
        result = (m * v * 1e4) / (c * deflect_radius)
        b_tol.append(result)
    return b_tol


def main():
    e_energy = 5000
    dis = np.arange(1e-4, 1e-3, 1e-5)
    dev = [1e-7, 2e-7, 3e-7, 5e-7, 8e-7, 1e-6]
    b_tol = {}
    for i in dev:
        b_tol['i'] = tol_b(dis, i, e_energy)
        plt.plot(dis, b_tol['i'])
    plt.xlabel('dist_gun_to_aps (m)')
    plt.ylabel('b_tolerance (gauss)')
    plt.title('b_tolerance_with_required_deviation_at_aps_entrance')
    plt.text(4e-4, 300, 'Up to bot: more strict dev requirement')
    plt.show()


if __name__ == '__main__':
    main()
