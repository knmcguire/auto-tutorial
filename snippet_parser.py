import sys
import os
import copy


if __name__ == '__main__':
    markdown_file_name = sys.argv[1]

    f = open('generated/test_code_snippets_gen.md', 'w')


    with open(markdown_file_name, 'rt') as file:
        content = file.readlines()
        for line in content:
            if '/snippet' in line:
               split_lines = line.split(" ",2)
               python_file = split_lines[1]
               id = split_lines[2]
               id = id.strip("\n")
               with open(python_file, 'rt') as file2:
                    content2 = file2.readlines()
                    code_snippet_detected = False
                    for line2 in content2:
                        if '##! ' + id in line2:
                            if code_snippet_detected == True:
                                code_snippet_detected = False
                                f.write('``` \n')
                                continue
                            else:
                                code_snippet_detected = True
                                f.write('\n```python \n')
                                continue
                        if code_snippet_detected:
                            f.write(line2)
            elif '/fullcode' in line:
                split_lines = line.split(" ",1)
                python_file = split_lines[1]
                python_file=python_file.strip('\n')
                with open(python_file, 'rt') as file3:
                    content3 = file3.readlines()
                    f.write('\n```python \n')
                    for line3 in content3:
                        if "##!" not in line3:
                            f.write(line3)
                    f.write('``` \n')
            else:
                f.write(line)


    f.close()

     

               
