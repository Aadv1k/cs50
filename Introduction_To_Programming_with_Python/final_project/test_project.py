from dotenv import load_dotenv

load_dotenv()

from .project import Practically

p = Practically()
p.create_session_from_env("USERNAME", "PASSWORD")


def test_if_can_get_classroom():
    classrooms = p.get_classrooms()
    assert classrooms != None and len(classrooms) > 0


def test_if_classroom_is_initialized():
    classrooms = p.get_classrooms()
    assert classrooms[0].name != None


def test_if_user_can_login():
    user = p.get_user()
    assert len(user.first_name) > 1


def test_should_work_if_session_is_invalid():
    p.session_id = "foobarbaz"
    p.create_session_from_env("USERNAME", "PASSWORD")

    user = p.get_user()

    assert user is not None
    assert len(user.last_name) > 1
