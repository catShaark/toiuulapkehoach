import random



def distribute_candies(min_per_person, max_per_person, num_people, num_candies) -> list:
    candies_allocation = num_people * [min_per_person]

    left_out_candies = num_candies - num_people * min_per_person

    max_addtional_candies = max_per_person - min_per_person

    left_people = num_people 
    for i in range(num_people):
        left_people -= 1
        must_give_to_this_person = left_out_candies - left_people * max_addtional_candies
        if must_give_to_this_person > 0:
            candies_allocation[i] += must_give_to_this_person
            left_out_candies -= must_give_to_this_person
        else:
            addtional_candies_to_this_person = random.randint(0, min(max_addtional_candies, left_out_candies))
            candies_allocation[i] += addtional_candies_to_this_person
            left_out_candies -= addtional_candies_to_this_person
    
    return candies_allocation

def range_exclude(begin, end, exclude):
    l = []

    for i in range(begin, end):
        if i not in exclude:
            l.append(i)

    return l

class Solution():
    def __init__(self, input) -> None:
        pathout, N, M, K, t, s, g, a, b, c, d, e, f = input

        self.num_thesis = N
        self.num_teacher = M
        self.num_council = K
        self.thesis_teacher = t
        self.thesis_similarity_matrix = s
        self.thesis_teacher_similarity_matrix = g
        self.num_thesis_in_council_lower_bound = a
        self.num_thesis_in_council_upper_bound = b
        self.num_teacher_in_council_lower_bound = c
        self.num_teacher_in_council_upper_bound = d
        self.thesis_similarity_lower_bound = e
        self.thesis_teacher_similarity_lower_bound = f
        
        self.thesis_allocation = self.num_thesis * [None]
        self.teacher_allocation = self.num_teacher * [None]

        self.thesis_allocation_map = dict()
        self.teacher_allocation_map = dict()
        
        self.total_similarity = 0
        self.total_thesis_similarity = 0
        self.total_thesis_teacher_similarity = 0

        self.path_output = pathout

        self.thesis_list = list(range(N))
        self.teacher_list = list(range(M))
        self.teacher_thesis = [list() for x in range(self.num_teacher)]

        self.valid = True
        for i in range(self.num_thesis):

            self.teacher_thesis[self.thesis_teacher[i]-1].append(i)



    def distribute_thesis(self, banned_thesis_in_council):

        num_thesis_in_council = self.num_council * [0]
        full_council = []

        thesis_distributed = 0
        for council_id in range(self.num_council):
            random.shuffle(banned_thesis_in_council[council_id])
            the_rest_of_the_councils = range_exclude(0, self.num_council, [council_id] + full_council)
            if len(the_rest_of_the_councils) == 0:
                self.valid = False
                return 0
            random.shuffle(the_rest_of_the_councils)
            
            i = 0
            for thesis_id in banned_thesis_in_council[council_id]:
                distribute_to_council = the_rest_of_the_councils[i]
                self.thesis_allocation[thesis_id] = distribute_to_council
                thesis_distributed += 1

                i += 1
                if i == len(the_rest_of_the_councils):
                    i = 0

                num_thesis_in_council[distribute_to_council] += 1
                
                if num_thesis_in_council[distribute_to_council] == self.num_thesis_in_council_upper_bound:
                    full_council.append(distribute_to_council)
                    the_rest_of_the_councils.remove(distribute_to_council)
                    if len(the_rest_of_the_councils) == 0:
                        if thesis_distributed == self.num_thesis:
                            self.valid = True
                        else:
                            self.valid = False
                        return 0
                    i = random.randint(0, len(the_rest_of_the_councils) - 1)


                
                
                
        

        
    def init_Sol(self):
        random.shuffle(self.teacher_list)
    
        num_teacher_in_council = distribute_candies(self.num_teacher_in_council_lower_bound, self.num_teacher_in_council_upper_bound, self.num_council, self.num_teacher)
        marker = 0

        banned_thesis_in_council = [list() for i in range(self.num_council)]


        for council_id in range(self.num_council):
            for teacher_id in self.teacher_list[marker: marker + num_teacher_in_council[council_id]]:
                self.teacher_allocation[teacher_id] = council_id
                for thesis_id in self.teacher_thesis[teacher_id]:
                    banned_thesis_in_council[council_id].append(thesis_id)
            marker += num_teacher_in_council[council_id]
  

        self.distribute_thesis(banned_thesis_in_council)  
        if self.valid == True:
            self.tinhk_xy()


    def rang_buoc(self)->bool:
        if self.valid == False:
            return False
        # RB1
        for so_DA in self.thesis_allocation_map.values():
            if (len(so_DA) > self.num_thesis_in_council_upper_bound) or (len(so_DA) < self.num_thesis_in_council_lower_bound):
                return False
        # RB2
        for so_GV in self.teacher_allocation_map.values():      
            if (len(so_GV) > self.num_teacher_in_council_upper_bound) or (len(so_GV) < self.num_teacher_in_council_lower_bound):

                return False
        # RB3
        for i in range(self.num_thesis):

            if self.thesis_allocation[i] == self.teacher_allocation[self.thesis_teacher[i] - 1]:

                return False
            
        # RB4 do tuong dong DA&DA
        if not self._DA_and_DA():

            return False
        # RB5 do tuong dong GV&DA
        if not self._GV_and_DA():
            return False
        
        self.total_similarity = self.total_thesis_similarity/2 + self.total_thesis_teacher_similarity
        return True
    
    def tinhk_xy(self):
        k_x = {}
        for i in range(self.num_council):
            k_x[i] = []
        
        for i in range(self.num_thesis):
            k_x[self.thesis_allocation[i]] = k_x[self.thesis_allocation[i]] + [i]

        k_y = {}
        for i in range(self.num_council):
            k_y[i] = []
        
        for i in range(self.num_teacher):
            k_y[self.teacher_allocation[i]] = k_y[self.teacher_allocation[i]] + [i]

        self.thesis_allocation_map = k_x
        self.teacher_allocation_map = k_y


    def _DA_and_DA(self):
        self.total_thesis_similarity = 0
        for xs in self.thesis_allocation_map.values():
            for DA1 in xs:
                for DA2 in xs:
                    if DA1 == DA2: continue
                    if self.thesis_similarity_matrix[DA1][DA2] < self.thesis_similarity_lower_bound:
                        return False
                    else:
                        self.total_thesis_similarity += self.thesis_similarity_matrix[DA1][DA2]
        return True
    
    def _GV_and_DA(self):
        self.total_thesis_teacher_similarity = 0
        for k in range(self.num_council):
            for GV in self.teacher_allocation_map[k]:
                for DA in self.thesis_allocation_map[k]:
                    if self.thesis_teacher_similarity_matrix[DA][GV] < self.thesis_teacher_similarity_lower_bound:
                        return False
                    else:
                        self.total_thesis_teacher_similarity += self.thesis_teacher_similarity_matrix[DA][GV]
        return True
