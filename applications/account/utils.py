

def get_update_data(data):
    update_fields = ["user_name", "nick_name", "birthday", 'gender', 'description', 'password']
    update_data = dict()
    for field in update_fields:
        if field in data:
            update_data[field] = data[field]
    return update_data
