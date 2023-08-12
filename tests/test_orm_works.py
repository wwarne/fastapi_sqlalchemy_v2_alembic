from sqlalchemy import text

import orm


async def test_orm_session(session):
    user = orm.User(
        name="Michael",
        fullname="Michael Test Jr.",
    )
    session.add(user)
    await session.commit()

    rows = await session.execute(text('SELECT id, name, fullname FROM "user_account"'))
    result = list(rows)[0]
    assert isinstance(result[0], int)
    assert result[1] == "Michael"
    assert result[2] == "Michael Test Jr."
