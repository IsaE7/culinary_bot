import sqlite3
from .queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as connect:
            connect.execute(Queries.CREATE_SURVEY_TABLE)
            connect.execute(Queries.DROP_CATEGORIES)
            connect.execute(Queries.CREATE_CATEGORIES_TABLE)
            connect.execute(Queries.POPULATE_CATEGORIES)
            connect.execute(Queries.DROP_DISHES)
            connect.execute(Queries.CREATE_DISHES_TABLE)
            connect.execute(Queries.POPULATE_DISHES)
            connect.execute(Queries.CREATE_USER_WARNINGS_TABLE)

            connect.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            connect.execute(query, params)

    def fetch(self, query: str, params: tuple = None, fetchmany: bool = True):
        with sqlite3.connect(self.path) as connect:
            result = connect.execute(query, params)
            result.row_factory = sqlite3.Row

            if fetchmany:
                to_return = result.fetchall()
                if not to_return:
                    return None
                return [dict(row) for row in to_return]
            else:
                to_return = result.fetchone()
                if not to_return:
                    return None
                return dict(to_return)
            # return result.fetchall()

    # def get_categories(self):
    #     with sqlite3.connect(self.path) as connect:
    #         data = connect.execute(Queries.GET_CATEGORIES)
    #         return data.fetchall()
    #
    # def get_recipes_by_category(self, category):
    #     with sqlite3.connect(self.path) as connect:
    #         data = connect.execute(Queries.GET_RECIPES_BY_CATEGORY, category)
    #         return data.fetchall()