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
