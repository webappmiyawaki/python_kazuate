from num import make_rnd_list
from num import input_num_list
from num import match_input_make_list

print('数あてゲームを始めます。n桁の数字を当ててください！')
LENGTH = int(input('まず、桁数を決めます。\n1-9の数字を入力してください>>'))
print()
ans_list = make_rnd_list(LENGTH)

print('answer:{}'.format(ans_list))

is_loop = True
while is_loop:
    num_list = input_num_list(LENGTH)
    result = match_input_make_list(ans_list, num_list)
    print('ヒット{}本,ボール{}本'.format(str(result[0]).zfill(2), str(result[1]).zfill(2)))

    if result[0] == len(ans_list):
        print('正解です！')
        is_loop = False
    else:
        text = input('続けますか？ 1:続ける 2:終了>>')
        if text == '2':
            print('正解は{}です'.format(ans_list))
            is_loop = False
        else:
            print('続行します\n')

print('ゲーム終了')
