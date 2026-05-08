# Copilot gerou TODO com prompt: "pytest para anagramas e fibonacci"

import pytest
from algorithms.anagramas import sao_anagramas
from algorithms.fibonacci import fibonacci_posicao

def test_anagramas():
    assert sao_anagramas("ouvir", "virou") == True
    assert sao_anagramas("gato", "pato") == False

def test_fibonacci():
    assert fibonacci_posicao(0) == 0
    assert fibonacci_posicao(5) == 5
    assert fibonacci_posicao(10) == 55