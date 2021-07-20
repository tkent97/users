from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.user_id = data['users_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE users_id=%(id)s;"

        results = connectToMySQL('user_schema').query_db(query, data)
      
        if len(results) > 0:
            return results[0]
        else:
            return False

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('user_schema').query_db(query, data)