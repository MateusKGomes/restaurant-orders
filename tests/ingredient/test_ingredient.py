from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('tomate')
    ingredient2 = Ingredient('salmão')
    ingredient3 = Ingredient('tomate')


    assert ingredient.restrictions == set()
    assert ingredient.name == 'tomate'
    assert ingredient.__repr__() == "Ingredient('tomate')"
    assert ingredient.__eq__(ingredient2) is False
    assert ingredient.__eq__(ingredient3) is True
    assert ingredient.__hash__() == hash(ingredient)
    assert ingredient2.__hash__() != hash(ingredient)
