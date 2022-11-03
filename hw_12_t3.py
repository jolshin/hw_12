import glob

def main():
    files = {}

    for file in glob.glob('*.txt'):
        with open(file) as f:
            files.update({file : len(f.readlines())})
    
    sorted_list = dict(sorted(files.items(), key=lambda item: item[1]))

    with open('output.txt', 'w') as f:
        for file in sorted_list:
            with open(file) as s:
                f.write(file + '\n')
                f.write(str(sorted_list[file]) + '\n')
                for line in s:
                    f.write(line)

                f.write('\n')

        print('создан файл \'output.txt\'')

main()