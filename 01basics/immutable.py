'''
   the variables refer to a info. which is in the memory :
             
                     x=10 means       MEMORY
                                x------->10
                    y=x means   y---------^

                    x=15 means            
                                    x--/--10
                                             (now x does not refer to 10 as soon as you write x=15 x starts referring to memory location which has 15 as value BUT y still refers 10 )
                                    x---->15
               
                                    
                    >>> x=10
                    >>> y=x
                    >>> x,y
                    (10, 10)
                    >>> x=15
                    >>> x,y
                    (15, 10)
                    >>> y=x
                    >>> x,y
                    (15, 15)



'''