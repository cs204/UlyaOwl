def main():
    s = input()
    print(convert(s))

def convert (s: str):
    s = s.replace(':)','🙂')
    s = s.replace(':(','🙁')
    return s

main()