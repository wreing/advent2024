
def day03_1(input):
    input ='xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    total = 0
    do = True
    for i in range(len(input)):
        #print(input[i], input[i+1], input[i+2], input[i+3] )
        if do:
            if input[i] == 'm' and input[i+1] == 'u' and input[i+2] == 'l' and input[i+3] == '(':
                j = i+4
                a = 0
                while j < len(input) and input[j].isnumeric():
                    a = a*10 + int(input[j])
                    j += 1
                if input[j] == ',':
                    j += 1
                    b = 0
                    while j < len(input) and input[j].isnumeric():
                        b = b*10 + int(input[j])
                        j += 1
                    if input[j] == ')':
                        print(a,b, total, a*b, total + a*b)
                        total += a*b
            if input[i] == 'd' and input[i+1] == 'o'  \
                and input[i+2] == 'n' and input[i+3] == '\'' and input[i+4] == 't' \
                and input[i+5] == '(' and input[i+6] == ')':
                print("don't")
                do = False
        else:
            # look for dok
            if input[i] == 'd' and input[i+1] == 'o' \
                    and input[i+2] == '(' and input[i+3] == ')':
                print("do")
                do = True
    return total




def day03_2(input):
    def day03_1(input):
        input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        total = 0
        for i in range(len(input)):
            # print(input[i], input[i+1], input[i+2], input[i+3] )
            if input[i] == 'm' and input[i + 1] == 'u' and input[i + 2] == 'l' and input[i + 3] == '(':
                j = i + 4
                a = 0
                while j < len(input) and input[j].isnumeric():
                    a = a * 10 + int(input[j])
                    j += 1
               if input[j] == ',':
                   j += 1
                   b = 0
                   while j < len(input) and input[j].isnumeric():
                       b = b * 10 + int(input[j])
                       j += 1
                  if input[j] == ')':
                       print(a, b, total, a * b, total + a * b)
                       total += a * b
           if input[i] == 'd' and input[i + 1] == 'o' \
              and input[i + 2] == 'n' and input[i + 3] == '\'' and input[i + 4] == 't' \
              and input[i + 5] == '(' and input[i + 6] == ')':
                    print("don't")
                    do = False
            else:
                # look for dok
                if input[i] == 'd' and input[i + 1] == 'o' \
                        and input[i + 2] == '(' and input[i + 3] == ')':
                    print("do")
                    do = True
        return total

    def day03_2(input):
        return None

