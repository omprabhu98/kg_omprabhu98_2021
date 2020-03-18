import sys
def mappingf(string1,string2):
    if len(string1) != len(string2):
        return False

    map = [[0] * 256] * 2

    for i in range(0,len(string2)-1):
        if map[0][ord(string1[i])] == 0:
            if map[1][ord(string2[i])] == 1:
                print(ord(string2[i]))
                return False
            map[1][ord(string2[i])] = 1
            map[0][ord(string1[i])] = string2[i]

        elif map[0][ord(string1[i])] != string2[i]:
            return False

    return True

def main():
  string1 = sys.argv[1]
  string2 = sys.argv[2]
  print(mappingf(string1,string2));

main();
