import sys

def main():
    for line in sys.stdin:
        options = line.strip().split(";")
        output = ""
        
        if options[0] == "S":
            if options[1] == "M" or options[1] == "V":
                value = options[2]
                for i in value:
                    if i.isupper():
                        output += " "
                    output += i.lower()
                output = output.replace("()", "")
            elif options[1] == "C":
                new_str = options[2][0].upper() + options[2][1:]
                for i in new_str:
                    if i.isupper():
                        output += " "
                    output += i.lower()
                output = output[1:]
        elif options[0] == "C":
            words = options[2].split(" ")
            for word in words:
                output += word[0].upper() + word[1:]
            if options[1] == "M":
                output = output[0].lower() + output[1:] + "()"
            elif options[1] == "V":
                output = output[0].lower() + output[1:]
        print(output)

if __name__ == "__main__":
    main()

