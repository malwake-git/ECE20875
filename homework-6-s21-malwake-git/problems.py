import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """


    str_search = re.search(r'^(\S?\d+\W?)\W?(\d+)\-(\d+)',searchstring)
    
    #str_search1 = re.search(r'^(\S\d+\W)(?=(\s|\d)\d+)',searchstring)

    #print(str_search)
    
    if (str_search):
        return True;
    else:
        return False;
    
    pass
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """

   

    #str_search1 = searchstring[::-1];
    #m = re.search('(AVE|St)\d+',str_search1);
    x = re.split('\d+',searchstring)[-1]
    str_search = re.search('(.*)\s(?=(Ave|St|Rd|Dr))',x)
    result = str_search.group();
    result1 = result.split(" ")[1:]

    
    
    return " ".join(result1)

    
    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """

    x = re.split('\d+',searchstring)[-1]
    #print(x)
    str_search = re.search('(\s.*)\s(?=(Ave|St|Rd|Dr))',x)
    group1 = str_search.group();
    group2 = group1
    part = str(group2[::-1]); # reverse
    x1 = set(x.split(" "))
    g1 = set(group1.split(" "))
    #last = []
    #print(x1)
    #print(g1)
    #for i in g1:
     #   for j in x1:
      #      if i != j:

    last = sorted(x1.difference(g1))

    #continue
    #last = x.split(" ")[2:]
    last = " ".join(last)
    result = searchstring.replace(x,part);

    return(result + last)
    
    pass


if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    #print(problem2('22 What A Wonderful Ave.'))
    #print(problem2('123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd.'))
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
    #print(problem3('Go West on 999 West St.'))
