import re
import os


def error_check() -> str:
    '''
    determines what type of error the expression generated
    '''
    
    while True:
        try:
            prompt = 'Please enter your expression: '
            expr = eval( input(prompt) )
            return 'No Error'
        except Exception as err:
            return "This is a {typ}\n{err}".format(typ=''.join([e for e in re.findall(r"\w*", str(type(err))) if 'error' in e.lower()]), err=err )
        
        
def sorter(L: list, descending: bool=False):
    maximum_so_far, rn = L[0], 0
    while len(L) > rn:
        
        if descending:
            print('Starting list for round {}: {}'.format(rn, L))
            for ind in range(len(L)):
                if ind == len(L)-1:
                    continue

                if L[ind] < L[ind+1]:
                    L[ind], L[ind+1] = L[ind+1], L[ind]
                    
        else:
            print('Starting list for round {}: {}'.format(rn, L))
            for ind in range(len(L)):
                if ind == len(L)-1:
                    continue

                if L[ind] > L[ind+1]:
                    L[ind], L[ind+1] = L[ind+1], L[ind]
            
        rn += 1
    return L


def file_search(search_from: 'path_like_str' = None, search_pattern_in_name: str = None, search_file_type: str = None,
                print_result: bool = False):
    """
    returns a str containing the full path/location of all the file(s)
    matching the given search pattern and file type
    """

    # raise error when invalid arguments are given
    if (search_from is None):
        raise ValueError('Please enter a valid search path')
    if (search_pattern_in_name is None) and (search_file_type is None):
        raise ValueError('Please enter a valid search pattern and/or file type')

    search_result = {}
    print(f"Starting search from: {search_from}\n")
    for fpath, folders, files in os.walk(search_from):
        for file in files:
            # when both search pattern and file type are entered
            if (search_file_type is not None) and (search_pattern_in_name is not None):
                if (search_file_type.split('.')[-1].lower() in file.lower().split('.')[-1]) and \
                        (search_pattern_in_name.lower() in file.lower().split('.')[0]):
                    search_result.setdefault(file, f'{fpath}\\{file}')

            # when file type is entered without any search pattern
            elif (search_pattern_in_name is None) and (search_file_type is not None):
                # print(search_file_type)
                if search_file_type.split('.')[-1].lower() in file.lower().split('.')[-1]:
                    search_result.setdefault(file, f'{fpath}\\{file}')

                    # when search pattern is entered without any file type
            elif (search_file_type is None) and (search_pattern_in_name is not None):
                if search_pattern_in_name.lower() in file.lower().split('.')[0]:
                    search_result.setdefault(file, f'{fpath}\\{file}')

    if print_result:
        for k, v in search_result.items():
            print(f"{k.split('.')[0]} is at {v}")

    return search_result