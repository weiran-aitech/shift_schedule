
# Intelligent Shift Scheduling  
#### 智能排班软件

## Motivation:
A satisfactory shift schedule can be extremely hard to create. On the other hand, no matter how perfect the first schedule is at the time of launch, frequent adjustments are usually inevitable due to unexpected events like an employee's illness or a no-show. Therefore, a broadly applicable, intelligent shift scheduling system that can react to the events of each day is required in the modern world. This software is designed and developed to quickly and effectively address such issues using combinatorial optimization and artificial intelligence (AI) technologies. 
## Key features:
- A wide variety of employee shift scheduling issues are categorized and modeled by the number of shifts arranged on each day. Currently, one to eight shift arrangements per day are supported.
- This software is furnished with innovatively developed scheduling engines that make it simpler for the user to create, update, and iteratively optimize employee shift schedules.
- This software provides a collection of basic shift scheduling constraints for decision-making, which are extracted and derived from common and frequently used schedule requests. Rather than being presented as mathematical formulas, these constraints are expressed in simple, descriptive phrases. Multiple basic constraints may be combined to generate more complex constraints to cope with the various requirements that arise in the real world.
- One of the most notable advantages this software delivers is its reactive scheduling capability, with which user can dynamically add or remove constraints to tackle the challenges of ongoing schedule adjusment. In order to create the least amount of perturbation when a new request comes in, a minimal number of altered shifts are sorted in contrast to the existing schedule.
- Another characteristic of this software is its remarkable flexibility. It can be used to fulfill simple and complex scheduling tasks. The process of modeling, creating and revising schedules can be as easy as choosing an option and pressing a button. Moreover, sophisticated strategies and techniques are also available to deal with difficult issues (e.g., decomposition of a problem and merging multiple scheduling results to form the final results).
- Each employee's total working hours, total number of shifts, total number of days off, total number of different shift types, and shift intervals are comprehensively considered and handled in a schedule cycle. A balance between the needs of employees and companies is achieved by applying optimization algorithms.
- A cycle of a schedule may last one to seven days. The user has the choice to terminate a scheduling process after one cycle of scheduling is done or continue into the next cycle. In the latter case, the software will take the constraints and outcomes of the preceding cycle into account.
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
![image](https://user-images.githubusercontent.com/84350533/195989630-e41d4abd-19a0-4b4e-9808-cd04854909ce.png)
In this shift schedule, 4 employees work for 48 hours and 5 employees work for 40 hours a week. Shifts assined to each employee are spaced by at least 16 hours.

### 2. Creating a schedule for 10 employees over a 7-day period, subject to the constraints as listed in example 1.

App Result:
![image](https://user-images.githubusercontent.com/84350533/194903255-47e8b605-31fc-4276-b548-bc78046de343.png)
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

Eindhoven, The Netherlands
