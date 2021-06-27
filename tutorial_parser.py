import sys
import os
import copy


if __name__ == '__main__':

    tutorial_file_name = sys.argv[1]

    step_detected = False
    preamble_detected = False
    postamble_detected = False
    code_block_detected = False

    code_string = ''
    text_string = ''
    markdown_string = ''
    tutorial_text = []
    tutorial_code = []
    tutorial_preamble = ''
    tutorial_postamble = ''
    tutorial_code_only = ''
    tutorial_infos = []
    tutorial_info = {
        'nr': 0,
        'tutorial_text': ''}

    ## Parse the tutorial python file
    with open(tutorial_file_name, 'rt') as file:
        content = file.readlines()
        for line in content:

            if 'TUTORIAL_STOP' in line and preamble_detected:
                preamble_detected = False


            if preamble_detected:
                tutorial_preamble = tutorial_preamble + line.split("## ",1)[1] 

            if 'TUTORIAL_PREAMBLE' in line:
                preamble_detected = True

            ## TUTORIAL_STEP

            if 'TUTORIAL_STOP' in line and step_detected:
                step_detected = False
                if code_block_detected:
                    code_block_detected = False
                    #print(markdown_string, markdown_string.strip())
                    markdown_string = markdown_string.rstrip() + '\n```\n'
                tutorial_text.append(markdown_string)
                tutorial_info['tutorial_text'] = markdown_string
                print(tutorial_info)
                tutorial_infos.append(copy.deepcopy(tutorial_info))
                tutorial_code.append(code_string)
                tutorial_code_only = tutorial_code_only  + code_string.strip('\n') + '\n'

                text_string = ''
                code_string = ''
                markdown_string = ''


            if step_detected:
                ## Detect the text in the tutorial
                if '##' in line:
                    ## End the code block before anything is added
                    if code_block_detected:
                        code_block_detected = False
                        markdown_string = markdown_string.rstrip() + '\n```\n'
                    text_string = text_string + line.split("## ",1)[1] 
                    markdown_string = markdown_string + line.split("## ",1)[1] 

                ## if not, it is code!
                else:
                    code_string = code_string  + line
                    if code_block_detected== False:
                        code_block_detected = True
                        markdown_string = markdown_string + '```python' + line
                    else:
                        markdown_string = markdown_string  + line
                    
            if 'TUTORIAL_STEP:' in line:
                step_nr_str = line.split("TUTORIAL_STEP: ",1)[1]
                step_nr = int(step_nr_str)
                print(step_nr)
                tutorial_info['nr'] = step_nr
                step_detected = True

            if 'TUTORIAL_STOP' in line and postamble_detected:
                postamble_detected = False
            
            ## END TUTORIAL STEP

            if postamble_detected:
                tutorial_postamble = tutorial_postamble + line.split("## ",1)[1] 

            if 'TUTORIAL_POSTAMBLE' in line:
                postamble_detected = True

        
        ## Write the markdown file
        sorted_tutorial_infos = sorted(tutorial_infos, key=lambda k: k['nr']) 

        f = open('generated/test_tutorial.md', 'w')
        f.write(tutorial_preamble)
        for it in range(0, len(sorted_tutorial_infos)):
            f.write('## Step ' + str(sorted_tutorial_infos[it]['nr']) + '\n')
            f.write(str(sorted_tutorial_infos[it]['tutorial_text']))
            f.write('\n')
            f.write('\n')
        f.write('Full Code \n ===\n')
        f.write('\n```python \n')
        f.write(tutorial_code_only)
        f.write('``` \n')
        f.write('Conclusion \n ===\n')
        f.write(tutorial_postamble)
        f.close()

        # Write the python code only file

        f = open('generated/test_tutorial_only_code.py', 'w')
        f.write(tutorial_code_only)
        f.close()
        print(tutorial_infos)
        newlist = sorted(tutorial_infos, key=lambda k: k['nr']) 
        print(newlist)

'''
    print(tutorial_preamble)
    print('tutorial text')
    print(tutorial_text)
    print('tutorial code')
    print(tutorial_code)
    print(tutorial_postamble)
'''
