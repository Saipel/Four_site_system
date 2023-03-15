import numpy as np
import pandas as pd

import threading as th
import random
import math


def create_ham_param(zone_wight):
    site_potential = np.zeros(4)
    for i in range(len(site_potential)):
        site_potential[i] = random.uniform(-zone_wight / 2, zone_wight / 2)

    t = 1
    return site_potential, t


def null_array(case_number):
    if case_number == 0 or case_number == 8:
        array = 0

    if case_number == 1 or case_number == 7:
        array = np.zeros(8)

    if case_number == 2 or case_number == 6:
        array = np.zeros(28)

    if case_number == 3 or case_number == 5:
        array = np.zeros(56)

    if case_number == 4:
        array = np.zeros(70)

    return array


def ham_array(case_number, site_energy, t, U, array):
    # finish
    if case_number == 0:
        array = 0

    # finish
    if case_number == 1:
        array[0][0] = array[4][4] = site_energy[0]
        array[1][1] = array[5][5] = site_energy[1]
        array[2][2] = array[6][6] = site_energy[2]
        array[3][3] = array[7][7] = site_energy[3]

        array[0][1] = array[1][0] = array[1][2] = array[2][1] = -t
        array[0][3] = array[3][0] = array[3][2] = array[2][3] = -t
        array[0 + 4][1 + 4] = array[1 + 4][0 + 4] = array[1 + 4][2 + 4] = array[2 + 4][1 + 4] = -t
        array[0 + 4][3 + 4] = array[3 + 4][0 + 4] = array[3 + 4][2 + 4] = array[2 + 4][3 + 4] = -t

    # mabe finish
    if case_number == 2:
        # Site energy
        array[0][0] = array[1][1] = array[2][2] = array[3][3] = site_energy[0] + site_energy[1]
        array[4][4] = array[5][5] = array[6][6] = array[7][7] = site_energy[0] + site_energy[2]
        array[8][8] = array[9][9] = array[10][10] = array[11][11] = site_energy[0] + site_energy[3]

        array[12][12] = array[13][13] = array[14][14] = array[15][15] = site_energy[1] + site_energy[2]
        array[16][16] = array[17][17] = array[18][18] = array[19][19] = site_energy[1] + site_energy[3]

        array[20][20] = array[21][21] = array[22][22] = array[23][23] = site_energy[2] + site_energy[3]

        array[24][24] = 2 * site_energy[0] + U
        array[25][25] = 2 * site_energy[1] + U
        array[26][26] = 2 * site_energy[2] + U
        array[27][27] = 2 * site_energy[3] + U

        # jump parameter

        for i in range(0, 7, 1):

            array[0 + i][4 + i] = array[4 + i][0 + i] = -t
            array[4 + i][12 + i] = array[12 + i][4 + i] = -t
            array[12 + i][16 + i] = array[16 + i][12 + i] = -t

        array[16][1] = array[1][16] = array[17][0] = array[0][17] = t
        array[18][2] = array[2][18] = array[19][3] = array[3][19] = t

        array[20][5] = array[5][20] = array[21][4] = array[4][21] = t
        array[22][6] = array[6][22] = array[7][23] = array[23][7] = t

        array[0][24] = array[24][0] = array[0][25] = array[25][0] = -t
        array[1][24] = array[24][1] = array[1][25] = array[25][1] = t

        array[8][24] = array[24][8] = array[8][27] = array[27][8] = -t
        array[9][24] = array[24][9] = array[9][27] = array[27][9] = t

        array[12][25] = array[25][12] = array[12][26] = array[26][12] = -t
        array[13][25] = array[25][13] = array[13][26] = array[26][13] = t

        array[20][26] = array[26][20] = array[20][27] = array[27][20] = -t
        array[21][26] = array[26][21] = array[21][27] = array[27][21] = t

        print(array)

    # not finish
    if case_number == 3:

        # site energy
        for i in range(0, 7, 1):
            array[i][i] = site_energy[0] + site_energy[1] + site_energy[2]
            array[i + 8][i + 8] = site_energy[0] + site_energy[1] + site_energy[3]
            array[i + 16][i + 16] = site_energy[0] + site_energy[2] + site_energy[3]
            array[i + 24][i + 24] = site_energy[1] + site_energy[2] + site_energy[3]

        array[32][32] = array[33][33] = 2 * site_energy[1] + site_energy[0] + U
        array[34][34] = array[35][35] = 2 * site_energy[0] + site_energy[1] + U

        array[36][36] = array[37][37] = 2 * site_energy[2] + site_energy[0] + U
        array[38][38] = array[39][39] = 2 * site_energy[0] + site_energy[2] + U

        array[40][40] = array[41][41] = 2 * site_energy[3] + site_energy[0] + U
        array[42][42] = array[43][43] = 2 * site_energy[0] + site_energy[3] + U

        array[44][44] = array[45][45] = 2 * site_energy[2] + site_energy[1] + U
        array[46][46] = array[47][47] = 2 * site_energy[1] + site_energy[2] + U

        array[48][48] = array[49][49] = 2 * site_energy[3] + site_energy[1] + U
        array[50][50] = array[51][51] = 2 * site_energy[1] + site_energy[3] + U

        array[52][52] = array[53][53] = 2 * site_energy[3] + site_energy[2] + U
        array[54][54] = array[55][55] = 2 * site_energy[2] + site_energy[3] + U

        # jump parameter

        for i in range(0, 23, 1):
            array[8][0] = array[0][8] = -t

        array[0][24] = array[24][0] = array[26][1] = array[1][26] = -t
        array[2][28] = array[28][2] = array[30][3] = array[3][30] = -t

        array[4][25] = array[25][4] = array[27][5] = array[5][27] = -t
        array[6][29] = array[29][6] = array[31][7] = array[7][31] = -t

        array[32][1] = array[1][32] = array[1][36] = array[36][1] = -t

        array[38][2] = array[2][38] = array[2][46] = array[46][2] = -t
        array[32][2] = array[2][32] = array[2][36] = array[36][2] = t

        array[39][3] = array[3][39] = array[3][47] = array[47][3] = -t

        array[38][4] = array[4][38] = array[4][46] = array[46][4] = t

        array[39][5] = array[5][39] = array[5][47] = array[47][5] = t
        array[33][5] = array[5][33] = array[5][37] = array[37][5] = -t

        array[33][6] = array[6][33] = array[6][37] = array[37][6] = t

        array[48][9] = array[9][48] = array[9][34] = array[34][9] = t

        array[42][10] = array[10][42] = array[10][50] = array[50][10] = -t

        array[35][11] = array[11][35] = array[11][49] = array[49][11] = t
        array[43][11] = array[11][43] = array[11][51] = array[51][11] = -t

        array[42][12] = array[12][42] = array[12][50] = array[50][12] = t
        array[48][12] = array[12][48] = array[12][34] = array[34][12] = -t

        array[43][13] = array[13][43] = array[13][51] = array[51][13] = t

        array[35][14] = array[14][35] = array[14][49] = array[49][14] = -t

        array[36][17] = array[17][36] = array[17][40] = array[40][17] = -t
        array[38][17] = array[17][38] = array[17][52] = array[52][17] = t

        array[36][18] = array[18][36] = array[18][40] = array[40][18] = t

        array[39][19] = array[19][39] = array[19][53] = array[53][19] = t

        array[38][20] = array[20][38] = array[20][52] = array[52][20] = -t

        array[37][21] = array[21][37] = array[21][41] = array[41][21] = -t

        array[37][22] = array[22][37] = array[22][41] = array[41][22] = t
        array[39][22] = array[22][39] = array[22][53] = array[53][22] = -t

        array[44][25] = array[25][44] = array[25][48] = array[48][25] = -t

        array[44][26] = array[26][44] = array[26][48] = array[48][26] = t
        array[50][26] = array[26][50] = array[26][54] = array[54][26] = -t

        array[51][27] = array[27][51] = array[27][55] = array[55][27] = -t

        array[50][28] = array[28][50] = array[28][54] = array[54][28] = t

        array[59][27] = array[29][51] = array[29][55] = array[55][29] = t
        array[45][29] = array[29][45] = array[29][49] = array[49][29] = -t

        array[45][30] = array[30][45] = array[30][49] = array[49][30] = t




    # not finish
    if case_number == 4:
        array = 0

    # not finish
    if case_number == 5:
        array = 0

    # Not finished
    if case_number == 6:
        array[0][0] = array[1][1] = array[2][2] = array[3][3] = 2 * site_energy[0] + 2 * site_energy[1] + site_energy[
            2] + site_energy[3] + 2 * U
        array[4][4] = array[5][5] = array[6][6] = array[7][7] = 2 * site_energy[0] + 2 * site_energy[2] + site_energy[
            1] + site_energy[3] + 2 * U
        array[8][8] = array[9][9] = array[10][10] = array[11][11] = 2 * site_energy[1] + 2 * site_energy[2] + \
                                                                    site_energy[0] + site_energy[3] + 2 * U

        array[12][12] = array[13][13] = array[14][14] = array[15][15] = 2 * site_energy[1] + 2 * site_energy[3] + \
                                                                        site_energy[2] + site_energy[0] + 2 * U
        array[16][16] = array[17][17] = array[18][18] = array[19][19] = 2 * site_energy[2] + 2 * site_energy[3] + \
                                                                        site_energy[0] + site_energy[1] + 2 * U

        array[20][20] = array[21][21] = array[22][22] = array[23][23] = 2 * site_energy[0] + 2 * site_energy[3] + \
                                                                        site_energy[2] + site_energy[1] + 2 * U

        array[24][24] = 2 * site_energy[0] + 2 * site_energy[1] + 2 * site_energy[2] + 3 * U
        array[25][25] = 2 * site_energy[0] + 2 * site_energy[1] + 2 * site_energy[3] + 3 * U
        array[26][26] = 2 * site_energy[0] + 2 * site_energy[2] + 2 * site_energy[3] + 3 * U
        array[27][27] = 2 * site_energy[1] + 2 * site_energy[2] + 2 * site_energy[3] + 3 * U

    # finish
    if case_number == 7:
        array[0][0] = array[4][4] = 2 * site_energy[0] + 2 * site_energy[1] + 2 * site_energy[2] + site_energy[
            3] + 3 * U
        array[1][1] = array[5][5] = 2 * site_energy[0] + 2 * site_energy[1] + 2 * site_energy[3] + site_energy[
            2] + 3 * U
        array[2][2] = array[6][6] = 2 * site_energy[0] + 2 * site_energy[3] + 2 * site_energy[2] + site_energy[
            1] + 3 * U
        array[3][3] = array[7][7] = 2 * site_energy[3] + 2 * site_energy[1] + 2 * site_energy[2] + site_energy[
            0] + 3 * U

        array[0][1] = array[1][0] = array[1][2] = array[2][1] = t
        array[0][3] = array[3][0] = array[3][2] = array[2][3] = t
        array[0 + 4][1 + 4] = array[1 + 4][0 + 4] = array[1 + 4][2 + 4] = array[2 + 4][1 + 4] = t
        array[0 + 4][3 + 4] = array[3 + 4][0 + 4] = array[3 + 4][2 + 4] = array[2 + 4][3 + 4] = t

    # finish
    if case_number == 8:
        array = 2 * site_energy[0] + 2 * site_energy[1] + 2 * site_energy[2] + 2 * site_energy[3] + 4 * U

    return 0


def calc_eigenvalue_array(array_for_calc, number_of_case):
    array_for_output = []
    if number_of_case != 8:
        intermediate_stage, _ = np.linalg.eig(array_for_calc)
        # print("intermediate_stage = ", intermediate_stage)
        return intermediate_stage
    else:
        array_for_output.append(array_for_calc)

    return array_for_output


def calc_eigenvectors_of_an_array(array_for_calc):
    _, intermediate_stage = np.linalg.eig(array_for_calc)
    # print("intarmidate of vector array = \n", intermediate_stage)

    return intermediate_stage
