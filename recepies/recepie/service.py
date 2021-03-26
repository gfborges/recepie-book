from typing import List, Dict

# TODO: split services
# TODO: inject db
class RecepieService():
    __recepies = [{
        "name": "Macarrão",
        "summary": "Receita de macarrão super especial que foi passada de geração em geração na minha familia. Este é o melhor macarrão que você vai comer na sua vida",
        "date": "20/12/20 10:55",
        "image": "https://www.spendwithpennies.com/wp-content/uploads/2019/03/Spaghetti-and-Meatballs-SpendWithPennies-4.jpg",
        "ingredients": [
            "molho de tomate",
            "massa de macarrão",
            "carne moida",
            "queijo ralado",
            "manjericão",
        ],
        "steps": [
            "cozinhar o macarrão em uma panela grande",
            "cozinhar a carne moída com temperos a sua escolha",
            "misturar o molho de tomate na carne moída e deixar o molho ficar consistente",
            "misturar o macarrão no molho",
        ],
        "link": "/recepie/0",
    },]

    __ingredients = [{
        "name": "limão",
        "summary": "fruta ácida",
        "date": "20/12/20 10:55",
        "image": "https://5.imimg.com/data5/QX/FQ/MY-68428614/lemon-500x500.jpeg",
        "link": "/ingredient/0",
    }]
    
    def get_recepies(self) -> List[Dict]:
        return self.__recepies

    def get_recepie(self, id) -> Dict:
        return self.__recepies[id]
    
    def get_ingredients(self) -> List[Dict]:
        return self.__ingredients
    
    def get_ingredient(self, id) -> List[Dict]:
        return self.__ingredients[0]
    
    def get_all(self) -> List[Dict]:
        return [*self.get_recepies(), *self.get_ingredients()]
    
    def find_many(self, query) ->List[Dict]:
        all = self.get_all()
        query = query.lower()
        return list(filter(lambda x: x["name"].lower().startswith(query), all))
