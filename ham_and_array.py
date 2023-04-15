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
        array = np.zeros((8, 8))

    if case_number == 2 or case_number == 6:
        array = np.zeros((28, 28))

    if case_number == 3 or case_number == 5:
        array = np.zeros((56, 56))

    if case_number == 4:
        array = np.zeros((70, 70))

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

    # finish
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

        for i in range(0, 8, 1):
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

    # finish
    if case_number == 3:

        # site energy
        for i in range(0, 8, 1):
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

        for i in range(0, 24, 1):
            array[8 + i][0 + i] = array[0 + i][8 + i] = -t

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

        array[51][29] = array[29][51] = array[29][55] = array[55][29] = t
        array[45][29] = array[29][45] = array[29][49] = array[49][29] = -t

        array[45][30] = array[30][45] = array[30][49] = array[49][30] = t

        array[32][34] = array[34][32] = t
        array[32][50] = array[50][32] = -t

        array[33][35] = array[35][33] = t
        array[33][51] = array[51][33] = -t

        array[34][38] = array[38][34] = -t
        array[35][39] = array[39][35] = -t

        array[36][44] = array[44][36] = -t
        array[36][54] = array[54][36] = -t

        array[37][45] = array[45][37] = -t
        array[37][55] = array[55][37] = -t

        array[38][42] = array[42][38] = -t
        array[39][43] = array[43][39] = -t

        array[40][42] = array[42][40] = t
        array[40][48] = array[48][40] = -t

        array[41][43] = array[43][41] = t
        array[41][49] = array[49][41] = -t

        array[44][46] = array[46][44] = t
        array[45][47] = array[47][45] = t

        array[46][50] = array[50][46] = -t
        array[47][51] = array[51][47] = -t

        array[48][52] = array[52][48] = -t
        array[49][53] = array[53][49] = -t

        array[54][52] = array[52][54] = t
        array[53][55] = array[55][53] = t

    # finish
    if case_number == 4:

        # site energy
        for i in range(0, 16, 1):
            array[i][i] = site_energy[0] + site_energy[1] + site_energy[2] + site_energy[3]

        for i in range(0, 4, 1):
            array[16 + i][16 + i] = 2 * site_energy[0] + site_energy[1] + site_energy[2] + U
            array[16 + 4 + i][16 + 4 + i] = 2 * site_energy[1] + site_energy[0] + site_energy[2] + U
            array[16 + 8 + i][16 + 8 + i] = 2 * site_energy[2] + site_energy[1] + site_energy[0] + U

            array[16 + 12 + i][16 + 12 + i] = 2 * site_energy[0] + site_energy[1] + site_energy[3] + U
            array[16 + 16 + i][16 + 16 + i] = 2 * site_energy[1] + site_energy[0] + site_energy[3] + U
            array[16 + 20 + i][16 + 20 + i] = 2 * site_energy[3] + site_energy[1] + site_energy[0] + U

            array[16 + 24 + i][16 + 24 + i] = 2 * site_energy[0] + site_energy[2] + site_energy[3] + U
            array[16 + 28 + i][16 + 28 + i] = 2 * site_energy[2] + site_energy[0] + site_energy[3] + U
            array[16 + 32 + i][16 + 32 + i] = 2 * site_energy[3] + site_energy[2] + site_energy[0] + U

            array[16 + 36 + i][16 + 36 + i] = 2 * site_energy[1] + site_energy[2] + site_energy[3] + U
            array[16 + 40 + i][16 + 40 + i] = 2 * site_energy[2] + site_energy[1] + site_energy[3] + U
            array[16 + 44 + i][16 + 44 + i] = 2 * site_energy[3] + site_energy[2] + site_energy[1] + U

        array[64][64] = 2 * site_energy[0] + 2 * site_energy[1] + 2 * U
        array[65][65] = 2 * site_energy[0] + 2 * site_energy[2] + 2 * U
        array[66][66] = 2 * site_energy[0] + 2 * site_energy[3] + 2 * U

        array[67][67] = 2 * site_energy[1] + 2 * site_energy[2] + 2 * U
        array[68][68] = 2 * site_energy[1] + 2 * site_energy[3] + 2 * U

        array[69][69] = 2 * site_energy[2] + 2 * site_energy[3] + 2 * U

        # jump parameter

        array[1][16] = array[16][1] = array[1][60] = array[60][1] = -t
        array[1][24] = array[24][1] = array[1][36] = array[36][1] = -t

        array[2][24] = array[24][2] = array[2][36] = array[36][2] = t
        array[2][32] = array[32][2] = array[2][44] = array[44][2] = -t

        array[3][33] = array[33][3] = array[3][45] = array[45][3] = -t
        array[3][17] = array[17][3] = array[3][61] = array[61][3] = -t

        array[4][32] = array[32][4] = array[4][44] = array[44][4] = t
        array[4][40] = array[40][4] = array[4][52] = array[52][4] = -t

        array[5][18] = array[18][5] = array[5][25] = array[25][5] = -t
        array[5][37] = array[37][5] = array[5][41] = array[41][5] = -t
        array[5][53] = array[53][5] = array[5][62] = array[62][5] = -t
        array[5][33] = array[33][5] = array[5][45] = array[45][5] = t

        array[6][25] = array[25][6] = array[6][37] = array[37][6] = t
        array[6][42] = array[42][6] = array[6][54] = array[54][6] = -t

        array[7][19] = array[19][7] = array[7][43] = array[43][7] = -t
        array[7][55] = array[55][7] = array[7][63] = array[63][7] = -t

        array[8][16] = array[16][8] = array[8][40] = array[40][8] = t
        array[8][52] = array[52][8] = array[8][60] = array[60][8] = t

        array[9][26] = array[26][9] = array[9][38] = array[38][9] = -t
        array[9][41] = array[41][9] = array[9][53] = array[53][9] = t

        array[10][17] = array[17][10] = array[10][26] = array[26][10] = t
        array[10][46] = array[46][10] = array[10][34] = array[34][10] = -t
        array[10][42] = array[42][10] = array[10][38] = array[38][10] = t
        array[10][54] = array[54][10] = array[10][61] = array[61][10] = t

        array[11][35] = array[35][11] = array[11][47] = array[47][11] = -t
        array[11][43] = array[43][11] = array[11][55] = array[55][11] = t

        array[12][18] = array[18][12] = array[12][34] = array[34][12] = t
        array[12][46] = array[46][12] = array[12][62] = array[62][12] = t

        array[13][27] = array[27][13] = array[13][39] = array[39][13] = -t
        array[13][35] = array[35][13] = array[13][47] = array[47][13] = t

        array[14][19] = array[19][14] = array[14][27] = array[27][14] = t
        array[14][39] = array[39][14] = array[14][63] = array[63][14] = t

        for i in range(0, 8, 1):
            array[16 + i][20 + i] = array[20 + i][16 + i] = t
            array[16 + i][28 + i] = array[28 + i][16 + i] = -t

        array[24][56] = array[56][24] = array[26][57] = array[57][26] = -t
        array[25][58] = array[58][25] = array[27][59] = array[59][27] = -t

        for i in range(0, 4, 1):
            array[36 + i][48 + i] = array[48 + i][36 + i] = -t
            array[40 + i][48 + i] = array[48 + i][40 + i] = -t
            array[44 + i][48 + i] = array[48 + i][44 + i] = t

        for i in range(0, 8, 1):
            array[52 + i][56 + i] = array[56 + i][52 + i] = t

        array[17][64] = array[64][17] = array[17][65] = array[65][17] = -t
        array[18][64] = array[64][18] = array[18][65] = array[65][18] = t

        array[25][65] = array[65][25] = array[25][67] = array[67][25] = -t
        array[26][65] = array[65][26] = array[26][67] = array[67][26] = t

        array[33][64] = array[64][33] = array[33][68] = array[68][33] = -t
        array[34][64] = array[64][34] = array[34][68] = array[68][34] = t

        array[37][66] = array[66][37] = array[37][68] = array[68][37] = -t
        array[38][66] = array[66][38] = array[38][68] = array[68][38] = t

        array[41][65] = array[65][41] = array[41][66] = array[66][41] = -t
        array[42][65] = array[65][42] = array[42][66] = array[66][42] = t

        array[45][65] = array[65][45] = array[45][69] = array[69][45] = -t
        array[45][66] = array[65][46] = array[46][69] = array[69][46] = t

        array[53][67] = array[67][53] = array[53][68] = array[68][53] = -t
        array[54][67] = array[67][54] = array[54][68] = array[68][54] = t

        array[61][69] = array[69][61] = array[61][68] = array[68][61] = -t
        array[62][69] = array[69][62] = array[62][68] = array[68][62] = t

    # finish
    if case_number == 5:

        # site energy
        for i in range(0, 8, 1):
            array[i][i] = 2 * site_energy[0] + site_energy[1] + site_energy[2] + site_energy[3] + U
            array[i + 8][i + 8] = 2 * site_energy[1] + site_energy[0] + site_energy[2] + site_energy[3] + U
            array[i + 16][i + 16] = 2 * site_energy[2] + site_energy[1] + site_energy[0] + site_energy[3] + U
            array[i + 24][i + 24] = 2 * site_energy[3] + site_energy[1] + site_energy[2] + site_energy[0] + U

        array[32][32] = array[33][33] = 2 * site_energy[1] + 2 * site_energy[0] + site_energy[2] + 2 * U
        array[34][34] = array[35][35] = 2 * site_energy[2] + 2 * site_energy[0] + site_energy[1] + 2 * U

        array[36][36] = array[37][37] = 2 * site_energy[1] + 2 * site_energy[2] + site_energy[0] + 2 * U
        array[38][38] = array[39][39] = 2 * site_energy[1] + 2 * site_energy[0] + site_energy[3] + 2 * U

        array[40][40] = array[41][41] = 2 * site_energy[3] + 2 * site_energy[0] + site_energy[1] + 2 * U
        array[42][42] = array[43][43] = 2 * site_energy[1] + 2 * site_energy[3] + site_energy[0] + 2 * U

        array[44][44] = array[45][45] = 2 * site_energy[0] + 2 * site_energy[2] + site_energy[3] + 2 * U
        array[46][46] = array[47][47] = 2 * site_energy[0] + 2 * site_energy[3] + site_energy[2] + 2 * U

        array[48][48] = array[49][49] = 2 * site_energy[2] + 2 * site_energy[3] + site_energy[0] + 2 * U
        array[50][50] = array[51][51] = 2 * site_energy[2] + 2 * site_energy[3] + site_energy[1] + 2 * U

        array[52][52] = array[53][53] = 2 * site_energy[1] + 2 * site_energy[3] + site_energy[2] + 2 * U
        array[54][54] = array[55][55] = 2 * site_energy[1] + 2 * site_energy[2] + site_energy[3] + 2 * U

        # jump parameter

        for i in range(0, 24, 1):
            array[8 + i][0 + i] = array[0 + i][8 + i] = t

        array[0][24] = array[24][0] = t
        array[1][28] = array[28][1] = t
        array[3][25] = array[25][3] = t
        array[4][29] = array[29][4] = t
        array[5][26] = array[26][5] = t
        array[6][30] = array[30][6] = t
        array[7][27] = array[27][7] = t
        array[8][31] = array[31][8] = t

        array[1][34] = array[34][1] = array[40][1] = array[1][40] = -t

        array[2][34] = array[34][2] = array[40][2] = array[2][40] = t
        array[2][38] = array[38][2] = array[44][2] = array[2][44] = -t

        array[3][39] = array[39][3] = array[45][3] = array[3][45] = -t

        array[4][38] = array[38][4] = array[44][4] = array[4][44] = t

        array[5][39] = array[39][5] = array[45][5] = array[5][45] = t
        array[5][35] = array[35][5] = array[41][5] = array[5][41] = -t

        array[6][35] = array[35][6] = array[41][6] = array[6][41] = t

        array[9][32] = array[32][9] = array[52][9] = array[9][52] = t
        array[9][36] = array[36][9] = array[42][9] = array[9][42] = -t

        array[10][36] = array[36][10] = array[42][10] = array[10][42] = t

        array[11][33] = array[33][11] = array[53][11] = array[11][53] = t

        array[12][32] = array[32][12] = array[52][12] = array[12][52] = -t

        array[13][37] = array[37][13] = array[43][13] = array[13][43] = -t

        array[14][33] = array[33][14] = array[53][14] = array[14][53] = -t
        array[14][37] = array[37][14] = array[43][14] = array[14][43] = t

        array[17][34] = array[34][17] = array[50][17] = array[17][50] = t

        array[14][37] = array[37][14] = array[43][14] = array[14][43] = t

        array[18][44] = array[44][18] = array[54][18] = array[18][54] = -t

        array[19][35] = array[35][19] = array[51][19] = array[19][51] = t
        array[19][45] = array[45][19] = array[55][19] = array[19][55] = -t

        array[20][34] = array[34][20] = array[50][20] = array[20][50] = -t
        array[20][44] = array[44][20] = array[54][20] = array[20][54] = t

        array[21][45] = array[45][21] = array[55][21] = array[21][55] = t

        array[22][35] = array[35][22] = array[51][22] = array[22][51] = -t

        array[25][42] = array[42][25] = array[48][25] = array[25][48] = -t

        array[26][42] = array[42][26] = array[48][26] = array[26][48] = t
        array[26][46] = array[46][26] = array[52][26] = array[26][52] = -t

        array[27][47] = array[47][27] = array[53][27] = array[27][53] = -t

        array[28][46] = array[46][28] = array[52][28] = array[28][52] = t

        array[29][47] = array[47][29] = array[53][29] = array[29][53] = t
        array[29][43] = array[43][29] = array[49][29] = array[29][49] = -t

        array[30][43] = array[43][30] = array[49][30] = array[30][49] = t

        array[32][34] = array[34][32] = array[33][35] = array[35][33] = t
        array[32][38] = array[38][32] = array[33][39] = array[39][33] = -t

        array[34][36] = array[36][34] = array[35][37] = array[37][35] = t

        array[36][54] = array[54][36] = array[37][55] = array[55][37] = -t

        array[38][42] = array[42][38] = array[39][43] = array[43][39] = t

        array[40][42] = array[42][40] = array[41][43] = array[43][41] = t
        array[40][46] = array[46][40] = array[41][47] = array[47][41] = -t

        array[44][46] = array[46][44] = array[45][47] = array[47][45] = t
        array[44][48] = array[48][44] = array[45][49] = array[49][45] = -t

        array[50][48] = array[48][50] = array[49][51] = array[51][49] = -t

        array[52][50] = array[50][52] = array[51][53] = array[53][51] = t

        array[52][54] = array[54][52] = array[53][55] = array[55][53] = t

    # finished
    if case_number == 6:

        # site energy
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

        # jump parameter

        for i in range(0, 20, 1):
            array[4][0] = array[0][4] = t

        array[12][0] = array[0][12] = -t
        array[14][1] = array[1][14] = -t
        array[13][2] = array[2][13] = -t
        array[15][3] = array[3][15] = -t

        array[20][4] = array[4][20] = t
        array[21][5] = array[5][21] = t
        array[22][6] = array[6][22] = t
        array[23][7] = array[7][23] = t

        array[1][24] = array[24][1] = array[1][25] = array[25][1] = -t
        array[2][24] = array[24][2] = array[2][25] = array[25][2] = t

        array[9][24] = array[24][9] = array[9][27] = array[27][9] = -t
        array[10][24] = array[24][10] = array[10][27] = array[27][10] = t

        array[17][26] = array[26][17] = array[17][27] = array[27][17] = -t
        array[18][26] = array[26][18] = array[18][27] = array[27][18] = t

        array[21][25] = array[25][21] = array[21][26] = array[26][21] = -t
        array[22][25] = array[25][22] = array[22][26] = array[26][22] = t

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


def calc_eigenvalue_array(array_for_calc, number_of_case):
    if number_of_case != 8 or number_of_case != 0:
        intermediate_stage, _ = np.linalg.eig(array_for_calc)
        # print("intermediate_stage = ", intermediate_stage)
        return intermediate_stage

    else:
        return array_for_calc


def calc_eigenvectors_of_an_array(array_for_calc):

    _, intermediate_stage = np.linalg.eig(array_for_calc)
        #print("intermediate of vector array = \n", intermediate_stage)

    return intermediate_stage


def data_frame_to_csv_array(case_number, array, name, directory_name):
    if case_number == 1:
        df = pd.DataFrame(array,
                          index=['u000', '0u00', '00u0', '000u', 'd000', '0d00', '00d0', '000d'],
                          columns=['u000', '0u00', '00u0', '000u', 'd000', '0d00', '00d0', '000d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 2:
        df = pd.DataFrame(array,
                          index=['ud00', 'du00', 'uu00', 'dd00', 'u0d0', 'd0u0', 'u0u0', 'd0d0', 'u00d', 'd00u', 'u00u',
                                 'd00d', '0ud0', '0du0', '0uu0', '0dd0', '0u0d', '0d0u', '0u0u', \
                                 '0d0d', '00ud', '00du', '00uu', '00dd', '2000', '0200', '0020', '0002'],
                          columns=['ud00', 'du00', 'uu00', 'dd00', 'u0d0', 'd0u0', 'u0u0', 'd0d0', 'u00d', 'd00u',
                                   'u00u', 'd00d', '0ud0', '0du0', '0uu0', '0dd0', '0u0d', '0d0u', '0u0u', \
                                   '0d0d', '00ud', '00du', '00uu', '00dd', '2000', '0200', '0020', '0002'])
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 3:
        df = pd.DataFrame(array,
                          index=['uuu0', 'uud0', 'udu0', 'udd0', 'duu0', 'dud0', 'ddu0', 'ddd0', 'uu0u', 'uu0d', 'ud0u',
                                 'ud0d', \
                                 'du0u', 'du0d', 'dd0u', 'dd0d', 'u0uu', 'u0ud', 'u0du', 'u0dd', 'd0uu', 'd0ud', 'd0du',
                                 'd0dd', '0uuu', '0uud', \
                                 '0udu', '0udd', '0duu', '0dud', '0ddu', '0ddd', 'u200', 'd200', '2u00', '2d00', 'u020',
                                 'd020', '20u0', '20d0', \
                                 'u002', 'd002', '200u', '200d', '0u20', '0d20', '02u0', '02d0', '0u02', '0d02', '020u',
                                 '020d', '00u2', '00d2', '002u', '002d'],

                          columns=['uuu0', 'uud0', 'udu0', 'udd0', 'duu0', 'dud0', 'ddu0', 'ddd0', 'uu0u', 'uu0d',
                                   'ud0u', 'ud0d', \
                                   'du0u', 'du0d', 'dd0u', 'dd0d', 'u0uu', 'u0ud', 'u0du', 'u0dd', 'd0uu', 'd0ud',
                                   'd0du', 'd0dd', '0uuu', '0uud', \
                                   '0udu', '0udd', '0duu', '0dud', '0ddu', '0ddd', 'u200', 'd200', '2u00', '2d00',
                                   'u020', 'd020', '20u0', '20d0', \
                                   'u002', 'd002', '200u', '200d', '0u20', '0d20', '02u0', '02d0', '0u02', '0d02',
                                   '020u', '020d', '00u2', '00d2', '002u', '002d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 4:
        df = pd.DataFrame(array,
                          index=['uuuu', 'uuud', 'uudu', 'uudd', 'uduu', 'udud', 'uddu', 'uddd', 'duuu', 'duud', 'dudu',
                                 'dudd', 'dduu', 'ddud', 'dddu', \
                                 'dddd', '2uu0', '2ud0', '2du0', '2dd0', 'u2u0', 'u2d0', 'd2u0', 'd2d0', 'uu20', 'ud20',
                                 'du20', 'dd20', '2u0u', '2u0d', \
                                 '2d0u', '2d0d', 'u20u', 'u20d', 'd20u', 'd20d', 'uu02', 'ud02', 'du02', 'dd02', '20uu',
                                 '20ud', '20du', '20dd', 'u02u', \
                                 'u02d', 'd02u', 'd02d', 'u0u2', 'u0d2', 'd0u2', 'd0d2', '02uu', '02ud', '02du', '02dd',
                                 '0u2u', '0u2d', '0d2u', '0d2d', \
                                 '0uu2', '0ud2', '0du2', '0dd2', '2200', '2020', '2002', '0220', '0202', '0022'],
                          columns=['uuuu', 'uuud', 'uudu', 'uudd', 'uduu', 'udud', 'uddu', 'uddd', 'duuu', 'duud',
                                   'dudu', 'dudd', 'dduu', 'ddud', 'dddu', \
                                   'dddd', '2uu0', '2ud0', '2du0', '2dd0', 'u2u0', 'u2d0', 'd2u0', 'd2d0', 'uu20',
                                   'ud20', 'du20', 'dd20', '2u0u', '2u0d', \
                                   '2d0u', '2d0d', 'u20u', 'u20d', 'd20u', 'd20d', 'uu02', 'ud02', 'du02', 'dd02',
                                   '20uu', '20ud', '20du', '20dd', 'u02u', \
                                   'u02d', 'd02u', 'd02d', 'u0u2', 'u0d2', 'd0u2', 'd0d2', '02uu', '02ud', '02du',
                                   '02dd', '0u2u', '0u2d', '0d2u', '0d2d', \
                                   '0uu2', '0ud2', '0du2', '0dd2', '2200', '2020', '2002', '0220', '0202', '0022']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 5:
        df = pd.DataFrame(array,
        index=['2uuu',	'2uud',	'2udu',	'2udd',	'2duu',	'2dud',	'2ddu',	'2ddd',	'u2uu',	'u2ud',	'u2du',	'u2dd',	'd2uu',	'd2ud',	'd2du',	'd2dd',	'uu2u',	'uu2d',	'ud2u',	'ud2d',	'du2u',	'du2d',	'dd2u',	'dd2d',\
               'uuu2',	'uud2',	'udu2',	'udd2',	'duu2',	'dud2',	'ddu2',	'ddd2',	'22u0',	'22d0',	'2u20',	'2d20',	'u220',	'd220',	'220u',	'220d',	'2u02',	'2d02',	'u202',	'd202',	'202u',	'202d',	'20u2',	'20d2',\
               'u022',	'd022',	'0u22',	'0d22',	'02u2',	'02d2',	'022u',	'022d'],
        columns=['2uuu',	'2uud',	'2udu',	'2udd',	'2duu',	'2dud',	'2ddu',	'2ddd',	'u2uu',	'u2ud',	'u2du',	'u2dd',	'd2uu',	'd2ud',	'd2du',	'd2dd',	'uu2u',	'uu2d',	'ud2u',	'ud2d',	'du2u',	'du2d',	'dd2u',	'dd2d',\
               'uuu2',	'uud2',	'udu2',	'udd2',	'duu2',	'dud2',	'ddu2',	'ddd2',	'22u0',	'22d0',	'2u20',	'2d20',	'u220',	'd220',	'220u',	'220d',	'2u02',	'2d02',	'u202',	'd202',	'202u',	'202d',	'20u2',	'20d2',\
               'u022',	'd022',	'0u22',	'0d22',	'02u2',	'02d2',	'022u',	'022d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 6:
        df = pd.DataFrame(array,
                          index=['22uu', '22ud', '22du', '22dd', '2u2u', '2u2d', '2d2u', '2d2d', 'u22u', 'u22d', 'd22u',
                                 'd22d', 'u2u2', 'u2d2', \
                                 'd2u2', 'd2d2', 'uu22', 'ud22', 'du22', 'dd22', '2uu2', '2ud2', '2du2', '2dd2', '2220',
                                 '2202', '2022', '0222'],
                          columns=['22uu', '22ud', '22du', '22dd', '2u2u', '2u2d', '2d2u', '2d2d', 'u22u', 'u22d',
                                   'd22u', 'd22d', 'u2u2', 'u2d2', \
                                   'd2u2', 'd2d2', 'uu22', 'ud22', 'du22', 'dd22', '2uu2', '2ud2', '2du2', '2dd2',
                                   '2220', '2202', '2022', '0222']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 7:
        df = pd.DataFrame(array,
                          index=['222u', '22u2', '2u22', 'u222', '222d', '22d2', '2d22', 'd222'],
                          columns=['222u', '22u2', '2u22', 'u222', '222d', '22d2', '2d22', 'd222']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")


def data_frame_to_csv_value(case_number, array, name, directory_name):
    if case_number == 1:
        df = pd.DataFrame(array,
                          index=['u000', '0u00', '00u0', '000u', 'd000', '0d00', '00d0', '000d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 2:
        df = pd.DataFrame(array,
                          index=['ud00', 'du00', 'uu00', 'dd00', 'u0d0', 'd0u0', 'u0u0', 'd0d0', 'u00d', 'd00u', 'u00u',
                                 'd00d', '0ud0', '0du0', '0uu0', '0dd0', '0u0d', '0d0u', '0u0u', \
                                 '0d0d', '00ud', '00du', '00uu', '00dd', '2000', '0200', '0020', '0002'])
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 3:
        df = pd.DataFrame(array,
                          index=['uuu0', 'uud0', 'udu0', 'udd0', 'duu0', 'dud0', 'ddu0', 'ddd0', 'uu0u', 'uu0d', 'ud0u',
                                 'ud0d', \
                                 'du0u', 'du0d', 'dd0u', 'dd0d', 'u0uu', 'u0ud', 'u0du', 'u0dd', 'd0uu', 'd0ud', 'd0du',
                                 'd0dd', '0uuu', '0uud', \
                                 '0udu', '0udd', '0duu', '0dud', '0ddu', '0ddd', 'u200', 'd200', '2u00', '2d00', 'u020',
                                 'd020', '20u0', '20d0', \
                                 'u002', 'd002', '200u', '200d', '0u20', '0d20', '02u0', '02d0', '0u02', '0d02', '020u',
                                 '020d', '00u2', '00d2', '002u', '002d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 4:
        df = pd.DataFrame(array,
                          index=['uuuu', 'uuud', 'uudu', 'uudd', 'uduu', 'udud', 'uddu', 'uddd', 'duuu', 'duud', 'dudu',
                                 'dudd', 'dduu', 'ddud', 'dddu', \
                                 'dddd', '2uu0', '2ud0', '2du0', '2dd0', 'u2u0', 'u2d0', 'd2u0', 'd2d0', 'uu20', 'ud20',
                                 'du20', 'dd20', '2u0u', '2u0d', \
                                 '2d0u', '2d0d', 'u20u', 'u20d', 'd20u', 'd20d', 'uu02', 'ud02', 'du02', 'dd02', '20uu',
                                 '20ud', '20du', '20dd', 'u02u', \
                                 'u02d', 'd02u', 'd02d', 'u0u2', 'u0d2', 'd0u2', 'd0d2', '02uu', '02ud', '02du', '02dd',
                                 '0u2u', '0u2d', '0d2u', '0d2d', \
                                 '0uu2', '0ud2', '0du2', '0dd2', '2200', '2020', '2002', '0220', '0202', '0022']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 5:
        df = pd.DataFrame(array,
        index=['2uuu',	'2uud',	'2udu',	'2udd',	'2duu',	'2dud',	'2ddu',	'2ddd',	'u2uu',	'u2ud',	'u2du',	'u2dd',	'd2uu',	'd2ud',	'd2du',	'd2dd',	'uu2u',	'uu2d',	'ud2u',	'ud2d',	'du2u',	'du2d',	'dd2u',	'dd2d',\
               'uuu2',	'uud2',	'udu2',	'udd2',	'duu2',	'dud2',	'ddu2',	'ddd2',	'22u0',	'22d0',	'2u20',	'2d20',	'u220',	'd220',	'220u',	'220d',	'2u02',	'2d02',	'u202',	'd202',	'202u',	'202d',	'20u2',	'20d2',\
               'u022',	'd022',	'0u22',	'0d22',	'02u2',	'02d2',	'022u',	'022d']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 6:
        df = pd.DataFrame(array,
                          index=['22uu', '22ud', '22du', '22dd', '2u2u', '2u2d', '2d2u', '2d2d', 'u22u', 'u22d', 'd22u',
                                 'd22d', 'u2u2', 'u2d2', \
                                 'd2u2', 'd2d2', 'uu22', 'ud22', 'du22', 'dd22', '2uu2', '2ud2', '2du2', '2dd2', '2220',
                                 '2202', '2022', '0222']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")

    if case_number == 7:
        df = pd.DataFrame(array,
                          index=['222u', '22u2', '2u22', 'u222', '222d', '22d2', '2d22', 'd222']
                          )
        df.to_csv(str(directory_name) + '/' + str(name) + '_' + str(case_number) + ".csv", sep=";")