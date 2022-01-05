# Automatic Generated tutorial documentation

This is a tryout for auto generated tutorial documentation directly from the code files. For now this only works for python.

## Tutorial in MD with direct code snippets
Run this to try the snippet parser out:

    python snippet_parser.py source_code\test_code_snippets.md

Here first the markdown file build up and then the /snippet command takes out code snippets from the given python script. The result is given in /test_code_snippet_gen.md

## Full tutorial from one python file

 Run this in a terminal test out an example script.

    python tutorial_parser.py source_code/test_tutorial.py

This generates /generated/test_tutorial.md which is a markdown file with the code snippets within. It also generates /generated/test_tutorial_only_code.py, which is a python script with only code and none of the text.
