# hellopy-backend

hellopy-backend

## 빠른 시작 가이드

```bash
# 개발 환경 설정
make setup

# DB 마이그레이션
make migration

# runserver (default port: 8080, host: 0.0.0.0)
make run

# runserver specific port
make run PORT=9999

# runserver localhost only
make run HOST=localhost

# run test
make test
```

## 개발 환경 설정 가이드

```text
make setup
```

### 패키지 매니저 사용법

#### 글로벌 디펜던시 설정

```bash
# 패키지 설치하기
# uv add <package name>
> uv add django

# 패키지 삭제하기
# uv remove <package name>
> uv remove django
```

#### 개발 디펜던시 설정

```bash
# 패키지 설치하기
# uv add --dev <package name>
# or uv add --group dev <package name>
> uv add --dev pre-commit

# 패키지 삭제하기
# uv remove --dev <package name>
# or uv add --group dev <package name>
> uv remove --dev pre-commit
```

## API 사용 예시 (아직 TAG는 적용 X)

()의 경우 '()'자체는 생략  
해당 내용에 맞게 변경해야하는 부분
ex) (id) -> 1

### (POST) FAQ 생성

```bash
curl -X POST http://localhost:8080/api/faqs/ \
     -H "Content-Type: application/json" \
     -d '{
         "question": "API란 무엇인가요?",
         "answer": "API는 애플리케이션 간의 통신을 위한 인터페이스입니다.",
         "question_type": "activity",
         "status": "normal"
     }'
```

```javascript
fetch("http://localhost:8080/api/faqs/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        question: "API란 무엇인가요?",
        answer: "API는 애플리케이션 간의 통신을 위한 인터페이스입니다.",
        question_type: "activity",
        status: "normal"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

### (GET) FAQ 조회
```bash
curl -X GET http://localhost:8080/api/faqs/
```

```javascript
fetch("http://localhost:8080/api/faqs/")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

### (GET) 특정 FAQ 조회
```bash
curl -X GET http://localhost:8080/api/faqs/(id)/
```

```javascript
fetch("http://localhost:8080/api/faqs/2/")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

### (PUT) FAQ 수정
```bash
curl -X PUT http://localhost:8080/api/faqs/(id)/ \
     -H "Content-Type: application/json" \
     -d '{
         "question": "REST API란 무엇인가요?",
         "answer": "REST API는 HTTP를 통해 데이터를 전송하는 API입니다.",
         "question_type": "activity",
         "status": "normal"
     }'
```

```javascript
fetch("http://localhost:8080/api/faqs/2/", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        question: "REST API란 무엇인가요?",
        answer: "REST API는 HTTP를 통해 데이터를 전송하는 API입니다.",
        question_type: "activity",
        status: "normal"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

### (PATCH) FAQ 부분 수정
```bash
curl -X PATCH http://localhost:8080/api/faqs/(id)/ \
     -H "Content-Type: application/json" \
     -d '{
         "answer": "REST API는 클라이언트와 서버 간의 통신을 돕는 인터페이스입니다."
     }'
```

```javascript
fetch("http://localhost:8080/api/faqs/2/", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer: "REST API는 클라이언트와 서버 간의 통신을 돕는 인터페이스입니다." })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

### (DELETE) FAQ 삭제
```bash
curl -X DELETE http://localhost:8080/api/faqs/(id)/
```

```javascript
fetch("http://localhost:8080/api/faqs/2/", {
    method: "DELETE"
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```