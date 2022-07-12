from .modules import initials_register, finals_register, zero_initial_finals_register, Style, Mode

import pypinyin


def shuangpin(hans, mode=Mode.xiaohe, style=Style.NORMAL, heteronym=False):
    try:
        if style == Style.NORMAL:
            initials = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.INITIALS,
                                       strict=False, neutral_tone_with_five=True)
            finals = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.FINALS,
                                     errors=lambda x: [''], strict=False, neutral_tone_with_five=True)
            initials_tran = [[initials_register[mode](j) for j in i] for i in initials]
            finals_tran = [[finals_register[mode](j) for j in i] for i in finals]
            return [[zero_initial_finals_register[mode](finals[x][y]) if j[0] == '' else j[0] + j[1]
                     for y, j in enumerate(zip(i[0], i[1]))] for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.TONE:
            initials = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.INITIALS, strict=False,
                                       neutral_tone_with_five=True)
            finals = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.FINALS_TONE3,
                                     errors=lambda x: [' '], strict=False, neutral_tone_with_five=True)
            initials_tran = [[initials_register[mode](j) for j in i] for i in initials]
            finals_tran = [[finals_register[mode](j[:-1]) for j in i] for i in finals]
            return [[zero_initial_finals_register[mode](finals[x][y][:-1]) + finals[x][y][-1]
                     if j[0] == '' else j[0] + j[1] + finals[x][y][-1]
                     for y, j in enumerate(zip(i[0], i[1]))] for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.INITIALS:
            initials = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.INITIALS, strict=False,
                                       neutral_tone_with_five=True)
            finals = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.FINALS, strict=False,
                                     neutral_tone_with_five=True)
            initials_tran = [[initials_register[mode](j) for j in i] for i in initials]
            finals_tran = [[finals_register[mode](j) for j in i] for i in finals]
            return [[zero_initial_finals_register[mode](finals[x][y])[0] if j[0] == '' else j[0]
                     for y, j in enumerate(zip(i[0], i[1]))] for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.FINALS:
            initials = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.INITIALS, strict=False,
                                       neutral_tone_with_five=True)
            finals = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.FINALS, strict=False,
                                     neutral_tone_with_five=True)
            initials_tran = [[initials_register[mode](j) for j in i] for i in initials]
            finals_tran = [[finals_register[mode](j) for j in i] for i in finals]
            return [[zero_initial_finals_register[mode](finals[x][y])[1] if j[0] == '' else j[1]
                     for y, j in enumerate(zip(i[0], i[1]))] for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.FINALS_TONE:
            initials = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.INITIALS, strict=False,
                                       neutral_tone_with_five=True)
            finals = pypinyin.pinyin(hans, heteronym=heteronym, style=pypinyin.FINALS_TONE3, strict=False,
                                     neutral_tone_with_five=True)
            initials_tran = [[initials_register[mode](j) for j in i] for i in initials]
            finals_tran = [[finals_register[mode](j[:-1]) for j in i] for i in finals]
            return [[zero_initial_finals_register[mode](finals[x][y][:-1])[1] + finals[x][y][-1]
                     if j[0] == '' else j[1] + finals[x][y][-1]
                     for y, j in enumerate(zip(i[0], i[1]))] for x, i in enumerate(zip(initials_tran, finals_tran))]
        else:
            raise ValueError('style must be one of NORMAL, TONE, INITIALS, FINALS, FINALS_TONE')
    except KeyError:
        print("mode not found:", mode)
        return None


def lazy_shuangpin(hans, mode=Mode.xiaohe, style=Style.NORMAL, tone_sandhi=False):
    try:
        if style == Style.NORMAL:
            initials = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.INITIALS,
                                            strict=False, neutral_tone_with_five=True)
            finals = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.FINALS,
                                          errors=lambda x: [''], strict=False, neutral_tone_with_five=True)
            initials_tran = [initials_register[mode](i) for i in initials]
            finals_tran = [finals_register[mode](i) for i in finals]
            return [zero_initial_finals_register[mode](finals[x]) if i[0] == '' else i[0] + i[1]
                    for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.TONE:
            initials = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.INITIALS, strict=False,
                                            neutral_tone_with_five=True)
            finals = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.FINALS_TONE3,
                                          errors=lambda x: [' '], strict=False, neutral_tone_with_five=True)
            initials_tran = [initials_register[mode](i) for i in initials]
            finals_tran = [finals_register[mode](i) for i in finals]
            return [zero_initial_finals_register[mode](finals[x][:-1]) + finals[x][-1]
                    if i[0] == '' else i[0] + i[1] + finals[x][-1]
                    for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.INITIALS:
            initials = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.INITIALS, strict=False,
                                            neutral_tone_with_five=True)
            finals = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.FINALS, strict=False,
                                          neutral_tone_with_five=True)
            initials_tran = [initials_register[mode](i) for i in initials]
            finals_tran = [finals_register[mode](i) for i in finals]
            return [zero_initial_finals_register[mode](finals[x])[0] if i[0] == '' else i[0]
                    for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.FINALS:
            initials = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.INITIALS, strict=False,
                                            neutral_tone_with_five=True)
            finals = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.FINALS, strict=False,
                                          neutral_tone_with_five=True)
            initials_tran = [initials_register[mode](i) for i in initials]
            finals_tran = [finals_register[mode](i) for i in finals]
            return [zero_initial_finals_register[mode](finals[x])[1] if i[0] == '' else i[1]
                    for x, i in enumerate(zip(initials_tran, finals_tran))]
        elif style == Style.FINALS_TONE:
            initials = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.INITIALS, strict=False,
                                            neutral_tone_with_five=True)
            finals = pypinyin.lazy_pinyin(hans, tone_sandhi=tone_sandhi, style=pypinyin.FINALS_TONE3, strict=False,
                                          neutral_tone_with_five=True)
            initials_tran = [initials_register[mode](i) for i in initials]
            finals_tran = [finals_register[mode](i) for i in finals]
            return [zero_initial_finals_register[mode](finals[x][:-1])[1] + finals[x][-1]
                    if i[0] == '' else i[1] + finals[x][-1]
                    for x, i in enumerate(zip(initials_tran, finals_tran))]
        else:
            raise ValueError('style must be one of NORMAL, TONE, INITIALS, FINALS, FINALS_TONE')
    except KeyError:
        print("mode not found:", mode)
        return None
