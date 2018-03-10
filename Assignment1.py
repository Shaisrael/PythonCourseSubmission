#First question solution
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    answer = False
    if len(word) >= 6:
        ind = 0
        for number in range(len(word)-5):
            if word[ind] == word[ind+1] and word[ind+2] == word[ind+3] and word[ind+4] == word[ind+5]:
                answer = True
                break
            ind += 1
    return answer

print(trifeca('aannsSsddd'))


# Second question solution
def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.
    """
    valid_num = []
    for num in range(100000, 1000000):
        st2test = str(num)[2:]
        if actual_test(st2test):
            num = num + 1
            st2test = str(num)[1:]
            if actual_test(st2test):
                num = num + 1
                st2test = str(num)[1:-1]
                if actual_test(st2test):
                    num = num + 1
                    st2test = str(num)
                    if actual_test(st2test):
                        valid_num.append(num-3)
    return valid_num

def actual_test(st2test):
    """
    checks whether a given string is a palindrome
    """
    if st2test == st2test[::-1]:
        return True

print(check_palindrome())


# Third question solution
# Mock data:
math_all_students = {'Mike': [97, 62], 'Nicole': [86, 91], 'Greg': [77, 74], 'Michelle': [82, 93], 'Dan': [95, 88], 'Arnold': [91, 92]}

hist_all_students = {'Mike': [88, 95], 'George': [64, 82], 'Greg': [68, 78], 'Jack': [91, 96], 'William': [95, 88],
                      'Jacklin': [58, 79], 'Michelle': [93, 75], 'Arnold': [67, 73]}

def compare_subjects_within_student(math_all_students,
                                    hist_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students aren't printed.
    """
    students_math = set(math_all_students.keys())
    students_hist = set(hist_all_students.keys())
    valid_students=students_math.intersection(students_hist) #Selecting 2-subject students
    princ_tab = dict.fromkeys(valid_students, 0) #Preparing a dictionary for students' names and "preferred" subject to satisfy principle request
    for name in valid_students:
        if max(math_all_students.get(name)) > max(hist_all_students.get(name)):
            princ_tab[name] = 'Math'
        elif max(math_all_students.get(name)) == max(hist_all_students.get(name)):
            princ_tab[name] = 'No difference'
        else:
            princ_tab[name] = 'History'
    return princ_tab

print(compare_subjects_within_student(math_all_students,hist_all_students))