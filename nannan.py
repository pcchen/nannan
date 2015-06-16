import re
import unicodedata

def syllable_structure(syllable):
  # lan2 -> l+a+n+2
  # tshuinn -> tsh+ui+nn+None
  Onset='^(tsh|chh|ts|ch|th|kh|ph|ng|p|m|b|t|n|l|k|g|s|j|h)?'
  Nucleus='(uai|iau|ua|ue|ui|ia|io|iu|oo|au|ai|a|e|i|o|u|m|ng)'
  Coda='(hnn|nnh|nn|h|ng|m|n|p|t|k|)'
  Tone='([0-9])?$'

  syllable=syllable.strip()
  STRUCTURE_RE=re.compile(Onset+Nucleus+Coda+Tone,re.IGNORECASE)
  syllable_match=STRUCTURE_RE.match(syllable)
  if syllable_match:
    word_syllable=syllable_match.group(0)
    if syllable_match.group(1) is None:
      word_syllable_onset=''
    else:
      word_syllable_onset=syllable_match.group(1)
    word_syllable_nucleus=syllable_match.group(2)
    word_syllable_coda=syllable_match.group(3)
    if word_syllable_coda in ['m','n','ng','nn']:
        if syllable_match.group(4) is None:
            word_syllable_tone='1'
        else:
            word_syllable_tone=syllable_match.group(4)
    else:
        if syllable_match.group(4) is None:
            word_syllable_tone='4'
        else:
            word_syllable_tone=syllable_match.group(4)

    # print(syllable_match.group(0))
    # print(syllable_match.group(1))
    # print(syllable_match.group(2))
    # print(syllable_match.group(3))
    # print(syllable_match.group(4))

    word_structure=syllable+'='+word_syllable_onset+'+'+word_syllable_nucleus+'+'+word_syllable_coda
    # print(word_structure)

    if word_syllable == syllable:
      word_structure=syllable+'='+word_syllable_onset+'+'+word_syllable_nucleus+'+'+word_syllable_coda
      return word_syllable_onset, word_syllable_nucleus, word_syllable_coda,word_syllable_tone
    else:
      print('error')
      return False

  else:
    print('no match')
    return False

def syllable_2_alphanum(syllable):
  # convert a syllable in unicode to alphanum representation
  # oo & nn
  oo_uni=u'\u0358'
  nn_uni=u'ⁿ'
  #
  tone2_uni=u'\u0301'
  tone3_uni=u'\u0300'
  tone5_uni=u'\u0302'
  tone7_uni=u'\u0304'
  tone8_uni=u'\u030d'
  #
  tone6_uni=u'\u0301'
  tone9_uni=u'\u0301'

  #
  syllable_alphanum=unicodedata.normalize('NFD',syllable)
  # replace the unicode tones by number tones
  # á -> 'a'+u'\u0301' ,etc
  syllable_alphanum=syllable_alphanum.replace(tone2_uni,'2')
  syllable_alphanum=syllable_alphanum.replace(tone3_uni,'3')
  syllable_alphanum=syllable_alphanum.replace(tone5_uni,'5')
  syllable_alphanum=syllable_alphanum.replace(tone7_uni,'7')
  syllable_alphanum=syllable_alphanum.replace(tone8_uni,'8')
  # POJ orthography
  syllable_alphanum=syllable_alphanum.replace(oo_uni,'o')
  syllable_alphanum=syllable_alphanum.replace(nn_uni,'nn')

  # print('syllable_alphanum=',syllable_alphanum)
  tone = ""
  tone_re = re.compile("[0-9]")
  # find all the number tones
  m = tone_re.findall(syllable_alphanum)
  if len(m) == 0:
    # 1th or 4h tone
    if syllable_structure(syllable_alphanum):
      return syllable_alphanum
    else:
      print('invalid')
  elif len(m) == 1:
    # print m
    syllable_alphanum=tone_re.sub('',syllable_alphanum)
    # print('return', syllable_alphanum+m[0])
    return syllable_alphanum+m[0]
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
