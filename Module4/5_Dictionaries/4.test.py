jobs={
    'nurse': ['brother', 'dad', 'mom', 'wife', 'me'],
    'software developer': ['me'],
    'firefighter': ['anyone']
    }

'''1. iterate the dict the next methods are similar'''
'''a)'''
for job in jobs:
    print('job:', job, 'people:', jobs[job])

'''b'''
for job in jobs.keys():
    print(f'job: {job} people: {jobs[job]}')

'''2. .values method'''
print(jobs.values())

'''3. items'''
print(jobs.items())

'''4. update'''
jobs.update({'doctor': ['Strange']})
print(jobs)

'''The next methods can keep a value in another variable'''
'''5. popitem'''
dr=jobs.popitem()
print(dr)
print(jobs)

'''6. get'''
enfermeros=jobs.get('nurse')
print(enfermeros)

'''7. copy'''
trabajos=jobs.copy()
print(trabajos)

'''8. clear'''
trabajos.clear()
print(trabajos)

'''9. sorted'''
print('sorted function')
print(sorted(jobs))
sortedJobs=sorted(jobs)
print(sortedJobs)

'''10. There is another method it calls .pop, it's similar to
popitem() method but works different:'''
elementPop=jobs.pop('software developer')
print(f'using pop() method: {elementPop}')
print(f'this is the result after applying the pop method: {jobs}')

'''Remember the del is also allow in dicts'''
'''10. del'''
del jobs['firefighter']
print(jobs)
del jobs
try:
    print(jobs)
except NameError:
    print('The list was deleted')
    
'''11. There is another way to updata a dictionary'''
dictionary={}
#This way is well-known
dictionary.update({'a': 1})
print(dictionary)
#But this is a new one
dictionary['b']=2,
print(dictionary)
#And remember how to access to a specific element
print(dictionary['b'])
print(dictionary['b'][0])