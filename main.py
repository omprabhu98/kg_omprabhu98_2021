import sys
def mappingf(string1,string2):
    if len(string1) != len(string2):
        return False

    map = [([0] * 2) for row in range(256)]
    for i in range(0,len(string2)):
        if map[ord(string1[i])][0] == 0:
            map[ord(string2[i])][1] = 1
            map[ord(string1[i])][0] = string2[i]

        elif map[ord(string1[i])][0] != string2[i]:
            return False

    return True

def main():
  string1 = sys.argv[1]
  string2 = sys.argv[2]
  print(mappingf(string1,string2));

main();
