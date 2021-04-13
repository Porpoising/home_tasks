import requests
import re

source1 = input().strip()
source2 = input().strip()
source2_text = requests.get(source2).text


def source_recursion(s1, s2, check=False):
    req = requests.get(s1)

    source_ref1 = re.findall(r'href=\"(.+)\"', req.text)
    if len(source_ref1) == 0:
        return 'No'

    for source in source_ref1:
        if source == source_ref1[-1]:
            check = True
        source_ref2 = re.findall(r'href=\"(.+)\"', requests.get(source).text)
        if s2 in source_ref2:
            return 'Yes'
        else:
            if check:
                return 'No'
            continue


print(source_recursion(source1, source2))
