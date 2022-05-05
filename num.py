import random


def make_rnd_list(length):
    each_num_list = []
    [each_num_list.append(i) for i in range(1, 10, 1)]
    random.shuffle(each_num_list)
    return each_num_list[:length]


def input_num_list(length):
    num_list = []
    for i in range(length):
        num_list.append(int(input('{}桁目の予想を入力（0～9）>>'.format(i + 1))))
    return num_list


def match_input_make_list(make_list, input_list):
    hit = 0
    ball = 0
    for i in range(0, len(make_list), 1):
        for j in range(0, len(input_list), 1):
            if make_list[i] == input_list[j]:
                if i == j:
                    hit += 1
                else:
                    ball += 1
    return hit, ball
