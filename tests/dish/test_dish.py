import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient   # noqa: F401, E261, E501


def test_dish():
    dish_1 = Dish('pao', 15.00)
    ingredient_1 = Ingredient('farinha')
    assert dish_1.name == 'pao'
    dish_1.add_ingredient_dependency(ingredient_1, 5)
    assert dish_1.get_ingredients() == {ingredient_1}
    assert hash(dish_1) == hash(Dish('pao', 15.00))
    assert hash(dish_1) != hash(Dish('agua', 15.00))
    assert repr(dish_1) == "Dish('pao', R$15.00)"
    assert dish_1 == Dish('pao', 15.00)
    assert dish_1 != Dish('agua', 15.00)
    with pytest.raises(ValueError):
        Dish('acai', 0)
    dish_1.add_ingredient_dependency(ingredient_1, 1)
    with pytest.raises(TypeError):
        Dish('acai', '0')
    assert dish_1.get_restrictions() == ingredient_1.restrictions
