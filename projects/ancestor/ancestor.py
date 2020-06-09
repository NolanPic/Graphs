
def earliest_ancestor(ancestors, starting_node):
    # initialize the first path
    path = []
    # the list of paths that are possible earliest ancestors
    complete_paths = []
    # recurse
    _earliest_ancestor(ancestors, starting_node, path, complete_paths)

    # AT THIS POINT, complete_paths is populated with paths.
    # Now, we just need to see which path is the longest and
    # return the last item in that path

    # case where there is no parent
    if len(complete_paths) == 1:
        if len(complete_paths[0]) == 1:
            return -1
    
    # Now that we have a list of complete paths,
    # get the longest path (or, if two or more are the
    # longest, get the path with the lowest-valued, earliest ancestor).
    # Then, return the last item in that path
    possible_parents = []
    # sort the paths by length
    complete_paths = sorted(complete_paths, key=len, reverse=True)
    
    # the longest path will be at the front of the list,
    longest_path = len(complete_paths[0])
    
    # ...but there could be more paths with the SAME length. Let's find them.
    for i in range(len(complete_paths)):
        if len(complete_paths[i]) == longest_path:
            possible_parents.append(complete_paths[0][-1])
        else:
            # since the list is sirted, we know we're done
            break
    
    # next, find the lowest of the parents and return it
    possible_parents.sort()
    return possible_parents[0]
    
    
    

def _earliest_ancestor(ancestors, starting_node, path, complete_paths):
    
    # make a copy of the path
    copy_path = list(path)
    
    copy_path.append(starting_node)
    
    parents = get_parents(ancestors, starting_node)
    if len(parents) == 0:
        # no parents--we've reached the end of this path
        complete_paths.append(copy_path)
        return
    for parent in parents:
        _earliest_ancestor(ancestors, parent, copy_path, complete_paths)
        
    

def get_parents(ancestors, child):
    parents = []
    # loop thru ancestors -> [(1, 3), (2, 3)] etc.
    for rel in ancestors:
        # rel[1] == (1, 3)[1] == 3
        if rel[1] == child:
            parents.append(rel[0]) # <- append the direct parent
    return parents


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
    
    print(earliest_ancestor(test_ancestors, 6))
    print(earliest_ancestor(test_ancestors, 9))
    print(earliest_ancestor(test_ancestors, 11))
    
    print(earliest_ancestor(test_ancestors, 200))
