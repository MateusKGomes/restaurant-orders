import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


# Req 2
def test_dish():
    brasil = Dish('arroz e feijão', 12.00)
    japones = Dish('sushi', 50.00)
    ingredient = Ingredient('salmão')

    assert brasil.__repr__() == "Dish('arroz e feijão', R$12.00)"
    assert japones.__eq__(japones) is True
    assert japones.name == 'sushi'
    assert brasil.__hash__() != hash(japones)
    assert brasil.__hash__() == hash(brasil)
    japones.add_ingredient_dependency(ingredient, 5)
    assert japones.recipe == {ingredient: 5}
    assert japones.get_ingredients() == {ingredient}
    assert japones.get_restrictions() == {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED}
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('Name', 'float')
    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
        ):
        Dish('Name', 0)
