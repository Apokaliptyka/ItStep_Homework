from dz55 import Vector
import pytest


@pytest.fixture
def vector_obj1():
    return Vector(1, 2, 3)


@pytest.fixture
def vector_obj2():
    return Vector(1, 2, 6)


@pytest.fixture
def vector_obj3():
    return Vector(1, 2, 6)


def test_can_create_obj(vector_obj1):
    assert vector_obj1.x == 1
    assert vector_obj1.y == 2
    assert vector_obj1.z == 3


def test_can_to_equal(vector_obj1, vector_obj2, vector_obj3):
    assert vector_obj1 != vector_obj2
    assert vector_obj3 == vector_obj2


def test_can_to_add(vector_obj1, vector_obj2):
    assert vector_obj1 + vector_obj2 == Vector(2, 4, 9)


def test_can_to_sub(vector_obj3, vector_obj2):
    assert vector_obj3 - vector_obj2 == Vector(0, 0, 0)


def test_can_to_mul(vector_obj1):
    vector1 = vector_obj1 * 6
    vector2 = 6 * vector_obj1
    assert vector1 == vector2

def test_can_to_len(vector_obj1):
    assert len(vector_obj1)==4

def test_can_to_neg(vector_obj1):
    assert -vector_obj1==Vector(-1,-2,-3)

def test_can_to_bool(vector_obj1):
    assert bool(vector_obj1)
    assert not bool(Vector(0,0,0))
