import json
import sys
from q_a_model import QAModel

# Read from data
with open("./data/courses.json") as course_file:
    courses = json.load(course_file)

for course in courses:
    print(course['id'], ": ", course['name'])

course_id = input("Kurs Id waehlen: ")

with open("./data/%s.json" % course_id) as q_a_file:
    json_list = json.load(q_a_file)

# Add if argument given
if len(sys.argv) == 2 and (sys.argv[1].lower() == 'add' or sys.argv[1].lower() == 'a'):
    question = input('Question: ')
    answer = input('Answer: ')
    json_list.append({
        'id': len(json_list)+1,
        'question': question,
        'answer': answer,
        'ok': 0
    })

# Construct Question List
else:
    q_a_list = []
    for q_a in json_list:
        q_a_list.append(QAModel(**q_a))

    q_a_list.sort(key=lambda x: x.weight, reverse=True)

    # Ask first 10 question
    cnt = 1
    ok_id_list = []
    wrong_id_list = []
    for q_a in q_a_list:
        if cnt > 10:
            break
        print(cnt, ": ", q_a.question)
        cnt = cnt + 1
        input()
        print(q_a.answer)
        ok = input("korrekt (y,N)? ")
        print()
        if ok.lower() == 'y':
            ok_id_list.append(q_a.id)
        else:
            wrong_id_list.append(q_a.id)

    # update json
    for json_obj in json_list:
        if json_obj["id"] in ok_id_list:
            json_obj["ok"] = json_obj["ok"] + 1
        elif json_obj["id"] in wrong_id_list:
            json_obj["ok"] = 0

with open("./data/%s.json" % course_id, "w") as out_file:
    out_file.write(json.dumps(json_list))
