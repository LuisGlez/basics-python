def hello_world():
    print("Hello, world!")
    

def hello_world_name(first_name):
    print(f'Hello, {first_name}!')
    
 
def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]
    
    print(f'Hello, {first_name} / {second_name} / {third_name}')   
    
  
def hello_world_keyword_arg(first_person, second_person):
   print(f'Hello, {first_person} / {second_person}')
 
 
def hello_world_arbitrary_keyword_args(**kwargs):
    # print(kwargs)
    # print(kwargs.get("second_person"))
    
    if kwargs.get("second_person") is None:
        rint(f'Hello, {kwargs["first_person"]}')
        print('No hay segunda persona')
    else:
        # rint(type(kwargs))
        print(f'Hello, {kwargs["first_person"]} / {kwargs["second_person"]}!') 

    
    
# hello_world()
# hello_world_name('Luis')
# hello_world_args('Sebastian', 'Daniel', 'Vanesa')
# hello_world_keyword_arg(first_person="Sebastian", second_person="Daniel")
hello_world_arbitrary_keyword_args(first_person="Vanesa", second_person="Jose")
hello_world_arbitrary_keyword_args(first_person="Vanesa")