from nannan import *

# valid

# print(syllable_structure('chhuann'))
# print(syllable_structure('tshann'))
# print(syllable_structure('hm7'))
# print(syllable_structure('ah'))
# print(syllable_structure('ap8'))
# s = s_structure('tshuann')
# s['onset'] = s['onset'].replace('chh','tsh')
# print(s['onset'])

# test syllable_2_alphanum(syllable)
# print(syllable_2_alphanum('lán'))
# print(syllable_2_alphanum('tsi̍t'))
# print(syllable_2_alphanum('chi̍t'))
# print(syllable_2_alphanum('o͘-ji̍t'))
# print('îⁿ', s_unicode_2_ascii('îⁿ'))
# print('o͘', s_unicode_2_ascii('o͘'))

# POJ -> TL

# 單音節白話字轉台羅
# print('POJ_unicode', 'POJ_ascii', 'TL_ascii')
# POJ_unicode = ['góa','goá','chhòa','chò','he̍k','hōe','êng','īⁿ']
#
# for poj_u in POJ_unicode:
#     poj_ascii = s_unicode_2_ascii(poj_u)
#     tl_ascii = s_ascii_2_TL(poj_ascii)
#     print(poj_u, poj_ascii, tl_ascii)

# 多音節白話字轉台羅
W_POJ_unicode = ['tâi-oân-lâng','joa̍h--sí']
print('POJ_unicode', 'POJ_ascii', 'TL_ascii')
for w_u in W_POJ_unicode:
    w_ascii = w_unicode_2_ascii(w_u)
    w_ascii_TL = w_unicode_2_ascii_TL(w_u)
    print(w_u, w_ascii, w_ascii_TL)
