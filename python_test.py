dojos = [
    {
        "seattle" : {
            "python" : {
                "teacher" : "Graham",
                "TA" : "Reuben",
                "students" : [{"name": "Chee"},{"name": "Fong"}]
            },
            "mean" : {
                "teacher" : "Alan",
                "TA" : "Craig",
                "students" : [{"name": "Charlie"},{"name": "Carter"}]
            },
            "java" : {
                "teacher" : "Noelle",
                "TA" : None,
                "students" : [{"name": "Bob"},{"name": "Jack"}]
            }
        }
    },
    {
        "tulsa" : {
            "python" : {
                "teacher" : "Ryan",
                "TA": "Johnny",
                "students" : [{"name": "Dave"},{"name": "John"}]
            },
            "mean" : {
                "teacher" : "Vanessa",
                "TA": None,
                "students" : [{"name": "Matt"},{"name": "Grant"}]
            },
            "c#" : {
                "teacher" : "Michelle",
                "TA": "Ashley",
                "students" : [{"name": "Jonathan"},{"name": "Ratthew"}]
            }
        }
    },
    {
        "chicago" : {
            "python" : {
                "teacher" : "Clark",
                "TA": None,
                "students" : [{"name": "Anderson"},{"name": "Scott"}]
            },
            "mean" : {
                "teacher" : "Philip",
                "TA": None,
                "students" : [{"name": "Ed"},{"name": "Allen"}]
            },
            "java" : {
                "teacher" : "Ron",
                "TA": None,
                "students" : [{"name": "Elizabeth"},{"name": "Kim"}]
            }
        }
    }

]

# print all cities dojos are in

# # print all the teachers in the seattle dojo

# # print all the students in the tulsa campus

# # Chee changed his name to "Matt", apply it to the 'object'

# # The MEAN teacher in tulsa got replaced

# # transfer Ratthew to the Seattle campus

# for x in dojos:
#     print x

# for x in range(len(dojos)):
#     # print dojos[x]
#     for y in  dojos[x]:
#     #    print y
#        for z in dojos[x][y]:
#             # print z
#             print dojos[x][y][z]

#     print " "

# # print dojos[0]['seattle']['python']['teacher']



# temp = 

dojos[0]['seattle']['python']['students'][2] = dojos[1]['tulsa']['python']['students'][1]


dojos[1]['tulsa']['python']['students'].pop()