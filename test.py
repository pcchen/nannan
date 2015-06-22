from nannan import *

# 單音節白話字轉台羅
print('POJ_unicode', 'POJ_ascii', 'TL_ascii')
unicode = ['góa','goá','chhòa','chò','he̍k','hōe','êng','īⁿ']

for u in unicode:
    ascii = s_unicode_2_ascii(u)
    tl_ascii = s_ascii_2_TL(ascii)
    print(u, ascii, tl_ascii)
print()

# 多音節白話字轉台羅
W_POJ_unicode = ['tâi-oân-lâng', 'tâi-uân-lâng', 'joa̍h--sí']
print('unicode', 'ascii', 'POJ_ascii', 'TL_ascii')

for w_u in W_POJ_unicode:
    w_ascii = w_unicode_2_ascii(w_u)
    w_ascii_POJ = w_unicode_2_ascii(w_u, format='POJ')
    w_ascii_TL = w_unicode_2_ascii(w_u, format='TL')
    print(w_u, w_ascii, w_ascii_POJ, w_ascii_TL)
print()

# 純羅馬字字串轉數羅碼
print(LoStr_2_ascii('GOá ek eK Ek EK gÓ sī tâi-uân-lâng cHhe che Che CHe sī oa oe ou'))
print(LoStr_2_ascii('GOá ek eK Ek EK gÓ sī tâi-uân-lâng cHhe che Che CHe sī oa oe ou', format='TL'))
print(LoStr_2_ascii('GUa2 ik iK Ik IK gO2 si7 tai5-uan5-lang5 tShe tse Tse TSe si7 ua ue oo', format='POJ'))
