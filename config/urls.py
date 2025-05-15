from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="JWT Auth API",
        default_version='v1',
        description="JWT 인증 기반 API 문서",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
    security_definitions={  # ✨ 이 부분 추가!
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT 인증: Bearer {your_token} 형식으로 입력'
        }
    }
)
