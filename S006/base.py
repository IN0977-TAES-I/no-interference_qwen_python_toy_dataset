def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError
        return func(*args, **kwargs)
    return wrapper


def get_user_profile(user_id):
    return db.query(user_id)


def update_user(user_id, data):
    return db.update(user_id, data)


def delete_user(user_id):
    return db.delete(user_id)
