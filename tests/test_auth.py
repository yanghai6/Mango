from app.backend.services.service_auth import requires_scope, get_token_auth_header
from app.backend.exceptions.exception_auth_error import AuthError

import pytest
from jose import jwt
import json


class TestGetTokenAuthHeader:
    def test_get_token_auth_header_correctly_does_not_throw_error(self):
        get_token_auth_header("Bearer testJWT")

    def test_get_token_auth_header_missing_bearer_throws_error(self):
        with pytest.raises(AuthError) as e_info:
            get_token_auth_header("testJWT")
        assert (
            e_info.value.error["description"] == "Authorization header must start with"
            " Bearer"
        )

    def test_get_token_auth_header_invalid_format_throws_error(self):
        with pytest.raises(AuthError) as e_info:
            get_token_auth_header("Bearer test JWT 123")
        assert (
            e_info.value.error["description"] == "Authorization header must be"
            " Bearer token"
        )

    def test_get_token_auth_header_missing_JWT_throws_error(self):
        with pytest.raises(AuthError) as e_info:
            get_token_auth_header("Bearer")
        assert e_info.value.error["description"] == "Token not found"


class TestRequiresScope:
    def test_requires_scope_contain_scope_returns_true(self):
        scope = "read:data"
        token = jwt.encode({"scope": scope}, "secret", algorithm="HS256")
        assert requires_scope(scope, f"Bearer {token}")

    def test_requires_scope_missing_scope_returns_false(self):
        scope = "read:data"
        token = jwt.encode({"scope": "read:nothing"}, "secret", algorithm="HS256")
        assert not requires_scope(scope, f"Bearer {token}")


class TestExampleAuth:
    def test_public_endpoint(self, client):
        rv = client.get("/auth/test/public")
        assert "message" in json.loads(rv.data)

    def test_private_endpoint(self, client, mocker):
        mocker.patch(
            "app.backend.services.service_auth.is_token_valid", return_value=True
        )
        rv = client.get("/auth/test/private")
        assert "message" in json.loads(rv.data)

    def test_private_scoped_endpoint(self, client, mocker):
        mocker.patch(
            "app.backend.services.service_auth.is_token_valid", return_value=True
        )
        mocker.patch(
            "app.backend.services.service_auth.requires_scope", return_value=True
        )
        rv = client.get("/auth/test/private-scoped")
        assert "message" in json.loads(rv.data)

    def test_private_endpoint_missing_scope_fails(self, client, mocker):
        mocker.patch(
            "app.backend.services.service_auth.is_token_valid", return_value=True
        )
        mocker.patch(
            "app.backend.services.service_auth.requires_scope", return_value=False
        )
        rv = client.get("/auth/test/private-scoped")
        assert json.loads(rv.data)["code"] == "Unauthorized"
