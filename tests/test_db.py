from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='john', password='secret', email='john@email.com')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'john'))

    assert user.username == 'john'
