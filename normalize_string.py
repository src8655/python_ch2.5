# 문자열 데이터를 분석 하기전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리(Capitalize)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_string(strings):
    results = []
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        results.append(string)
    return results


results = clean_string(states)
print(results)

# ---------------------------------------------------
# ↑ 이런 방식보다 더 나은 방식
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results


def remove_special(s):
    return re.sub('[!#?]', '', s)


states = clean_strings(states, str.strip, str.title, remove_special)
print(states)
