from . import finals_register, initials_register, zero_initial_finals_register

initials_dict = {
    'sh': 'u',
    'ch': 'i',
    'zh': 'v'
}

finals_dict = {
    'ua': 'x',
    'ei': 'w',
    'e': 'e',
    'ou': 'z',
    'iu': 'q',
    'ue': 't',
    'u': 'u',
    'i': 'i',
    'o': 'o',
    'uo': 'o',
    'ie': 'p',
    'a': 'a',
    'ong': 's',
    'iong': 's',
    'ai': 'd',
    'ing': 'k',
    'uai': 'k',
    'ang': 'h',
    'uan': 'r',
    'an': 'j',
    'en': 'f',
    'ia': 'x',
    'iang': 'l',
    'uang': 'l',
    'eng': 'g',
    'in': 'b',
    'ao': 'c',
    'v': 'v',
    'ui': 'v',
    'un': 'y',
    'iao': 'n',
    'ian': 'm'
}

zero_initial_finals_dict = {
    'a': 'aa',
    'ai': 'ai',
    'an': 'an',
    'ang': 'ah',
    'ao': 'ao',
    'e': 'ee',
    'ei': 'ei',
    'en': 'en',
    'eng': 'eg',
    'er': 'er',
    'o': 'oo',
    'ou': 'ou'
}


@finals_register.register
@finals_register.register("小鹤")
def xiaohe(finals: str):
    return finals_dict.get(finals, finals)


@initials_register.register
@initials_register.register("小鹤")
def xiaohe(initials: str):
    return initials_dict.get(initials, initials)


@zero_initial_finals_register.register
@zero_initial_finals_register.register("小鹤")
def xiaohe(finals: str):
    return zero_initial_finals_dict.get(finals, finals)
