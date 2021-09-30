

# curl -v -H "X-Principal: {\"user_id\":1, \"student_id\":1}" -G localhost:7755/student/assignments
pytest -s tests/teachers_test.py -k "test_grade_assignment_cross"