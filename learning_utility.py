


def longest_common_substring(string1, string2):
    counter = 0
    for x in range(len(string1)):
        if string1[x]==string2[x]:
            counter+=1
        else:
            break

    return string1[0:counter]

def length_lcs(string1,string2):
    return len(longest_common_substring(string1,string2))

s1 = "4831ff6a095899b6104889d64d31c96a22415ab2070f0556506a2958996a025f6a015e0f05489748b90200115c48136bd7514889e66a105a6a2a580f05595e5a0f05ffe6"
s2 = "4831ff6a095899b6104889d64d31c96a22415ab2070f0556506a2958996a025f6a015e0f05489748b90200115c48136bd7514889e66a105a6a2a580f05595e5a0f05ffe6"

print longest_common_substring(s1, s2)
print length_lcs(s1, s2)

