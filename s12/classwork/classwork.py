
# #      ⬇⬇⬇⬇⬇⬇⬇⬇ SETS ⬇⬇⬇⬇⬇⬇⬇⬇

# set1 = {1, 0, False, 5, 5}
# print(set1)

# for i in set1:
#     print(i)

# #      ⬇⬇⬇⬇⬇⬇⬇⬇ DICTIONARY ⬇⬇⬇⬇⬇⬇⬇⬇

# info = {"Name": "Meder", "Last Name": "Emilev", "Age": 18, "City": "Philadelphia"}

# for k, v in info.items():
#     print(k)
#     print(v)



# task 

company = {
    "name": "TechVision",
    "location": "Chicago",
    "founded": 2018,
    "departments": ["Engineering", "Marketing", "HR", "Sales"],
    "employees": {
        "E002": {
            "name": "Anna",
            "age": 25,
            "position": "Marketing Manager",
            "skills": ["SEO", "Content Creation", "Analytics"],
            "full_time": True
        },
        "E003": {
            "name": "James",
            "age": 29,
            "position": "HR Specialist",
            "skills": ["Recruiting", "Onboarding", "Communication"],
            "full_time": False
        },
        "E004": {
            "name": "Maria",
            "age": 31,
            "position": "Sales Executive",
            "skills": ["Negotiation", "CRM", "Lead Generation"],
            "full_time": True
        }
    },
    "projects": [
        {
            "id": "P001",
            "name": "Website Revamp",
            "status": "In Progress",
            "team": ["E001", "E002"]
        },
        {
            "id": "P002",
            "name": "Marketing Automation",
            "status": "Completed",
            "team": ["E002", "E004"]
        }
    ]
}


print(company['name'])
print(company['departments'])
print(company['employees']['E002']['position'])
print(company['employees']['E003']['full_time'])
print(company['projects'][1]['name'])









