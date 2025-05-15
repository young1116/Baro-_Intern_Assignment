
**JWT Auth API 과제**

📌 배포 주소
[http://3.39.236.61:8000/swagger/](http://3.39.236.61:8000/swagger/)

✅ 구현 기능

* 회원가입 (POST /signup)
* 로그인 및 JWT 발급 (POST /login)
* JWT 인증 예외 처리

  * 토큰 없음
  * 토큰 만료
  * 토큰이 유효하지 않음

🧪 테스트

* pytest 기반 테스트 작성
* 성공/실패 케이스 테스트 완료

🛠 사용 기술

* Python 3.12
* Django 4.2
* Django REST Framework
* PyJWT
* drf-yasg (Swagger 문서화)
* AWS EC2 (Ubuntu 24.04)

⚙ 실행 방법

* git clone 후 가상환경 설정 및 패키지 설치
* `python manage.py migrate`
* `nohup python manage.py runserver 0.0.0.0:8000 &` 로 배포


