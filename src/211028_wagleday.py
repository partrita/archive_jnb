import random
from rich.console import Console
from rich.table import Table

employee_list = [
    "Eddy", "Elena", "Grace", "Henry", "Sam",
    "Shane","Angela", "Vera", "Smith","David",
    "Crystal", "Jay", "Logan", "Layla", "Andrew",
    "Anna", "Vivian", "Chloe", "Lucas", "Esther",
    "Jenny", "Stella", "Hailey", "Bianca", "Zena",
    "Sally", "Simon"
    
    ] #len(employee_list) = 26

## employee list json format

# employee_list = {
#     "master":[
#         {
#             "name":"Eddy",
#             "rank":"master",
#             "cell_phone":"",
#         },
#         {
#             "name":"Elena",
#             "rank":"master",
#             "cell_phone":"",
#         },
#     ],
#     "employee":[
#         {
#             "name":"Shane",
#             "rank":"champ",
#             "cell_phone":"",
#         },


#     ]
# }



# team_list = [
#     "team1",
#     "team2",
#     "team3",
#     "team4",
#     "team5"
# ]

# team_member = {
#     "team1": [],
#     "team2": [],
#     "team3": [],
#     "team4": [],
#     "team5": [],
# }
# for i in employee_list:
#     team_member[random.choice(team_list)].append(i)
# results
# {'team1': ['Andrew'], 'team2': ['Eddy', 'Elena', 'Grace', 'Shane', 'Crystal', 'Logan', 'Layla', 'Anna', 'Jenny'], 'team3': ['Vera', 'Smith', 'Chloe'], 'team4': ['Henry', 'Angela', 'David', 'Lucas', 'Esther', 'Stella', 'Zena', 'Sally'], 'team5': ['Sam', 'Jay', 'Vivian', 'Hailey', 'Bianca']}

team_number = 5
member_number = len(employee_list)//team_number
member_mod =  len(employee_list)%team_number

console = Console()
table = Table(show_header=True, header_style="bold magenta")

def pick_member():  
    if len(employee_list) >= member_number:
        team_member = random.sample(employee_list, member_number)
        for member in team_member:
            employee_list.remove(member)
        return team_member
    else:
        return employee_list

table.add_column("Team", justify="center")
table.add_column("Member")

for i in range(team_number):
    table.add_row(str(i+1),','.join(pick_member()))
console.print(table)
