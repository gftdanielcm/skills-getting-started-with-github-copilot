def test_unregister_successful(client):
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert email in result["message"]
    assert activity_name in result["message"]


def test_unregister_student_removed(client):
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"

    # Act
    client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    response = client.get("/activities")

    # Assert
    participants = response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_not_signed_up_fails(client):
    # Arrange
    email = "unknown@student.edu"
    activity_name = "Basketball Team"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"].lower()


def test_unregister_activity_not_found(client):
    # Arrange
    email = "student@test.edu"
    activity_name = "Missing Club"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
