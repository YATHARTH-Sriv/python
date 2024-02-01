'''
   accesing python shell hai whi IDLE hi hai but to access in vs code

   terminal>--python

   ##importing file into shell#####
   
   >>> import hello_world.py
     hello world
      4

    >>> import hello_world
     >>> hello_world.chai(score)
       43


       >>> hello_world.chai(4)
          4
    ###did some changes in hello_world.py####

        >>> hello_world.garlic(2)   
         Traceback (most recent call last):
         File "<stdin>", line 1, in <module>
         AttributeError: module 'hello_world' has no attribute 'garlic'
    
    #### changes are not reflected you have to reload the module############

         >>> from importlib import reload
         >>> reload(hello_world)
           hello world
            4

        >>> reload(hello_world)
           hello world
           4
          number of galic to be added 4
          changes to hello_world.py
            <module 'hello_world' from 'C:\\Users\\Yatharth srivastava\\Desktop\\python chai\\01_basics\\hello_world.py'>
          >>> hello_world.garlic(5)
          number of galic to be added 5

        




'''