from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    recipe_1 = Ingredient('farinha')
    assert recipe_1.name == 'farinha'

    assert recipe_1.restrictions == {
        Restriction.GLUTEN,
    }

    assert hash('farinha') != hash(Ingredient('tomate'))
    assert hash('farinha') == hash(Ingredient('farinha'))
    assert recipe_1 == Ingredient('farinha')
    assert recipe_1 != Ingredient('tomate')

    assert repr(recipe_1) == "Ingredient('farinha')"
