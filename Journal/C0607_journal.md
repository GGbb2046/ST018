#### Unfortunately, we missed our professor due to illness. We hope to see him in the next class. Take care professor.

##### There were 4 exercises that were undertaken watching the videos to the link.

1. C06Ex01 was similar to what we covered on the test. We created a pull request based on changes to a read only public repo. We performed this on an existing file.

2. Upon creating a pull request, a fork is displayed in our repo list. Under the next exercise, we cloned the fork of the public repo where we performed a pull request. We started working on it, making changes, addition and deletion.

3. Upon making changes to the fork, we again pulled request to the upstream repo which was a foreign repo created by our professor for testing purposes.

4. We also had an exercise where we performed a synch between changes in the local and git hub repo. We performed a pull orgin master, synched the git hub repo to the local, made changes in the local and pushed it upstream.

## question to the professor:
    a. what is a sub module.
    b. for class 6 exercises, i have made a public repo inside one of the exercises folder. 

5. 'git reset head <filename>' is used to unstage any staging before creating a commit

6. Similarly, git reset head --hard is used in resetting a previous commit and erase all the changes since.

7. ## creating branches, making changes and merging with the master

    1. listing all the branches (git branch) 
    2. creating a dev branch called "dev" (git branch dev).
    3. switching to  new dev branch (git checkout dev).
    4. make changes to any file in the branch. adding & commit.
    5. git status to get a view of the status of your repo.
    6. switching to the master branch (git checkout master)
    7. merging the dev branch into master (git merge dev).

    
## Please refer to sandbox folder to observe the below mentioned command outputs
## Enumerate: 
    Rather than to have count, we can use the enumerate function to bypass the need to count variables and avoid errors during programming.

## Split:
    Split can be used to split a string into a number of substrings. Split requires a delimiter where the splits are supposed to be made.

## Slice:
    Slice aids in the slicing of strings using the indexig feature already taught.

## Find:
    Find allows us to search for a string and returns an index to the start of the string found or -1 if the string was not found.

## Other methods:
    
    1. s.lower(), s.upper() lowercase or uppercase
    2. s.strip() acts like a trim command
    3. s.isalpha()/s.isdigit()/s.isspace() tests if all the string chars are in the various character classes
    4. s.startswith('other'), s.endswith('other') tests if the string starts or ends with the given other string
    5. s.replace('old', 'new') returns a string where all occurrences of 'old' have been replaced by 'new'
    6. s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. 

# String formatting: Enables us to format strings.
    1. Can set the width allocation to a field
    2. Can align the field left (<), right (>) or center (^)
    3. Can specify something about how a specific type is displayed - i.e. Specify the number of decimal          places to display for a float.
    4. The format specify must preceed a colon character


### Due to immutability, 
We would not be able to do the following

S1 = “hello”

S2=s1

S2[0] = “h”


However, we can do the following

L1= [1, 10,11,12]

L2=L1[:]

L2[0] =9

Print(L2)  [9,10,11,12]

## Reading and writing files
1. Files are typically text, binary, structure and unstructured.
    Some file types we will get acquainted later are csv, json, binary, shelf.
2. Binary files are not meant to be read directly on screen. While creating a json output, we will get to know one of the binary file.
3. Using with statement drops the requirement for closing the file. it's good to bring it into practice.
4. We would need to specify the location of the file that sits on another directory to call in for reading, writing or append purposes.
5. Please remember that while calling command line arguments - start with the python then your program name and the arguments without any parenthesis separated by a space.
6. Binary files saves proprietary data - example dll files of windows when trying to open them using text editor.
7. Structured text file manifest in the form of json or csv file. 
    CSV files are skeletal files without any formatting or flavor and just contain the raw data. Remember to call upon csv module when dealing with csv files.
    