from os import chdir, listdir, system, path


def main():
    choiceNum = getUserInput()
    directory = getDirectories()
    chdir(directory)
    if choiceNum == 1:
        flutterCleanProject()
    elif choiceNum == 3:
        flutterCleanDirectory()


def flutterCleanProject():
    system('flutter clean')


def flutterCleanDirectory():
    projectNumber = 0
    listOfProjects = listdir()
    for project in listOfProjects:
        if path.isdir(project):
            projectNumber += 1
            print('======BEGIN======')
            system('cd {0} && flutter clean'.format(project))
            print('=======END=====')

    print('{0} Projects Have Been Cleaned'.format(projectNumber))


def getUserInput():
    print("""
1 => For One Project
2 => For list Of Project
3 => For a Projects Directory
""")
    choiceNum = int(input('choice => '))
    return choiceNum


def getDirectories():
    directory = input("""
===================
Directory => """)
    return directory


if __name__ == "__main__":
    main()
