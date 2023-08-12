from fastapi import status


async def test_my_api(client, app):
    # Test to show that api is working
    response = await client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok", "data": []}

    response = await client.post(
        "/api/users/",
        json={"name": "Michael", "fullname": "Test Person"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    new_user_id = response.json()["data"]["id"]

    response = await client.get(f"/api/users/{new_user_id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status": "ok",
        "data": {
            "id": new_user_id,
            "name": "Michael",
            "fullname": "Test Person",
        },
    }

    response = await client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) == 1
