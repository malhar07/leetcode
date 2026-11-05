/* Write your T-SQL query statement below */
SELECT s.student_id, s.student_name, su.subject_name, count(e.student_id) AS attended_exams

FROM Students s 
CROSS JOIN Subjects su
Left Join examinations e on e.subject_name = su.subject_name 
AND e.student_id = s.student_id
Group by s.Student_id, su.subject_name, s.student_name
order by s.student_id, su.subject_name;
