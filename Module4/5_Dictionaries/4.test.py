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

'''Remember the del is also allow in dicts'''
'''10. del'''
del jobs['firefighter']
print(jobs)
del jobs
try:
    print(jobs)
except NameError:
    print('The list was deleted')