from fastapi import Request, HTTPException, Depends
import jwt

SECRET_KEY = "abcdefghijklmnopqrtuvwxyz"
ALGORITHM = "HS256"


def get_current_user(request: Request):
    """Decodes the JWT cookie and returns the payload ."""
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Login required")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


def require_role(*allowed_roles: str):
    """Dependency factory - use it to lock an endpoint to specific roles."""
    def role_checker(user: dict = Depends(get_current_user)):
        if user.get("role") not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Requires one of: {', '.join(allowed_roles)}"
            )
        return user
    return role_checker

allow_get = require_role("intern", "dev", "manager")
allow_write = require_role("dev", "manager")
allow_delete = require_role("manager")