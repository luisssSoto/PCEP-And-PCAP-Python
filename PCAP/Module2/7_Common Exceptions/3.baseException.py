""" Base Exception """
'''Tree:
BaseException'''
# Note: BaseException it's basically the same like only except:

try:
    anyExceptionYouWant
except BaseException as e:
    print(f'Base Exception the main root: ', e)