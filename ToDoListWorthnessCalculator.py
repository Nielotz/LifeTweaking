from copy import deepcopy
from dataclasses import dataclass

@dataclass
class TaskProperty:
	comment: str
	scale: float
	value: float = 0


base_tasks_properties: dict = {
	"Use time": TaskProperty(comment="How many months will the thing be working / active / influencing anything", scale=1),
	"Monthly saving in PLN": TaskProperty(comment="How much money it will save per month", scale=1),
	"One time costs in PLN": TaskProperty(comment="How much money it will save per month", scale=1),
	"Monthly costs in PLN": TaskProperty(comment="How much money it will save per month", scale=1),
	"Monthly maintenance time": TaskProperty(comment="How much time it will consume on mainetnance per month", scale=1),
	"Monthly saving in time": TaskProperty(comment="How much time it will save on mainetnance per month", scale=1),
}

def calculate_worthness(tasks_properties):
	worthness = 0
	
	total_saved_money = tasks_properties["Use time"].value * tasks_properties["Monthly saving in PLN"].value
	total_saved_money = tasks_properties["Use time"].value * tasks_properties["Monthly saving in PLN"].value
	total_saved_money = tasks_properties["Use time"].value * tasks_properties["Monthly saving in PLN"].value
	

	worthness += total_saved_money / 100

def get_task_properties() -> dict:
	return deepcopy(base_tasks_properties) 

def fill_tasks_properties(tasks_properties):
	for task_property_name in tasks_properties:
		tasks_properties[task_property_name].value = 1

		while True:
			try: 
				value = input(f"Provide value for {task_property_name}: ")
				value = int(value)
				tasks_properties[task_property_name].value = value
				print(tasks_properties[task_property_name].value)
				break
			except Exception as e:
				print(f"Incorrect value {value}.")


print("Hello, I am a worthness calculator")
while True:
	tasks_properties = get_task_properties()
	fill_tasks_properties(tasks_properties)
	print(tasks_properties)
	worthness = calculate_worthness(tasks_properties)
	print(f"Calculated worthness: {worthness}\n")