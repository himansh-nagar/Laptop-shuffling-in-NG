import random 
import pprint
already_assined_laptops={2:'prakesh',3:'prince',8:'khalil',10:'bhavnesh',34:'sanjay',39:'ajay udayan',11:'kritiv',6:'rohit Yadav'}
List_of_laptops=[4,7,9,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,30,31,32,33,35,37,36]
List_of_students=['aakash verma','atul','bhaskar','rakesh','deepak sharma','paranthaman','vivek','chandan','shabid','biju','akhilesh','ramesh','mohit','prabhakar','md tarique','himanshu','tapas','sushant','yousuf','vishal','ankur','shubham + kartik','kaushal + raju','bilal + bijendra ','naved + viresh','rahul + deepak patal']
students_left=['amarpal','sonu','somesh','umesh']
random.shuffle(List_of_laptops)
random.shuffle(List_of_students)
new_assined_laptop={}

for i in List_of_laptops:
	random_owner=random.choice(List_of_students)
	new_assined_laptop[i]=random_owner
	List_of_students.remove(random_owner)
new_assined_laptop.update(already_assined_laptops)
pprint.pprint(new_assined_laptop)


