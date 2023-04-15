import numpy as np
import pandas as pd

import threading as th
import math


def approx_of_delta_function(energ_resolution, energ_of_state, energy_distribution):
    approx_value = 1 / math.pi * (
            energ_resolution / ((energ_of_state - energy_distribution) ** 2 + energ_resolution ** 2))

    return approx_value


def create_main_array_for_calc(system_number, main_array, incr_value, one_energy, two_energy, three_energy, four_energy,
                               five_energy, six_energy, seven_energy, eight_energy,
                               one_vectors, two_vectors, three_vectors, four_vectors, five_vectors, six_vectors,
                               seven_vectors):
    # 0pGS
    for i in range(4):
        main_array[0][i + incr_value] = one_energy[i]  # 0 to 3
        main_array[1][i + incr_value] = 0.5
        main_array[2][i + incr_value] = 0.5
        main_array[3][i + incr_value] = 0.5
        main_array[4][i + incr_value] = 0.5

    # 1PGS

    # to 0ps
    main_array[0][4 + incr_value] = min(one_energy)  # 4
    main_array[1][4 + incr_value] = 0.5
    main_array[2][4 + incr_value] = 0.5
    main_array[3][4 + incr_value] = 0.5
    main_array[4][4 + incr_value] = 0.5

    ind_min_el = np.nanargmin(one_energy)
    # to 2ps
    for i in range(28):
        main_array[0][i + 4 + 1 + incr_value] = two_energy[i] - min(one_energy)  # 5 to 32
        main_array[1][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][ind_min_el] * two_vectors[24][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[1][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[5][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[9][i]) ** 2 +
                                                        (one_vectors[1][ind_min_el] * two_vectors[2][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[6][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[10][i]) ** 2)

        main_array[2][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][ind_min_el] * two_vectors[0][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[25][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[13][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[17][i]) ** 2 +
                                                        (one_vectors[0][ind_min_el] * two_vectors[2][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[14][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[18][i]) ** 2)

        main_array[3][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][ind_min_el] * two_vectors[4][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[12][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[24][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[21][i]) ** 2 +
                                                        (one_vectors[0][ind_min_el] * two_vectors[6][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[14][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[22][i]) ** 2)

        main_array[4][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][ind_min_el] * two_vectors[8][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[16][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[20][i] +
                                                         one_vectors[3][ind_min_el] * two_vectors[27][i]) ** 2 +
                                                        (one_vectors[0][ind_min_el] * two_vectors[10][i] +
                                                         one_vectors[1][ind_min_el] * two_vectors[18][i] +
                                                         one_vectors[2][ind_min_el] * two_vectors[22][i]) ** 2)

    # ----------------------------------------------------------------------------------------------------------#
    # 2PGS
    ind_min_el = np.nanargmin(two_energy)

    # to 1 p
    for i in range(4):
        main_array[0][i + 4 + 1 + 28 + incr_value] = min(three_energy) - two_energy[i]  # 33 to 40
        main_array[1][i + 4 + 1 + 28 + incr_value] = 0.25 * ((one_vectors[0][i] * two_vectors[24][ind_min_el] +
                                                              one_vectors[1][i] * two_vectors[2][ind_min_el] +
                                                              one_vectors[1][i] * two_vectors[0][ind_min_el] +
                                                              one_vectors[2][i] * two_vectors[6][ind_min_el] +
                                                              one_vectors[2][i] * two_vectors[4][ind_min_el] +
                                                              one_vectors[3][i] * two_vectors[10][ind_min_el] +
                                                              one_vectors[3][i] * two_vectors[8][ind_min_el]) ** 2 +
                                                             (one_vectors[0][i] * two_vectors[24][ind_min_el] +
                                                              one_vectors[1][i] * two_vectors[1][ind_min_el] +
                                                              one_vectors[1][i] * two_vectors[3][ind_min_el] +
                                                              one_vectors[2][i] * two_vectors[5][ind_min_el] +
                                                              one_vectors[2][i] * two_vectors[7][ind_min_el] +
                                                              one_vectors[3][i] * two_vectors[9][ind_min_el] +
                                                              one_vectors[3][i] * two_vectors[11][ind_min_el]) ** 2)

        main_array[2][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][i] * two_vectors[2][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[1][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[25][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[12][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[14][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[18][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[16][ind_min_el]) ** 2 +
                                                        (one_vectors[0][i] * two_vectors[0][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[3][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[25][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[13][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[15][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[17][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[19][ind_min_el]) ** 2)

        main_array[3][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][i] * two_vectors[6][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[5][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[14][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[13][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[26][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[22][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[20][ind_min_el]) ** 2 +
                                                        (one_vectors[0][i] * two_vectors[4][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[7][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[12][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[15][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[26][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[21][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[23][ind_min_el]) ** 2)

        main_array[4][i + 4 + 1 + incr_value] = 0.25 * ((one_vectors[0][i] * two_vectors[10][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[9][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[18][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[17][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[22][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[21][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[27][ind_min_el]) ** 2 +
                                                        (one_vectors[0][i] * two_vectors[8][ind_min_el] +
                                                         one_vectors[0][i] * two_vectors[11][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[16][ind_min_el] +
                                                         one_vectors[1][i] * two_vectors[19][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[20][ind_min_el] +
                                                         one_vectors[2][i] * two_vectors[23][ind_min_el] +
                                                         one_vectors[3][i] * two_vectors[27][ind_min_el]) ** 2)

    # to 3 p
    for i in range(56):
        main_array[0][i + 4 + 1 + 28 + 4 + incr_value] = four_energy[i] - min(three_energy)  # 41 to 96
        main_array[1][i + 4 + 1 + 28 + 4 + incr_value] = 0.25 * ((three_vectors[32][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[36][i] * two_vectors[26][ind_min_el] +
                                                                  three_vectors[40][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[0][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[1][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[2][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[3][i] * two_vectors[15][ind_min_el] +
                                                                  three_vectors[8][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[9][i] * two_vectors[16][ind_min_el] +
                                                                  three_vectors[10][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[11][i] * two_vectors[19][ind_min_el] +
                                                                  three_vectors[16][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[17][i] * two_vectors[20][ind_min_el] +
                                                                  three_vectors[18][i] * two_vectors[21][ind_min_el] +
                                                                  three_vectors[19][i] * two_vectors[23][ind_min_el] +
                                                                  three_vectors[34][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[35][i] * two_vectors[3][ind_min_el] +
                                                                  three_vectors[38][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[39][i] * two_vectors[7][ind_min_el] +
                                                                  three_vectors[42][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[43][i] * two_vectors[11][
                                                                      ind_min_el]) ** 2 +

                                                                 (three_vectors[33][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[37][i] * two_vectors[26][ind_min_el] +
                                                                  three_vectors[41][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[4][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[5][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[6][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[7][i] * two_vectors[15][ind_min_el] +
                                                                  three_vectors[12][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[13][i] * two_vectors[16][ind_min_el] +
                                                                  three_vectors[14][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[15][i] * two_vectors[19][ind_min_el] +
                                                                  three_vectors[20][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[21][i] * two_vectors[20][ind_min_el] +
                                                                  three_vectors[22][i] * two_vectors[21][ind_min_el] +
                                                                  three_vectors[23][i] * two_vectors[23][ind_min_el] +
                                                                  three_vectors[34][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[35][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[38][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[39][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[42][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[43][i] * two_vectors[8][
                                                                      ind_min_el]) ** 2)

        main_array[2][i + 4 + 1 + 28 + 4 + incr_value] = 0.25 * ((three_vectors[34][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[44][i] * two_vectors[26][ind_min_el] +
                                                                  three_vectors[48][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[0][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[1][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[4][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[5][i] * two_vectors[7][ind_min_el] +
                                                                  three_vectors[8][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[9][i] * two_vectors[8][ind_min_el] +
                                                                  three_vectors[12][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[13][i] * two_vectors[11][ind_min_el] +
                                                                  three_vectors[24][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[25][i] * two_vectors[20][ind_min_el] +
                                                                  three_vectors[26][i] * two_vectors[21][ind_min_el] +
                                                                  three_vectors[27][i] * two_vectors[23][ind_min_el] +
                                                                  three_vectors[32][i] * two_vectors[0][ind_min_el] +
                                                                  three_vectors[33][i] * two_vectors[3][ind_min_el] +
                                                                  three_vectors[46][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[47][i] * two_vectors[15][ind_min_el] +
                                                                  three_vectors[50][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[51][i] * two_vectors[19][
                                                                      ind_min_el]) ** 2 +

                                                                 (three_vectors[35][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[45][i] * two_vectors[26][ind_min_el] +
                                                                  three_vectors[49][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[2][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[3][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[6][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[7][i] * two_vectors[7][ind_min_el] +
                                                                  three_vectors[10][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[11][i] * two_vectors[8][ind_min_el] +
                                                                  three_vectors[14][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[15][i] * two_vectors[11][ind_min_el] +
                                                                  three_vectors[28][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[29][i] * two_vectors[20][ind_min_el] +
                                                                  three_vectors[30][i] * two_vectors[21][ind_min_el] +
                                                                  three_vectors[31][i] * two_vectors[23][ind_min_el] +
                                                                  three_vectors[32][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[33][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[46][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[47][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[50][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[51][i] * two_vectors[16][
                                                                      ind_min_el]) ** 2)

        main_array[3][i + 4 + 1 + 28 + 4 + incr_value] = 0.25 * ((three_vectors[38][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[46][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[52][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[0][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[2][i] * two_vectors[0][ind_min_el] +
                                                                  three_vectors[4][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[6][i] * two_vectors[3][ind_min_el] +
                                                                  three_vectors[16][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[17][i] * two_vectors[8][ind_min_el] +
                                                                  three_vectors[20][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[21][i] * two_vectors[11][ind_min_el] +
                                                                  three_vectors[24][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[25][i] * two_vectors[16][ind_min_el] +
                                                                  three_vectors[28][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[29][i] * two_vectors[19][ind_min_el] +
                                                                  three_vectors[36][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[37][i] * two_vectors[7][ind_min_el] +
                                                                  three_vectors[44][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[45][i] * two_vectors[15][ind_min_el] +
                                                                  three_vectors[54][i] * two_vectors[21][ind_min_el] +
                                                                  three_vectors[55][i] * two_vectors[23][
                                                                      ind_min_el]) ** 2 +

                                                                 (three_vectors[39][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[47][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[53][i] * two_vectors[27][ind_min_el] +
                                                                  three_vectors[1][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[3][i] * two_vectors[0][ind_min_el] +
                                                                  three_vectors[5][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[7][i] * two_vectors[3][ind_min_el] +
                                                                  three_vectors[18][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[19][i] * two_vectors[8][ind_min_el] +
                                                                  three_vectors[22][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[23][i] * two_vectors[11][ind_min_el] +
                                                                  three_vectors[26][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[27][i] * two_vectors[16][ind_min_el] +
                                                                  three_vectors[30][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[31][i] * two_vectors[19][ind_min_el] +
                                                                  three_vectors[36][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[37][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[44][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[45][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[54][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[55][i] * two_vectors[20][
                                                                      ind_min_el]) ** 2)

        main_array[4][i + 4 + 1 + 28 + 4 + incr_value] = 0.25 * ((three_vectors[42][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[50][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[54][i] * two_vectors[26][ind_min_el] +

                                                                  three_vectors[8][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[10][i] * two_vectors[0][ind_min_el] +
                                                                  three_vectors[12][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[14][i] * two_vectors[3][ind_min_el] +

                                                                  three_vectors[16][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[18][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[20][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[22][i] * two_vectors[7][ind_min_el] +

                                                                  three_vectors[24][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[26][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[28][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[30][i] * two_vectors[15][ind_min_el] +

                                                                  three_vectors[40][i] * two_vectors[8][ind_min_el] +
                                                                  three_vectors[41][i] * two_vectors[11][ind_min_el] +
                                                                  three_vectors[48][i] * two_vectors[16][ind_min_el] +
                                                                  three_vectors[49][i] * two_vectors[19][ind_min_el] +
                                                                  three_vectors[52][i] * two_vectors[20][ind_min_el] +
                                                                  three_vectors[53][i] * two_vectors[23][
                                                                      ind_min_el]) ** 2 +

                                                                 (three_vectors[43][i] * two_vectors[24][ind_min_el] +
                                                                  three_vectors[51][i] * two_vectors[25][ind_min_el] +
                                                                  three_vectors[55][i] * two_vectors[26][ind_min_el] +

                                                                  three_vectors[9][i] * two_vectors[2][ind_min_el] +
                                                                  three_vectors[11][i] * two_vectors[0][ind_min_el] +
                                                                  three_vectors[13][i] * two_vectors[1][ind_min_el] +
                                                                  three_vectors[15][i] * two_vectors[3][ind_min_el] +

                                                                  three_vectors[17][i] * two_vectors[6][ind_min_el] +
                                                                  three_vectors[19][i] * two_vectors[4][ind_min_el] +
                                                                  three_vectors[21][i] * two_vectors[5][ind_min_el] +
                                                                  three_vectors[23][i] * two_vectors[7][ind_min_el] +

                                                                  three_vectors[25][i] * two_vectors[14][ind_min_el] +
                                                                  three_vectors[27][i] * two_vectors[12][ind_min_el] +
                                                                  three_vectors[29][i] * two_vectors[13][ind_min_el] +
                                                                  three_vectors[31][i] * two_vectors[15][ind_min_el] +

                                                                  three_vectors[40][i] * two_vectors[10][ind_min_el] +
                                                                  three_vectors[41][i] * two_vectors[9][ind_min_el] +
                                                                  three_vectors[48][i] * two_vectors[18][ind_min_el] +
                                                                  three_vectors[49][i] * two_vectors[17][ind_min_el] +
                                                                  three_vectors[52][i] * two_vectors[22][ind_min_el] +
                                                                  three_vectors[53][i] * two_vectors[21][
                                                                      ind_min_el]) ** 2)

    # ----------------------------------------------------------------------------------------------------------#
    # 3PGS
    ind_min_el = np.nanargmin(three_energy)
    for i in range(28):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + incr_value] = min(three_energy) - two_energy[i]  # 97 to 124
        main_array[1][i + 4 + 1 + 28 + 4 + 56 + incr_value] = 0.25 * (
                    (three_vectors[32][ind_min_el] * two_vectors[25][i] +
                     three_vectors[36][ind_min_el] * two_vectors[26][i] +
                     three_vectors[40][ind_min_el] * two_vectors[27][i] +
                     three_vectors[0][ind_min_el] * two_vectors[14][i] +
                     three_vectors[1][ind_min_el] * two_vectors[12][i] +
                     three_vectors[2][ind_min_el] * two_vectors[13][i] +
                     three_vectors[3][ind_min_el] * two_vectors[15][i] +
                     three_vectors[8][ind_min_el] * two_vectors[18][i] +
                     three_vectors[9][ind_min_el] * two_vectors[16][i] +
                     three_vectors[10][ind_min_el] * two_vectors[17][i] +
                     three_vectors[11][ind_min_el] * two_vectors[19][i] +
                     three_vectors[16][ind_min_el] * two_vectors[22][i] +
                     three_vectors[17][ind_min_el] * two_vectors[20][i] +
                     three_vectors[18][ind_min_el] * two_vectors[21][i] +
                     three_vectors[19][ind_min_el] * two_vectors[23][i] +
                     three_vectors[34][ind_min_el] * two_vectors[1][i] +
                     three_vectors[35][ind_min_el] * two_vectors[3][i] +
                     three_vectors[38][ind_min_el] * two_vectors[5][i] +
                     three_vectors[39][ind_min_el] * two_vectors[7][i] +
                     three_vectors[42][ind_min_el] * two_vectors[9][i] +
                     three_vectors[43][ind_min_el] * two_vectors[11][i]) ** 2 +

                    (three_vectors[33][ind_min_el] * two_vectors[25][i] +
                     three_vectors[37][ind_min_el] * two_vectors[26][i] +
                     three_vectors[41][ind_min_el] * two_vectors[27][i] +
                     three_vectors[4][ind_min_el] * two_vectors[14][i] +
                     three_vectors[5][ind_min_el] * two_vectors[12][i] +
                     three_vectors[6][ind_min_el] * two_vectors[13][i] +
                     three_vectors[7][ind_min_el] * two_vectors[15][i] +
                     three_vectors[12][ind_min_el] * two_vectors[18][i] +
                     three_vectors[13][ind_min_el] * two_vectors[16][i] +
                     three_vectors[14][ind_min_el] * two_vectors[17][i] +
                     three_vectors[15][ind_min_el] * two_vectors[19][i] +
                     three_vectors[20][ind_min_el] * two_vectors[22][i] +
                     three_vectors[21][ind_min_el] * two_vectors[20][i] +
                     three_vectors[22][ind_min_el] * two_vectors[21][i] +
                     three_vectors[23][ind_min_el] * two_vectors[23][i] +
                     three_vectors[34][ind_min_el] * two_vectors[2][i] +
                     three_vectors[35][ind_min_el] * two_vectors[4][i] +
                     three_vectors[38][ind_min_el] * two_vectors[6][i] +
                     three_vectors[39][ind_min_el] * two_vectors[4][i] +
                     three_vectors[42][ind_min_el] * two_vectors[10][i] +
                     three_vectors[43][ind_min_el] * two_vectors[8][i]) ** 2)

        main_array[2][i + 4 + 1 + 28 + 4 + 56 + incr_value] = 0.25 * (
                    (three_vectors[34][ind_min_el] * two_vectors[24][i] +
                     three_vectors[44][ind_min_el] * two_vectors[26][i] +
                     three_vectors[48][ind_min_el] * two_vectors[27][i] +
                     three_vectors[0][ind_min_el] * two_vectors[6][i] +
                     three_vectors[1][ind_min_el] * two_vectors[4][i] +
                     three_vectors[4][ind_min_el] * two_vectors[5][i] +
                     three_vectors[5][ind_min_el] * two_vectors[7][i] +
                     three_vectors[8][ind_min_el] * two_vectors[10][i] +
                     three_vectors[9][ind_min_el] * two_vectors[8][i] +
                     three_vectors[12][ind_min_el] * two_vectors[9][i] +
                     three_vectors[13][ind_min_el] * two_vectors[11][i] +
                     three_vectors[24][ind_min_el] * two_vectors[22][i] +
                     three_vectors[25][ind_min_el] * two_vectors[20][i] +
                     three_vectors[26][ind_min_el] * two_vectors[21][i] +
                     three_vectors[27][ind_min_el] * two_vectors[23][i] +
                     three_vectors[32][ind_min_el] * two_vectors[0][i] +
                     three_vectors[33][ind_min_el] * two_vectors[3][i] +
                     three_vectors[46][ind_min_el] * two_vectors[13][i] +
                     three_vectors[47][ind_min_el] * two_vectors[15][i] +
                     three_vectors[50][ind_min_el] * two_vectors[17][i] +
                     three_vectors[51][ind_min_el] * two_vectors[19][i]) ** 2 +

                    (three_vectors[35][ind_min_el] * two_vectors[24][i] +
                     three_vectors[45][ind_min_el] * two_vectors[26][i] +
                     three_vectors[49][ind_min_el] * two_vectors[27][i] +
                     three_vectors[2][ind_min_el] * two_vectors[6][i] +
                     three_vectors[3][ind_min_el] * two_vectors[4][i] +
                     three_vectors[6][ind_min_el] * two_vectors[5][i] +
                     three_vectors[7][ind_min_el] * two_vectors[7][i] +
                     three_vectors[10][ind_min_el] * two_vectors[10][i] +
                     three_vectors[11][ind_min_el] * two_vectors[8][i] +
                     three_vectors[14][ind_min_el] * two_vectors[9][i] +
                     three_vectors[15][ind_min_el] * two_vectors[11][i] +
                     three_vectors[28][ind_min_el] * two_vectors[22][i] +
                     three_vectors[29][ind_min_el] * two_vectors[20][i] +
                     three_vectors[30][ind_min_el] * two_vectors[21][i] +
                     three_vectors[31][ind_min_el] * two_vectors[23][i] +
                     three_vectors[32][ind_min_el] * two_vectors[2][i] +
                     three_vectors[33][ind_min_el] * two_vectors[1][i] +
                     three_vectors[46][ind_min_el] * two_vectors[14][i] +
                     three_vectors[47][ind_min_el] * two_vectors[12][i] +
                     three_vectors[50][ind_min_el] * two_vectors[18][i] +
                     three_vectors[51][ind_min_el] * two_vectors[16][i]) ** 2)

        main_array[3][i + 4 + 1 + 28 + 4 + 56 + incr_value] = 0.25 * (
                    (three_vectors[38][ind_min_el] * two_vectors[24][i] +
                     three_vectors[46][ind_min_el] * two_vectors[25][i] +
                     three_vectors[52][ind_min_el] * two_vectors[27][i] +
                     three_vectors[0][ind_min_el] * two_vectors[2][i] +
                     three_vectors[2][ind_min_el] * two_vectors[0][i] +
                     three_vectors[4][ind_min_el] * two_vectors[1][i] +
                     three_vectors[6][ind_min_el] * two_vectors[3][i] +
                     three_vectors[16][ind_min_el] * two_vectors[10][i] +
                     three_vectors[17][ind_min_el] * two_vectors[8][i] +
                     three_vectors[20][ind_min_el] * two_vectors[9][i] +
                     three_vectors[21][ind_min_el] * two_vectors[11][i] +
                     three_vectors[24][ind_min_el] * two_vectors[18][i] +
                     three_vectors[25][ind_min_el] * two_vectors[16][i] +
                     three_vectors[28][ind_min_el] * two_vectors[17][i] +
                     three_vectors[29][ind_min_el] * two_vectors[19][i] +
                     three_vectors[36][ind_min_el] * two_vectors[4][i] +
                     three_vectors[37][ind_min_el] * two_vectors[7][i] +
                     three_vectors[44][ind_min_el] * two_vectors[12][i] +
                     three_vectors[45][ind_min_el] * two_vectors[15][i] +
                     three_vectors[54][ind_min_el] * two_vectors[21][i] +
                     three_vectors[55][ind_min_el] * two_vectors[23][i]) ** 2 +

                    (three_vectors[39][ind_min_el] * two_vectors[24][i] +
                     three_vectors[47][ind_min_el] * two_vectors[25][i] +
                     three_vectors[53][ind_min_el] * two_vectors[27][i] +
                     three_vectors[1][ind_min_el] * two_vectors[2][i] +
                     three_vectors[3][ind_min_el] * two_vectors[0][i] +
                     three_vectors[5][ind_min_el] * two_vectors[1][i] +
                     three_vectors[7][ind_min_el] * two_vectors[3][i] +
                     three_vectors[18][ind_min_el] * two_vectors[10][i] +
                     three_vectors[19][ind_min_el] * two_vectors[8][i] +
                     three_vectors[22][ind_min_el] * two_vectors[9][i] +
                     three_vectors[23][ind_min_el] * two_vectors[11][i] +
                     three_vectors[26][ind_min_el] * two_vectors[18][i] +
                     three_vectors[27][ind_min_el] * two_vectors[16][i] +
                     three_vectors[30][ind_min_el] * two_vectors[17][i] +
                     three_vectors[31][ind_min_el] * two_vectors[19][i] +
                     three_vectors[36][ind_min_el] * two_vectors[6][i] +
                     three_vectors[37][ind_min_el] * two_vectors[5][i] +
                     three_vectors[44][ind_min_el] * two_vectors[14][i] +
                     three_vectors[45][ind_min_el] * two_vectors[13][i] +
                     three_vectors[54][ind_min_el] * two_vectors[22][i] +
                     three_vectors[55][ind_min_el] * two_vectors[20][i]) ** 2)

        main_array[4][i + 4 + 1 + 28 + 4 + 56 + incr_value] = 0.25 * (
                    (three_vectors[42][ind_min_el] * two_vectors[24][i] +
                     three_vectors[50][ind_min_el] * two_vectors[25][i] +
                     three_vectors[54][ind_min_el] * two_vectors[26][i] +

                     three_vectors[8][ind_min_el] * two_vectors[2][i] +
                     three_vectors[10][ind_min_el] * two_vectors[0][i] +
                     three_vectors[12][ind_min_el] * two_vectors[1][i] +
                     three_vectors[14][ind_min_el] * two_vectors[3][i] +

                     three_vectors[16][ind_min_el] * two_vectors[6][i] +
                     three_vectors[18][ind_min_el] * two_vectors[4][i] +
                     three_vectors[20][ind_min_el] * two_vectors[5][i] +
                     three_vectors[22][ind_min_el] * two_vectors[7][i] +

                     three_vectors[24][ind_min_el] * two_vectors[14][i] +
                     three_vectors[26][ind_min_el] * two_vectors[12][i] +
                     three_vectors[28][ind_min_el] * two_vectors[13][i] +
                     three_vectors[30][ind_min_el] * two_vectors[15][i] +

                     three_vectors[40][ind_min_el] * two_vectors[8][i] +
                     three_vectors[41][ind_min_el] * two_vectors[11][i] +
                     three_vectors[48][ind_min_el] * two_vectors[16][i] +
                     three_vectors[49][ind_min_el] * two_vectors[19][i] +
                     three_vectors[52][ind_min_el] * two_vectors[20][i] +
                     three_vectors[53][ind_min_el] * two_vectors[23][i]) ** 2 +

                    (three_vectors[43][ind_min_el] * two_vectors[24][i] +
                     three_vectors[51][ind_min_el] * two_vectors[25][i] +
                     three_vectors[55][ind_min_el] * two_vectors[26][i] +

                     three_vectors[9][ind_min_el] * two_vectors[2][i] +
                     three_vectors[11][ind_min_el] * two_vectors[0][i] +
                     three_vectors[13][ind_min_el] * two_vectors[1][i] +
                     three_vectors[15][ind_min_el] * two_vectors[3][i] +

                     three_vectors[17][ind_min_el] * two_vectors[6][i] +
                     three_vectors[19][ind_min_el] * two_vectors[4][i] +
                     three_vectors[21][ind_min_el] * two_vectors[5][i] +
                     three_vectors[23][ind_min_el] * two_vectors[7][i] +

                     three_vectors[25][ind_min_el] * two_vectors[14][i] +
                     three_vectors[27][ind_min_el] * two_vectors[12][i] +
                     three_vectors[29][ind_min_el] * two_vectors[13][i] +
                     three_vectors[31][ind_min_el] * two_vectors[15][i] +

                     three_vectors[40][ind_min_el] * two_vectors[10][i] +
                     three_vectors[41][ind_min_el] * two_vectors[9][i] +
                     three_vectors[48][ind_min_el] * two_vectors[18][i] +
                     three_vectors[49][ind_min_el] * two_vectors[17][i] +
                     three_vectors[52][ind_min_el] * two_vectors[22][i] +
                     three_vectors[53][ind_min_el] * two_vectors[21][i]) ** 2)



    for i in range(70):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + incr_value] = four_energy[i] - min(three_energy)

    # ----------------------------------------------------------------------------------------------------------#
    # 4PGS

    for i in range(56):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + incr_value] = min(four_energy) - three_energy[i]  # 97 to 124

    for i in range(56):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + incr_value] = five_energy[i] - min(four_energy)

    # ----------------------------------------------------------------------------------------------------------#
    # 5PGS

    for i in range(70):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + incr_value] = min(five_energy) - four_energy[
            i]  # 97 to 124

    for i in range(28):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + incr_value] = six_energy[i] - min(five_energy)

    # ----------------------------------------------------------------------------------------------------------#
    # 6PGS

    for i in range(56):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + 28 + incr_value] = min(six_energy) - five_energy[
            i]  # 97 to 124

    for i in range(4):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + 28 + 56 + incr_value] = seven_energy[i] - min(
            six_energy)

    # ----------------------------------------------------------------------------------------------------------#
    # 7PGS

    for i in range(28):
        main_array[0][i + 4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + 28 + 56 + 4 + incr_value] = min(seven_energy) - \
                                                                                                six_energy[
                                                                                                    i]  # 97 to 124

    main_array[0][4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + 28 + 56 + 4 + 28 + incr_value] = eight_energy - min(
        seven_energy)

    # ----------------------------------------------------------------------------------------------------------#
    # 8PGS

    for i in range(4):
        main_array[0][4 + 1 + 28 + 4 + 56 + 28 + 70 + 56 + 70 + 28 + 56 + 4 + 28 + 1 + incr_value] = eight_energy - \
                                                                                                     seven_energy[i]  # to 446

    incr_value = incr_value + 438  # исправить
    return incr_value


def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if int(array[0][mid] * 1000) / 1000 - 0.05 <= element <= int(array[0][mid] * 1000) / 1000 + 0.05:
        return mid

    if element < int(array[0][mid] * 1000) / 1000 - 0.05:
        return binary_search_recursive(array, element, start, mid - 1)
    if element > int(array[0][mid] * 1000) / 1000 + 0.05:
        return binary_search_recursive(array, element, mid + 1, end)


def output_to_file(file_name, output_values):
    file = open(file_name + '.txt', 'a')

    file.write(output_values + '\n')

    file.close()


# изменить с учетом четырех  узлов в системе
def DOS_calc_for_inter_system(energ_array, zone_weight, number_of_sys, coulomb_potential):
    energy_distribution = energ_array[0][0] - 0.5
    while energy_distribution < energ_array[0][number_of_sys * 18 - 1] + 0.5:

        element_index = binary_search_recursive(energ_array, energy_distribution, 0, len(energ_array[0]) - 1)
        dos = 0
        if element_index < 250_001:
            for array_element in range(0, element_index + 250_000):
                dos = dos + (energ_array[1][array_element] + energ_array[2][array_element]) * \
                      approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution)

        if 250_001 <= element_index < len(energ_array[0]) - 250_000:
            for array_element in range(element_index - 250_000, element_index + 250_000):
                dos = dos + (energ_array[1][array_element] + energ_array[2][array_element]) * \
                      approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution)

        if element_index >= len(energ_array[0]) - 250_000:
            for array_element in range(element_index - 250_000, len(energ_array[0]) - 1):
                dos = dos + (energ_array[1][array_element] + energ_array[2][array_element]) * \
                      approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution)

        energy_distribution += 0.002

        output_to_file('DOS for system with interaction U = ' + str(coulomb_potential), str(dos / number_of_sys))


# изменить с учетом четырех  узлов в системе
def GIPR(energ_array, array_element, energy_distribution):
    gipr = ((energ_array[1][array_element] * approx_of_delta_function(0.0015, energ_array[0][array_element],
                                                                      energy_distribution)) ** 2 +
            (energ_array[2][array_element] * approx_of_delta_function(0.0015, energ_array[0][array_element],
                                                                      energy_distribution)) ** 2) / (
                   energ_array[1][array_element] * approx_of_delta_function(0.0015, energ_array[0][array_element],
                                                                            energy_distribution) +
                   energ_array[2][array_element] * approx_of_delta_function(0.0015, energ_array[0][array_element],
                                                                            energy_distribution)) ** 2
    return gipr


# изменить с учетом четырех  узлов в системе
def ensemble_averaged_GIPR(energ_array, zone_weight, number_of_sys, coulomb_potential):
    energy_distribution = energ_array[0][0] - 1
    while energy_distribution < energ_array[0][number_of_sys * 18 - 1] + 1:
        element_index = binary_search_recursive(energ_array, energy_distribution, 0, len(energ_array[0]) - 1)
        esemble_average_gipr = 0
        intermidate = 0

        if element_index < 250_000:
            for array_element in range(0, element_index + 250_000):
                esemble_average_gipr = esemble_average_gipr + (
                        (energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015, energ_array[0][array_element],
                    energy_distribution) *
                        GIPR(energ_array, array_element, energy_distribution) * approx_of_delta_function(0.0015,
                                                                                                         energ_array[0][
                                                                                                             array_element],
                                                                                                         energy_distribution))
                intermidate = intermidate + (
                        energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015,
                    energ_array[
                        0][
                        array_element],
                    energy_distribution) * (
                                  approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution))
            esemble_average_gipr = esemble_average_gipr / intermidate

        if 250_000 <= element_index < len(energ_array[0]) - 250_000:
            for array_element in range(element_index - 250_000, element_index + 250_000):
                esemble_average_gipr = esemble_average_gipr + (
                        (energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015,
                    energ_array[0][array_element],
                    energy_distribution) *
                        GIPR(energ_array, array_element, energy_distribution) * approx_of_delta_function(0.0015,
                                                                                                         energ_array[0][
                                                                                                             array_element],
                                                                                                         energy_distribution))
                intermidate = intermidate + (
                        energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015, energ_array[0][array_element], energy_distribution) * (
                                  approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution))

            esemble_average_gipr = esemble_average_gipr / intermidate

        if element_index >= len(energ_array[0]) - 250_000:
            for array_element in range(element_index - 250_000, len(energ_array[0]) - 1):
                esemble_average_gipr = esemble_average_gipr + (
                        (energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015,
                    energ_array[0][array_element],
                    energy_distribution) *
                        GIPR(energ_array, array_element, energy_distribution) * approx_of_delta_function(0.0015,
                                                                                                         energ_array[0][
                                                                                                             array_element],
                                                                                                         energy_distribution))
                intermidate = intermidate + (
                        energ_array[1][array_element] + energ_array[2][array_element]) * approx_of_delta_function(
                    0.0015, energ_array[0][array_element], energy_distribution) * (
                                  approx_of_delta_function(0.0015, energ_array[0][array_element], energy_distribution))

            esemble_average_gipr = esemble_average_gipr / intermidate

        output_to_file('IPR for system with interaction U = ' + str(coulomb_potential), str(esemble_average_gipr))
        energy_distribution += 0.002


def hip_trad(main_array, func_name, zone_wight=None, systems_of_number=None, coulomb_potential=None):
    separator = int(len(main_array[0]) / 10)
    calc_range = 0

    for i in range(10):
        calc_range_start = calc_range
        calc_range_fin = calc_range = calc_range + separator
        x = th.Thread()
        x.start(target=func_name, args=(main_array, zone_wight, systems_of_number, coulomb_potential,
                                        calc_range_start, calc_range_fin))

    return 0


def quick_sort(mas, fst, lst):
    if fst >= lst:
        return mas

    i, j = fst, lst
    pivot = mas[0][int((fst + lst) / 2)]
    while i <= j:
        while mas[0][i] < pivot:
            i += 1
        while mas[0][j] > pivot:
            j -= 1
        if i <= j:
            mas[0][i], mas[0][j] = mas[0][j], mas[0][i]
            mas[1][i], mas[1][j] = mas[1][j], mas[1][i]
            mas[2][i], mas[2][j] = mas[2][j], mas[2][i]
            mas[3][i], mas[3][j] = mas[3][j], mas[3][i]
            mas[4][i], mas[4][j] = mas[4][j], mas[4][i]
            i, j = i + 1, j - 1

    quick_sort(mas, fst, j)
    quick_sort(mas, i, lst)
