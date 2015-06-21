import re
import unicodedata

# naming convention
# s: syllable
# slist: word in syllable list
# w: word
# unicode: unicode representation
# ascii: ascii alpha-num representation

# TL: TL orthography
# POJ: POJ orthography

# ok s_ascii_2_TL(syllable)
# ok s_ascii_2_POJ(syllable)
# ? s_unicode_2_ascii(syllable)

# s_ascii_2_unicode(syllable, format)

# s_structure(syllable)

# Han
# Lo

def LoStr_2_ascii_TL(str):
    """convert a string in Latin into ascii TL"""
    WList = str.split()
    for i in range(len(WList)):
        WList[i] = w_unicode_2_ascii_TL(WList[i])
    return ' '.join(WList)

def LoStr_2_ascii_POJ(str):
    """convert a string in Latin into ascii POJ"""
    WList = str.split()
    for i in range(len(WList)):
        WList[i] = w_unicode_2_ascii_POJ(WList[i])
    return ' '.join(WList)


def w_2_slist(word):
    # tâi-uân-lâng -> ['tâi','uân,'lâng']
    # i--ê -> ['i','','ê']
    slist=word.split('-')
    return slist

def w_unicode_2_ascii(word):
    slist = w_2_slist(word)
    for i in range(len(slist)):
        if slist[i] != '':
            slist[i] = s_unicode_2_ascii(slist[i])
    return '-'.join(slist)

def w_unicode_2_ascii_TL(word):
    slist = w_2_slist(word)
    for i in range(len(slist)):
        if slist[i] != '':
            s = s_unicode_2_ascii(slist[i])
            slist[i] = s_ascii_2_TL(s)
    return '-'.join(slist)

def w_unicode_2_ascii_POJ(word):
    slist = w_2_slist(word)
    for i in range(len(slist)):
        if slist[i] != '':
            s = s_unicode_2_ascii(slist[i])
            slist[i] = s_ascii_2_POJ(s)
    return '-'.join(slist)


def s_ascii_convert(syllable, format='TL'):
    """convert syllable in ascii representation to TL form"""

    ch_ts = [ ('ch','ts'), ('Ch','Ts'), ('cH','tS'), ('CH','TS') ]
    e_i = [ ('e', 'i'), ('E', 'I')]
    oa_ua = [ ('oa','ua'), ('Oa','Ua'), ('oA','uA'), ('OA','UA') ]
    oe_ue = [ ('oe','ue'), ('Oe','Ue'), ('oE','uE'), ('OE','UE') ]
    ou_oo = [ ('ou','oo'), ('Ou','Oo'), ('oU','oO'), ('OU','OO') ]

    k_ng = ['k', 'K', 'ng', 'Ng', 'nG', 'NG']

    s = s_structure(syllable)
    if s != None:
        if format == 'TL':
            # ch -> ts, chh -> tsh
            for (ch, ts) in ch_ts:
                s['onset'] = s['onset'].replace(ch, ts)
            # ek -> ik, eng -> ing
            if s['coda'] in k_ng:
                for (e, i) in e_i:
                    s['nucleus'] = s['nucleus'].replace(e, i)
            # oa -> ua
            for (oa, ua) in oa_ua:
                s['nucleus'] = s['nucleus'].replace(oa, ua)
            # oe -> ue
            for (oe, ue) in oe_ue:
                s['nucleus'] = s['nucleus'].replace(oe, ue)
            # ou -> oo
            for (ou, oo) in ou_oo:
                s['nucleus'] = s['nucleus'].replace(ou, oo)

            if s['tone'] == '1' or s['tone'] == '4':
                return s['onset'] + s['nucleus'] + s['coda']
            else:
                return s['onset'] + s['nucleus'] + s['coda'] + s['tone']

        elif format == 'POJ':
            # ch <- ts, chh <- tsh
            for (ch, ts) in ch_ts:
                s['onset'] = s['onset'].replace(ts, ch)
            # s['onset'] = s['onset'].replace('ts','ch')
            # ek <- ik, eng <- ing
            if s['coda'] in k_ng:
                for (e, i) in e_i:
                    s['nucleus'] = s['nucleus'].replace(i, e)
            # oa <- ua
            for (oa, ua) in oa_ua:
                s['nucleus'] = s['nucleus'].replace(ua, oa)
            # s['nucleus'] = s['nucleus'].replace('ua','oa')
            # oe <- ue
            for (oe, ue) in oe_ue:
                s['nucleus'] = s['nucleus'].replace(ue, oe)
            # s['nucleus'] = s['nucleus'].replace('ue','oe')
            # ou <- oo
            for (ou, oo) in ou_oo:
                s['nucleus'] = s['nucleus'].replace(oo, ou)
            # s['nucleus'] = s['nucleus'].replace('oo','ou')

            if s['tone'] == '1' or s['tone'] == '4':
                return s['onset'] + s['nucleus'] + s['coda']
            else:
                return s['onset'] + s['nucleus'] + s['coda'] + s['tone']

        else:
            return(syllable)
    else:
        return(syllable)

def s_ascii_2_TL(syllable):
    """convert syllable in ascii representation to TL form"""
    return s_ascii_convert(syllable, format='TL')

def s_ascii_2_POJ(syllable):
    """convert syllable in ascii representation to POJ form"""
    return s_ascii_convert(syllable, format='POJ')

def s_structure(syllable):
    """return the structure of a syllable as a dictionary"""
    # lan2 -> l+a+n+2
    # tshuinn -> tsh+ui+nn+None
    # print(syllable)
    Onset = '^(tsh|chh|ts|ch|th|kh|ph|ng|p|m|b|t|n|l|k|g|s|j|h)?'
    Nucleus = '(uai|iau|ua|oa|ue|oe|ui|ia|io|iu|oo|ou|au|ai|a|e|i|o|u|m|ng)'
    Coda = '(hnn|nnh|nn|h|ng|m|n|p|t|k|)'
    Tone = '([0-9])?$'

    syllable = syllable.strip()

    STRUCTURE_RE = re.compile(Onset + Nucleus + Coda + Tone, re.IGNORECASE)
    syllable_match = STRUCTURE_RE.match(syllable)
    if syllable_match:
        word_syllable = syllable_match.group(0)
        if syllable_match.group(1) is None:
            word_syllable_onset = ''
        else:
            word_syllable_onset = syllable_match.group(1)
        word_syllable_nucleus = syllable_match.group(2)
        word_syllable_coda = syllable_match.group(3)
        if word_syllable_coda in ['m', 'n', 'ng', 'nn']:
            if syllable_match.group(4) is None:
                word_syllable_tone = '1'
            else:
                word_syllable_tone = syllable_match.group(4)
        else:
            if syllable_match.group(4) is None:
                word_syllable_tone = '4'
            else:
                word_syllable_tone = syllable_match.group(4)

        # print(syllable_match.group(0))
        # print(syllable_match.group(1))
        # print(syllable_match.group(2))
        # print(syllable_match.group(3))
        # print(syllable_match.group(4))

        word_structure = syllable + '=' + word_syllable_onset + \
            '+' + word_syllable_nucleus + '+' + word_syllable_coda
        # print(word_structure)

        if word_syllable == syllable:
            word_structure = syllable + '=' + word_syllable_onset + \
                '+' + word_syllable_nucleus + '+' + word_syllable_coda
            s = {'onset':word_syllable_onset, 'nucleus':word_syllable_nucleus, 'coda':word_syllable_coda, 'tone':word_syllable_tone }
            # return word_syllable_onset, word_syllable_nucleus, word_syllable_coda, word_syllable_tone
            return s
        else:
            print('error')
            return False

    else:
        print('no match--')
        # return syllable
        return None

def s_unicode_2_ascii(syllable):
    """convert syllable in unicode representation to ascii representation"""

    # oo & nn
    oo_uni = u'\u0358'
    nn_uni = u'ⁿ' # need to fix capital superscript N
    #
    tone2_uni = u'\u0301'
    tone3_uni = u'\u0300'
    tone5_uni = u'\u0302'
    tone7_uni = u'\u0304'
    tone8_uni = u'\u030d'
    # fix me
    tone6_uni = u'\u0301'
    tone9_uni = u'\u0301'

    #
    s_ascii = unicodedata.normalize('NFD', syllable)
    # á -> a+u'\u0301' -> a2
    s_ascii = s_ascii.replace(tone2_uni, '2')
    s_ascii = s_ascii.replace(tone3_uni, '3')
    s_ascii = s_ascii.replace(tone5_uni, '5')
    s_ascii = s_ascii.replace(tone7_uni, '7')
    s_ascii = s_ascii.replace(tone8_uni, '8')
    # need to add tone6,9

    # o͘ -> o+u'\u0358' -> oo
    s_ascii = s_ascii.replace(oo_uni, 'o')
    # ⁿ -> nn
    s_ascii = s_ascii.replace(nn_uni, 'nn')

    # print('s_ascii=',s_ascii)
    tone = ""
    tone_re = re.compile("[0-9]")

    # find all the number tones
    m = tone_re.findall(s_ascii)
    # print(m)
    if len(m) == 0:
        # 1th or 4h tone
        if s_structure(s_ascii):
            return s_ascii
        else:
            print('invalid')
    elif len(m) == 1:
        # print m
        s_ascii = tone_re.sub('', s_ascii)
        # print('return', syllable_alphanum+m[0])
        return s_ascii + m[0]
    else:
        # not a valid syllable, return original syllable without any conversion
        # print('return', syllable)
        return syllable
    # print m
    # if m:
    #   for each in m:
    #     # tone = m.group(0)
    #     # tone=
    #     print each
    #     # syllable_alphanum = tone_re.sub("", syllable_alphanum)
    #     syllable_alphanum=syllable_alphanum + each
    # return syllable_alphanum
