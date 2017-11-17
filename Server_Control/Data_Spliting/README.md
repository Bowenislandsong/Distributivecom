# Data split 

## Environment & Running Instruction
Place the files in a sibling folder as Resource and Coding.

Run with "java -cp "zip4j_1.3.2.jar:commons-io-2.6.jar:" Main <Resourcefoldername> <Codingfoldername> <#ofNodes>"

For example: java -cp "zip4j_1.3.2.jar:commons-io-2.6.jar:" Main Resourse Code 5

Application will return on "System.exit" an int value for the actual number of nodes needed. This number will be equal or less than claimed number
of nodes.

Output of the application will be zip files named "Distribute#". # will be based 0 to number of nodes required-1. THe zip file contains code and segmented recourses.

