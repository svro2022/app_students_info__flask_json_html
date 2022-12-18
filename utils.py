import json

#загружаем данные из из файла candidates.json
def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)

#возвращаем всех кандидатов
def get_candidates_all():
    return load_candidates()

#возвращаем кандидата по id
def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate["id"] == pk:
            return candidate
    return 'Not Found'

#возвращаем кандидата по name
def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


#возвращаем кандидата по skills
def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result
