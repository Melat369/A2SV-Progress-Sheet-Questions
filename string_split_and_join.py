def split_and_join(line):
    ret = line.replace(" ","-")
    return ret
    
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)