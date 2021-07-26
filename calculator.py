def main():
    text = input()
    top = 0
    islem = 0
    gec = ""
    gec2 = ""
    ilkislem = False
    for i,char in enumerate(text):
        if char == "+":
            islem = 1
        elif char == "-":
            islem = 2
        elif char == "*":
            islem = 3
        elif char == "/":
            islem = 4
        else:
            if islem != 0 and not ilkislem:
                ilkislem = True
                top = int(gec)

            if not ilkislem:
                gec += char
            else:
                gec2 += char

            if islem != 0:
                if i+1 == len(text):
                    pass
                elif not text[i+1].isdigit():
                    pass
                else:
                    continue
                if islem == 1:
                    top += int(gec2)
                    gec2 = ""
                if islem == 2:
                    top -= int(gec2)
                    gec2 = ""
                if islem == 3:
                    top *= int(gec2)
                    gec2 = ""
                if islem == 4:
                    top /= int(gec2)
                    gec2 = ""
                islem = 0

    print(top)

main()