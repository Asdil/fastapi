# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jwt
   Description :
   Author :       asdil
   date：          2022/6/16
-------------------------------------------------
   Change Activity:
                   2022/6/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import jwt
from core import conf
from jwt import PyJWTError
from fastapi import Depends
from datetime import datetime
from common import sqlite3_db
from datetime import timedelta
from passlib.context import CryptContext
from schemas.response import response_code

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# passlib 处理哈希加密的包
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """verify_password方法用于验证哈希密码

    Parameters
    ----------
    plain_password : str
        用户输入的密码
    hashed_password : str
        哈希密码

    Returns
    ----------
    flag : bool
        验证正确或者错误
    """
    flag = pwd_context.verify(plain_password, hashed_password)
    return flag


def get_password_hash(password):
    """get_password_hash方法用于获取哈希密码

    Parameters
    ----------
    password : str
        密码

    Returns
    ----------
    hash_password : str
        哈希密码
    """
    hash_password = pwd_context.hash(password)
    return hash_password


def verity_user(user, password):
    """verity_user方法用于查询数据库验证用户

    Parameters
    ----------
    user : str
        用户名
    password : str
        密码

    Returns
    ----------
    flag : bool
        是否匹配到用户名密码
    """
    ret = sqlite3_db.select_one(conf.SQL_LITE4, (user, ))
    if not ret:
        return False
    hashed_password = ret[0]
    if verify_password(password, hashed_password):
        return True
    return False


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    """create_access_token方法用于创建访问令牌

    Parameters
    ----------
    data : dict
        用户数据
    expires_delta : 过期时间
        timedelta

    Returns
    ----------
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta  # expire 令牌到期时间
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, conf.SECRET_KEY, algorithm=conf.ALGORITHM)
    return encoded_jwt


async def verify_token(token: str = Depends(oauth2_scheme)):
    """verify_token方法用于验证token

    Parameters
    ----------
    token : str
        token字符串

    Returns
    ----------
    """
    credentials_exception = response_code.http_exception(401, 'token验证错误', {"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, conf.SECRET_KEY, algorithms=[conf.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    flag = sqlite3_db.select_one(conf.SQL_LITE5, (username,))
    if not flag:
        raise credentials_exception
    return True


async def login_for_access_token(form_data):
    """login_for_access_token方法用于获取token

    Parameters
    ----------
    form_data : OAuth2PasswordRequestForm
        表单数据

    Returns
    ----------
    """
    # 1、验证用户名密码是否正确
    if not verity_user(form_data.username, form_data.password):
        raise response_code.http_exception(401, '用户名密码错误', {"WWW-Authenticate": "Bearer"})
    # 2、access_token_expires访问令牌过期
    access_token_expires = timedelta(minutes=conf.ACCESS_TOKEN_EXPIRE_MINUTES)
    # 3、create_access_token创建访问令牌
    access_token = create_access_token(data={"sub": form_data.username},
                                                expires_delta=access_token_expires)
    # 返回token
    return {"access_token": access_token, "token_type": "bearer"}


if __name__ == '__main__':
    password = 'maintainer'
    # print(get_password_hash(password))
    print(verity_user('root', password))
