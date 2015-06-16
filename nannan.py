import re

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
