# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_name(name, student_id):
    print('Student name is {}\nStudent id is {}'.format(name, student_id))
    print('\n')
    print('Student name is {one}\nStudent id is {two}'.format(one=name, two=student_id))
    names()


def names():
    names = ['Arjun', 'Avinash', 'Balaji', 'Bala Krishna', 'Bhanu Teja', 'Bharath', 'Chandramohan Reddy',
             [401, 402, 403, 404, 405, 406, 407]]
    print(names[6:7])
    print(names[7][6])


def dicx():
    d = {'Arjun': 401, 'Avinash': 402, 'Balaji': 403, 'BhanuTeja': 404, 'BalaKrishna': 405, 'Bharath': 406,
         'Chandramohan': {'details': [407, 2010, 8861163436]}}
    print("Year of joining: ")
    print(d['Chandramohan']['details'][1])


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    dicx()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
