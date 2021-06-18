import sys
import os


if __name__ == '__main__':
    step_detected = False
    code_string = ''
    text_string = ''
    tutorial_text = []
    tutorial_code = []

    tutorial_code_only = ''
    ## Parse the tutorial python file
    with open('test_tutorial.py', 'rt') as file:
        content = file.readlines()
        for line in content:

            if 'AUTO_TUTORIAL_STOP' in line:
                step_detected = False
                tutorial_text.append(text_string)
                tutorial_code.append(code_string)
                tutorial_code_only = tutorial_code_only  + code_string.strip('\n') + '\n'
                text_string = ''
                code_string = ''


            if step_detected:
                if '##' in line:
                    text_string = text_string + line.split("## ",1)[1] 
                else:
                    code_string = code_string  + line
                    

            if 'AUTO_TUTORIAL:' in line:
                step_nr_str = line.split("AUTO_TUTORIAL:",1)[1]
                step_nr = int(step_nr_str)
                step_detected = True
        
        ## Write the markdown file
            
        f = open('test_tutorial.md', 'w')
        for it in range(0, len(tutorial_text)):
            f.write('## Step ' + str(it) + '\n')
            f.write(str(tutorial_text[it]))
            f.write('\n')
            f.write('```\n')
            f.write(str(tutorial_code[it].strip('\n')))
            f.write('\n```')
            f.write('\n')
        f.close()

        # Write the python code only file

        f = open('test_tutorial_only_code.py', 'w')
        f.write(tutorial_code_only)
        f.close()


    print('tutorial text')
    print(tutorial_text)
    print('tutorial code')
    print(tutorial_code)
