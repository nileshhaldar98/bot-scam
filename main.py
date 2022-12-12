import os

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        # staging 
        os.system('git add data.txt')
        # commit 
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')
        return days * makeCommits(days - 1)
values = range(61)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
makeCommits(i)