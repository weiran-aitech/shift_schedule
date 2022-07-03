
# Intelligent Shift Scheduling 
智能排班

Ceating an employee shift schedule can be an extremely complex optimization problem. The highlights of this Shift Scheduling system are:
1.  Models and solves a wide range of shift scheduling problems which are categorized by different number of shifts per day. Currently,  1/2/3/4/5/6/7/8 shifts per day are suppored.
2. A variety of shift constraints are presented for selection that can be applied to meet different requirements.
3. Incremental and iterative optimization is the core strategy in building a satisfactory shift schedule. 
4. Reactive scheduling algorithm with flexible constraint addition and removal plays a major role in dealing with the dynamically changing environment, such as frequently changed preference/availability of employees.
5. Provides useful references for mangement to minimize the total number of staffs and the administrative costs, and continuously optimize the employment struture.
6. The system is characterized by a high degree of flexibility. It is capable of coping with different application levels. At the basic level, a small number of staffs and shifts per day specified in the schedule, creating and repairing schedules can be easily operated in the system. At a higher level,  a large number of staffs and a bit more shifts per day specified in the schedule, a more complicated mechnism is available in the system to deal with these chanllenges (e.g. decompsition of a problem and merging multiple scheduling results to form the final results).
7. For each employee in certain period, the number and type of shifts, the number of day off and the total number of working hours are comprehasively considered. The employees' needs and companies' requirements can be well balanced with constraint adjustment.
8. Schedule tables are available to present the visible results. Customizable integrations tools are provided to communicate with external system (e.g. import employee data into the system, output schedule results to excel file)

# Shift-Scheduling Examples
员工轮班计划: 该如何做规律的三班倒排班?

现在共有9人，做轮换排班。
A班：0：00-8：00（仅限一人。且每人在同一个月平均一些，如果不平均在下个月也可以有补充。）
B班：8：00-16：00（共三人。不限次数。）
C班：16：00-24：00（共三人。不限次数。）
每个月按照有几个法定休息日进行休息。例如这个月共有五个周六，四个周日，那就是休息9天。
![image](https://user-images.githubusercontent.com/84350533/119012794-a5a1a800-b996-11eb-8254-cbe54cebc874.png)
在这个轮班计划里，有四个员工一周必须工作四十八小时

Email:weiran.aitech@gmail.com 2021-02-01
