def test_signup_successful(client):
    # Arrange
    email = "alice@mergington.edu"
    activity_name = "Basketball Team"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert email in result["message"]
    assert activity_name in result["message"]


def test_signup_duplicate_student_fails(client):
    # Arrange
    email = "duplicate@mergington.edu"
    activity_name = "Basketball Team"

    # Act
    first_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    second_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert "already signed up" in second_response.json()["detail"].lower()


def test_signup_activity_not_found(client):
    # Arrange
    email = "student@test.edu"
    activity_name = "Nonexistent Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
