
# Intelligent Shift Scheduling  
#### 智能排班软件

## Motivation:
A satisfactory shift schedule can be extremely hard to create. On the other hand, no matter how perfect the first schedule is at the time of launch, frequent adjustments are usually inevitable due to circumstances like an employee's illness or a no-show. Therefore, a broadly applicable, intelligent shift scheduling system that can react to the events of each day is required in the modern world. This app is designed and developed using technology from artificial intelligence (AI) and combinatorial optimization to quickly and effectively address such issues. It is powered by the following features:

## Features:
- A wide variety of employee shift scheduling issues are categorized and modeled by the number of shifts arranged on each day. Currently, one to eight shift arrangements per day are supported.
- The App is furnished with innovatively developed scheduling engines that make it simpler for the user to create, update, and iteratively optimize employee shift schedules.
- The App provides a collection of fundamental shift scheduling constraints for scheduling decision-making, which are extracted and derived from common and frequently used schedule requests. To satisfy numerous requirements in the real world, those constraints might be merged to form quite complicated constraints.
- The app uses reactive scheduling with constraint addition and removal to handle often changing requirements. To address the new request and create the least amount of perturbation, a minimal number of altered shifts are sorted in contrast to the existing schedule.
- Another characteristic of this app is its remarkable flexibility. It can be used to fulfill simple and complex scheduling tasks. The process of creating and revising schedules can be as easy as choosing an option and pressing a button. On the other hand, sophisticated strategies and techniques are also available to deal with difficult issues (e.g., decomposition of a problem and merging multiple scheduling results to form the final results).
- Each employee's total working hours, total number of shifts, total number of days off, and total number of shift types are comprehensively considered and handled in a schedule cycle. To achieve a better balance between the needs of the employees and the companies, constraint adjustment and optimization algorithms are applied.
- The scheduling outcomes will be shown in Gantt-charts and tables. Integration tools are provided to communicate with external systems (e.g., import employee data into the app, export results to an excel file, and send results to employees via text message or social media. etc.).

## Examples:
### 1. Creating a schedule for 9 employees over a 7-day period, subject to the following constraints:
   - Each day is divided into three 8-hour shifts. Each shift requires different number of employees.
     - A-shift：00:00-08:00（1 employee required）
     - B-sfhit：08:00-16:00（3 employees required）
     - C-shift：16:00-24:00（3 employees required）
   - Every day, no employee works more than one shift.
   - Number of shifts are evenly assigned to employees.
   - Each employee has at least one day off in the 7-day period.

App Result:
![image](https://user-images.githubusercontent.com/84350533/119012794-a5a1a800-b996-11eb-8254-cbe54cebc874.png)
In this shift schedule, 4 employees work for 48 hours and 5 employees work for 40 hours a week. Shifts assined to each employee are spaced by at least 16 hours.

### 2. Creating a schedule for 10 employees over a 7-day period, subject to the constraints as listed in example 1.

App Result:
![image](https://user-images.githubusercontent.com/84350533/183247091-44349e8b-6a47-492b-bb71-90b6bf94c437.png)
In this shift schedule, 9 employees work for 40 hours, 1 employee works for 32 hours a week. Shifts assigned to each employee are spaced by at least 24 hours. For each employee, different shift types are assigned on two adjacent days.

### 3. Creating a schedule for 35 employees over a 7-day period, subject to the following constraints:
   - Every day is divided into six 4-hour time slots. Each time slot requires different number of employees. 
     - A-slot：02:00-06:00（6 employee required）
     - B-slot：06:00-10:00（9 employees required）
     - C-slot：10:00-14:00（10 employees required）
     - D-slot：14:00-18:00（10 employees required）
     - E-slot：18:00-22:00（9 employees required）
     - F-slot：22:00-02:00（6 employees required)
   - Every day, 5 shifts are arranged as shown in the table below:
   
  ![image](https://user-images.githubusercontent.com/84350533/183245697-5dc5c5ad-f774-49d1-93ca-512be6bbd809.png)
   - Every day, no employee works more than one shift.
   - Each employee has two days off in the 7-day period. 
   - Number of shifts are evenly assigned to employees

App Result:
![image](https://user-images.githubusercontent.com/84350533/181852021-45e3dec2-4bf8-42b8-ab56-0e08492d99c3.png)
In this shift schedule, each employee works for 40 hours a week. Shifts assigned to each employee are spaced by at least 24 hours.

Email:weiran.aitech@gmail.com

30-07-2022, Eindhoven, The Netherlands.
