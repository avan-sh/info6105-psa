# question from codesignal test
def check_all_saved_rectangles_fit(operation, saved_rectangles):
    rectangle_len = operation[1]
    rectangle_breadth = operation[2]
    fit = True
    
    for saved_rectangle in saved_rectangles:
        saved_len = saved_rectangle[1]
        saved_bre = saved_rectangle[2]
        align1_fit = (saved_len<=rectangle_len) & (saved_bre<=rectangle_breadth)
        align2_fit = (saved_len<=rectangle_breadth) & (saved_bre<=rectangle_len)
        fit = align1_fit or align2_fit
        if fit != True:
            return False
    
    return True

def check_max(operation, max_len, max_brea):
    rectangle_len = operation[1]
    rectangle_breadth = operation[2]
    align1_fit = (max_len<=rectangle_len) & (max_brea<=rectangle_breadth)
    align2_fit = (max_len<=rectangle_breadth) & (max_brea<=rectangle_len)
    fit = align1_fit or align2_fit
    return fit
    

def solution(operations):
    saved_rectangles = []
    max_len = 0
    max_bre = 0
    op = []
    for operation in operations:
        if operation[0] == 0:
            saved_rectangles.append(operation)
            saved_len = operation[1]
            saved_bre = operation[2]
            max_len, max_bre = max(saved_len, max_len),  max(saved_bre, max_bre)
        else:
            all_fit = check_max(operation, max_len, max_bre)
            # check_all_saved_rectangles_fit(operation, saved_rectangles)
            op.append(all_fit)
    return op

test1 = [[0,1,3], [0,4,2], [1,3,4], [1,3,2]]
print(solution(test1))
assert solution(test1) == [True, False]






a1 = "This is a mess@ge with no users"
a2 = "This is a message @id1 with 1 users"


id_grps = a1.split['@']
num_groups = len(id_grps)
for id_grp_index in range(1, num_groups):
    id_grp = id_grps[id_grp_index]
    # id_grp = 'id1,id2,id3'
    only_ids = id_grp.split(' ')[0]
    ids = only_ids.split(',')
    