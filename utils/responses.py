import typing as t
from enum import IntEnum
from msgspec import json, Struct
from blacksheep import Content, Response

ENCODER = json.Encoder()
DECODER = json.Decoder()

JSON_CONTENT_TYPE = b"application/json"


def jsonify(data: "ApiResponse", status: int = 200) -> Response:
    """
    Returns a response with application/json content,
    and given status (default HTTP 200 OK).
    """
    return Response(
        status=status,
        headers=None,
        content=Content(content_type=JSON_CONTENT_TYPE, data=ENCODER.encode(data)),
    )


def pretty_jsonify(
    data: "ApiResponse",
    status: int = 200,
) -> Response:
    """
    Returns a response with indented application/json content,
    and given status (default HTTP 200 OK).
    """
    return Response(
        status=status,
        headers=None,
        content=Content(
            content_type=JSON_CONTENT_TYPE,
            data=(json.format(ENCODER.encode(data))),
        ),
    )


class StatusCode(IntEnum):
    # 通用状态码 (0 - 1999)
    SUCCESS = 0  # 成功
    INVALID_PARAMS = 1001  # 无效参数
    SERVER_ERROR = 1002  # 服务器错误
    PAGE_NOT_FOUND = 1003  # 页面未找到
    DATA_NOT_FOUND = 1004  # 数据未找到
    DATA_CONFLICT = 1005  # 数据冲突
    AUTH_FAILED = 1006  # 身份验证失败
    PERMISSION_DENIED = 1007  # 权限不足
    SERVER_EXCEPTION = 1008  # 服务器异常
    RANGE_NOT_SATISFIABLE = 1009  # 范围不满足


class ApiResponse(Struct):
    code: int = StatusCode.SUCCESS
    data: t.Optional[t.Union[str, list, dict]] = None
    message: str = ""
