def test_signup_new_account(app):
    username = "user12"
    password = "test"
    app.jamesHelper.ensure_user_exists(username, password)
