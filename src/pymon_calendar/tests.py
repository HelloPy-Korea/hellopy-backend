from datetime import date

from django.test import TestCase

from pymon_calendar.models import PymonCalendar  # your_app을 실제 앱 이름으로 변경


class PymonCalendarTestCase(TestCase):
    def setUp(self):
        # 테스트 데이터를 생성
        PymonCalendar.objects.create(year_month=date(2024, 1, 1), description="2024년 1월 데이터")
        PymonCalendar.objects.create(year_month=date(2024, 2, 1), description="2024년 2월 데이터")
        PymonCalendar.objects.create(year_month=date(2023, 3, 1), description="2023년 3월 데이터")

    def test_filter_by_year(self):
        # 2024년 데이터를 필터링
        year = "2024"
        filtered_data = PymonCalendar.objects.filter(year_month__year=int(year))

        # 필터링된 데이터 확인
        self.assertEqual(filtered_data.count(), 2)
        self.assertTrue(all(obj.year_month.year == 2024 for obj in filtered_data))

    def test_filter_by_year_no_results(self):
        # 2022년 데이터 필터링 (존재하지 않는 경우)
        year = "2022"
        filtered_data = PymonCalendar.objects.filter(year_month__year=int(year))

        # 필터링된 데이터가 없는지 확인
        self.assertEqual(filtered_data.count(), 0)
