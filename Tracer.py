#Tracer is a type of functions that keeps Track of input and outputs of any function arguments
#and ability to show 1 Test Validation 

def Tracer(function,arr_args,arr_length,arg_type,check_all,arg_elmnt_type='',Test=''):
    if not callable(function):
        print("%s is not a Function"%function)
        return
    if len(arr_args)<arr_length:
        print("Error Parameter Number is less than {}".format(arr_length))
        return
    if not isinstance(arr_args,arg_type):
        print("Wrong Type Passed to Function %s"%function.__name__)
        print("Error Arg: %s"%arr_args)
        return 
    if check_all:#check all elements of the same type
        if  all(isinstance(arr_args,arg_elmnt_type) for elmnts in arr_args):
            print("Error at Function [%s]"%function.__name__)
            print("Wrong element in argument passed %s"%arr_args)
            return 
    print("Arguments: %s"%arr_args)
    result = function(arr_args)
    print("function {} == Result : {}".format(function.__name__,result))
    if Test!='':
        print("Expected Result %s"%Test)
    return result

#usage example 
# let fun(var->[]) function takes array Parameter
# Tracer(fun,var,len,[],True/False, optional[ (int/list/float) if check_all is False] , [expected output]