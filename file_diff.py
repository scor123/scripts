"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
        Inputs:
          line1 - first single line string
          line2 - second single line string
        Output:
          Returns the index where the first difference between
          line1 and line2 occurs.

          Returns IDENTICAL if the two lines are the same.
        """
    if (line1 == line2):
        return IDENTICAL
    if(len(line1) == len(line2)):
        for letter1, letter2 in zip(range(len(line1)), range(len(line2))):
            if(line1[letter1] != line2[letter2]):
                return letter1
    elif(len(line1) > len(line2)):
        for letter1, letter2 in zip(range(len(line1)), range(len(line2))):
            if(line1[letter1] != line2[letter2]):
                return letter1
        length2 = len(line2)
        return line1.index(line1[length2])
    length1 = len(line1)
    if(line1 == line2[:length1]):
        return length1
    for letter1, letter2 in zip(range(len(line1)), range(len(line2))):
        if (line1[letter1] != line2[letter2]):
            return letter1
    return None
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if("\n" in line1) or ("\r" in line1) or("\n" in line2) or ("\r" in line2):
        return ""
    if(idx < 0) or (idx > len(line2)) or(idx > len(line1)):
        return ""
    str1 = ""
    for item in range(idx):
        item = ""
        str1 += item+"="
    str1 += "^"
    sen = line1 + "\n"+str1 +"\n"+line2+"\n"
    return sen




def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if(lines1 == lines2):
        return (IDENTICAL, IDENTICAL)
    if(len(lines1) < len(lines2)):
        lines1_length = len(lines1)
        return (lines1_length, 0)
    if (len(lines1) > len(lines2)):
        lines2_length = len(lines2)
        return (lines2_length, 0)


    for num, line1, line2 in zip(range(len(lines1)), lines1, lines2):
        if(singleline_diff(line1, line2) < 0):
            pass
        else:
            return (num, singleline_diff(line1, line2))
    return None

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename, "r")
    read = file.readlines()
    read1 = []
    for line in range(len(read)):
        if(read[line][-1] == "\n"):
            read1.append(read[line][0:-1])
        else:
            read1.append(read[line])
    file.close()
    return read1

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    lin_num, idx = multiline_diff(file1, file2)
    if(lin_num < 0):
        return "No differences\n"
    return "Line "+ str(lin_num)+":\n"+ singleline_diff_format(file1[lin_num], file2[lin_num], idx)










